import os

import os, sys, traceback, re, inspect, io
import datetime
import hashlib, secrets
from collections import defaultdict
import requests, json, string, time
from json import JSONEncoder

# Use this for testing and then make it true for all

def is_jsonable(x):
   try: json.dumps(x, cls=CustomJsonEncoder)
   except: return False
   return True

def only_jsonable(indict):
    return {k: v for k,v in indict.items() if is_jsonable(v)}

class CustomJsonEncoder(JSONEncoder):
    #Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

def typecasted(val, valtype=None):
    if valtype == "int": return int(float(val))
    if valtype == "float": return float(val)
    return val

def is_identifier(val):
    return val and (val not in ["None", "True","False"] and (val[0] == "_" or val[0] in string.ascii_letters))

def evalParamLiteral(param_val, param_type=None, runner=None):
    prnt = print
    if runner: prnt = runner.debugprint
    if type(param_val) is not str:
        prnt("Not str so returning: ", param_val)
        return param_val

    # Strings need careful treatment
    assert len(param_val) > 0, f"Param value ({param_val}) literals cannot be empty"
    if param_val[0] == "'" and param_val[-1] == "'":
        return param_val[1:-1]
    if param_val[0] == '"' and param_val[-1] == '"':
        return param_val[1:-1]
    if param_val.lower() in ("true", "false"):
        try:
            return bool(param_val)
        except:
            prnt("Cannot boolify: ", str(param_val))
    try: return int(param_val)
    except:
        prnt("Cannot intify: ", str(param_val))
    try: return float(param_val)
    except:
        prnt("Cannot floatify: ", str(param_val))

    if type(param_val) is datetime.datetime:
        return param_val.timestamp()

    # Dont call eval - very dangerous
    try:
        return json.loads(param_val)
    except Exception as exc:
        prnt("Error decoding param_val: ", param_val, traceback.format_exc())
    return None

class Sequence:
    def __init__(self,start=0):
        self.curr = start

    @property
    def next(self):
        self.curr += 1
        return self.curr

class Block:
    def __init__(self, block_type, title=""):
        self.title = ""
        self.block_type = block_type.lower().strip()

    def to_json(self):
        return {
            "type": self.block_type,
            "title": self.title,
        }

class Div(Block):
    def __init__(self):
        Block.__init__(self, "DIV", "")
        self.content = "Hello World"

    def to_json(self):
        out = super().to_json().copy()
        out.update({
            "content": self.content,
        })
        return out

class Table(Block):
    def __init__(self):
        Block.__init__(self, "TABLE", "")
        self.num_rows = 1
        self.num_cols = 1
        self.cell_values = defaultdict(lambda: defaultdict(lambda: None))
        self.cell_styles = defaultdict(lambda: defaultdict(lambda: None))
        self.has_header_row = False
        self.has_header_col = False

    def to_json(self):
        out = super().to_json().copy()
        cv = {}
        for r,rowvals in self.cell_values.items():
            for c, cellval in rowvals.items():
                if cellval is not None:
                    if r not in cv: cv[r] = {}
                    cv[r][c] = cellval

        cs = {}
        for r,rowvals in self.cell_styles.items():
            for c, cellval in rowvals.items():
                if cellval is not None:
                    if r not in cs: cs[r] = {}
                    cs[r][c] = cellval

        out.update({
            "num_rows": self.num_rows,
            "num_cols": self.num_cols,
            "cell_values": cv,
            "cell_styles": cs,
            "has_header_row": self.has_header_row,
            "has_header_col": self.has_header_col,
        })
        return out

    def setval(self, row, col, value):
        self.cell_values[row][col] = value

    def getval(self, row, col):
        return self.cell_values[row][col]

    def setstyle(self, row, col, style):
        self.cell_styles[row][col] = style

    def getstyle(self, row, col):
        return self.cell_styles[row][col]

class Plot(Block):
    def __init__(self):
        Block.__init__(self, "PLOT", "")
        self.xlabel = []
        self.ylabel = []
        self.traces = []

    def to_json(self):
        out = super().to_json().copy()
        out.update({
            "xlabel": self.xlabel,
            "ylabel": self.ylabel,
            "traces": self.traces,
        })
        return out

    def add_trace(self, name, xpts, ypts, tracetype="lines", extra=None):
        if tracetype == "pie":
           self.traces.append({
               "name": name,
               "labels": xpts,
               "values": ypts,
               "type": tracetype,
               "extra": extra
           })
        else:
           self.traces.append({
               "name": name,
               "x": xpts,
               "y": ypts,
               "type": tracetype,
               "extra": extra
           })

class TaskContext:
    """
    TaskContext is what is passed between tasks and keeps track of inputs and
    output variables.
    """
    __VERSION__ = "1"
    def __init__(self, runner, job_id, task_title, task_id, task_index, parent_context=None, all_tasks=None):
        self.parent_context = parent_context
        if parent_context: self.root = parent_context.root
        else: self.root = self

        self.start_seq = Sequence()
        self.finish_seq = Sequence()
        self.all_tasks = all_tasks
        self.runner = runner
        self.vars = {}
        self.called_with = {}
        self.recorded_vars = {}
        self.proceed = True
        self.logs = []
        self.skip_sub_tasks = False
        self.completed = False
        self.started_at = time.time()
        self.start_order = self.root.start_seq.next
        self.finish_order = -1
        runner.debugprint(("Entering ID: ", task_id, self.started_at))
        self.finished_at = -1
        self.job_id = job_id
        self.task_id = task_id
        self.task_title = task_title
        self.task_index = task_index
        self.stdout = io.StringIO()
        self.stderr = io.StringIO()
        self.stdall = io.StringIO()
        self.exception = None
        self.sub_tasks = []
        self.sub_task_call_info = []
        self.export_to_parent = {}
        # Blocks are custom elemnts we want to "send"
        self.blocks = []
        self._job_context = None
        self._curr_block_of_type = {}

    @property
    def runbook_task_id(self):
        return self.runner.runbook_task_id

    @property
    def starting_child_path(self):
        return self.runner.starting_child_path

    @property
    def starting_task_id(self):
        return self.runner.starting_task_id

    @property
    def curr_iter(self):
        return self.runner.curr_iter

    @property
    def job_context(self):
        if self.parent_context:
            return self.parent_context.job_context
        else:
            if self._job_context is None:
                self._job_context = {}
            return self._job_context

    @property
    def proceed(self):
        return self._proceed and not self.runner.is_stopped

    @proceed.setter
    def proceed(self, newval):
        self._proceed = newval
        if self.parent_context:
            self.parent_context.proceed = newval

    def is_allowed_var(self, vname):
        return vname not in ["self", "context"]

    def add_block(self, block, set_as_curr=True):
        self.blocks.append(block)
        if set_as_curr:
            self._curr_block_of_type[block.block_type] = block
        return block

    def remove_block(self, index):
        if index >= 0 and index < len(self.blocks):
            self.blocks.pop(index)

    def get_block(self, block_type, n, select=False):
        block_type = (block_type or "").strip().lower()
        typeblocks = self.blocks
        if block_type:
            typeblocks = [b for b in self.blocks if b.block_type == block_type]
        try:
            return typeblocks[n]
        except:
            return None

    def ensure_block(self, block_type, creator):
        if not self.get_block(block_type, -1):
            self.add_block(creator(), True)

    def newdiv(self, set_as_curr=True): return self.add_block(Div(), set_as_curr)
    @property
    def div(self):
        """ Gets the current table being worked on.  If one does not exist it is created. """
        self.ensure_block("DIV", lambda: Div())
        return self.get_block("DIV", -1, select=True)

    def newtable(self, set_as_curr=True): return self.add_block(Table(), set_as_curr)
    @property
    def table(self):
        """ Gets the current table being worked on.  If one does not exist it is created. """
        self.ensure_block("TABLE", lambda: Table())
        return self.get_block("TABLE", -1, select=True)

    def newplot(self, set_as_curr=True): return self.add_block(Plot(), set_as_curr)
    @property
    def plot(self):
        """ Gets the current plot being worked on.  If one does not exist it is created. """
        self.ensure_block("PLOT", lambda: Plot())
        return self.get_block("PLOT", -1, select=True)

    @property
    def index_path(self):
        parent = self.parent_context
        if self.task_id == "<root>": #or (parent and parent.task_id == "<root>"):
            return ""
        pip = parent.index_path
        if pip:
            return pip + f".{self.task_index}"
        else:
            return f"{self.task_index}"

    def record(self, varname, value):
        self.recorded_vars[varname] = value

    def log(self, level, data, print=False):
        if print: self.ctxprint(l)
        l = {"level": level, "data": data}
        self.logs.append(l)

    def to_json(self, include_sub_tasks=True):
        out = {
            "task_id": self.task_id,
            "task_title": self.task_title,
            "task_index": self.task_index,
            "proceed": self.proceed,
            "completed": self.completed,
            "index_path": self.index_path,
            "start_order": self.start_order,
            "finish_order": self.finish_order,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "var_values": {k: v for k,v in self.vars.items() if self.is_allowed_var(k)},
            "recorded_var_values": {k: v for k,v in self.recorded_vars.items() if self.is_allowed_var(k)},
            "stdout": self.stdout.getvalue(),
            "stderr": self.stderr.getvalue(),
            "stdall": self.stdall.getvalue(),
            "extras": { 
                "logs": self.logs,
                "plots": [p.to_json() for p in self.blocks if p.block_type == "plot"],
                "blocks": [b.to_json() for b in self.blocks],
                "st_call_info": self.sub_task_call_info,
                "called_with": self.called_with,
                "export_to_parent": self.export_to_parent,
            }
        }
        if self.exception:
            out["exceptions"] = [self.exception]
        if include_sub_tasks:
            out["sub_tasks"] = [c.to_json() for c in self.sub_tasks]
        return out

    def ctxprint(self, *args, **kwargs):
        ## curr_frame = inspect.currentframe()
        ## self.runner.debugprint(("Curr Frame: ", curr_frame))
        self.runner.ensureNotStopped()
        self.runner.debugprint((f"PRINTING ---------- ", args, kwargs))
        newkw = kwargs.copy()

        oldfile = newkw.get("file", None)
        streamname = ""
        if oldfile == sys.stderr:
            streamname = "stderr"
            newkw["file"] = self.stderr
            self.runner.orig_print(*args, **newkw)
        elif oldfile is None or oldfile == sys.stdout:
            streamname = "stdout"
            newkw["file"] = self.stdout
            self.runner.orig_print(*args, **newkw)
        else:
            # Should we even entertain this as we are here
            # writing to a non standard stream
            self.runner.debugprint("WARNING - Writing to a non std stream")

        self.postMessage("print", stream=streamname, args=args, kwargs=kwargs)

        # Write to "combined" output as a tee
        newkw["file"] = self.stdall
        self.runner.orig_print(*args, **newkw)

    def new_context(self, sub_task_id, sub_task_info):
        newcontext =TaskContext(self.runner, self.job_id, ALLTASKS[sub_task_id].get('title', ""),
                                sub_task_id, len(self.sub_tasks), self, self.all_tasks)
        self.sub_tasks.append(newcontext)
        self.sub_task_call_info.append(sub_task_info)
        return newcontext

    def invoke_task(self, task_id, func_name, task_param_values=None):
        self.runner.ensureNotStopped()
        self.runner.debugprint(f"InvokeTask {func_name}, Task Params: ", task_param_values)
        task_param_values = task_param_values or {}
        taskfunc = getattr(self.runner, func_name)
        task_input_params = self.all_tasks[task_id].get("input_params", [])
        task_output_params = self.all_tasks[task_id].get("output_params", [])
        self.runner.debugprint(f"Task Input Params: ", task_input_params)

        input_defaults = {}
        for inparam in task_input_params:
            def_val = inparam.get("default_value", "").strip()
            if def_val == "" or is_identifier(def_val): continue
            input_defaults[inparam["name"]] = evalParamLiteral(def_val, runner=self.runner)

        ## Create a subtask context
        # sub_task_context = self.new_context(task_id, task_param_values)
        sub_task_context = self.new_context(task_id, None)

        # when we do inputs at a root level we should *not* take from assignments
        input_asgns = {inparam["name"]: inparam["name"] for inparam in task_input_params}
        sub_task_context.copy_with_assignments(input_asgns, task_param_values, self.runner.special_param_values, input_defaults)
        if not taskfunc(sub_task_context): return False

        output_asgns = {outparam["name"]: outparam["name"] for outparam in task_output_params}
        self.copy_with_assignments(output_asgns, sub_task_context.vars)

        # Not really required as output asgns are in the client
        # but send for convinience
        for from_child, to_parent in output_asgns.items():
            if from_child != to_parent and from_child in sub_task_context.vars:
                sub_task_context.export_to_parent[to_parent] = sub_task_context.vars[from_child]

        return True

    def emit_wm_string(self, suffix):
        return self.invoke_command({}, f"""echo {self.wmprefix}_{suffix}""")

    def invoke_command(self, caller_locals, cmd_str, input_params=None):
        # cmd_str = json.loads(encoded_cmd_str)
        self.runner.ensureNotStopped()
        self.runner.debugprint("Decoded Command Str: ", cmd_str)
        self.runner.debugprint("Decoded Command Locals: ", caller_locals)
        self.runner.debugprint("Decoded Command Input Params: ", input_params)
        self.runner.debugprint("Decoded Special Param Vals: ", self.runner.special_param_values)

        # Render template through a particular engine (jinja etc)
        # This should happen before it is passed to cmd exec
        rendered_str = cmd_str
        input_params = input_params or []
        for ip in input_params:
            pname = ip["name"]
            pval = caller_locals.get(pname, self.runner.special_param_values.get(pname, ""))
            rendered_str = rendered_str.replace(f"<{pname}>", str(pval))

        # Send to cmd exec
        self.runner.debugprint("Rendered Command: ", rendered_str)

        hostname = self.runner.special_param_values.get(
                        "host", self.runner.special_param_values.get(
                            "hostname", caller_locals.get("hostname", None)))
        cred_label = self.runner.special_param_values.get(
                            "cred_label", caller_locals.get("cred_label", None))
        if not hostname and self.parent_context and "hostname" in self.parent_context.vars:
            hostname = self.parent_context.vars["hostname"]
        if not cred_label and self.parent_context and "cred_label" in self.parent_context.vars:
            cred_label = self.parent_context.vars["cred_label"]

        """
        print("TaskId: ", self.task_id)
        print("Parent: ", self.parent_context)
        print("HostName, CredLabel: ", hostname, cred_label)
        print("Runner Special Params: ", self.runner.special_param_values)
        print("Caller Locals: ", caller_locals)
        """
        tmpReq = {
            "user": self.runner.user_info["uid"],
            "cmd": rendered_str,
            "host": hostname,
            "cred_label": cred_label,
            "jwt": self.runner.daglib.jwt,
        }


        interactive = hostname not in ["", None]
        resp = self.runner.dispatchCommand(tmpReq, interactive)
        self.runner.debugprint(f"ExecuteCmd resp (hostname={hostname}, interactive={interactive}): ", resp)

        # Anything to be done for parent?
        retval = False
        if resp.status_code == 200:
            resp = resp.json()
            if "responsecode" not in resp or resp["responsecode"] == "True":
                self.vars["stdout"] = self.vars["stdall"] = resp["msg"]
                retval = True
            else:
                self.vars["stderr"] = self.vars["stdall"] = resp["msg"]
        else:
            resp = resp.content.decode()
            self.vars["stderr"] = resp
            self.vars["stdall"] = resp

        self.stdall.write(self.vars.get("stdall", ""))
        self.stderr.write(self.vars.get("stderr", ""))
        self.stdout.write(self.vars.get("stdout", ""))
        if self.parent_context:
            self.parent_context.vars["stdall"] = self.vars.get("stdall", "")
            self.parent_context.vars["stderr"] = self.vars.get("stderr", "")
            self.parent_context.vars["stdout"] = self.vars.get("stdout", "")
        return retval

    def invoke_sub_task(self, caller_locals, st_func_name, sub_task_info):
        """ Ensures a task is invoked with the right env. """
        self.runner.ensureNotStopped()
        self.runner.debugprint(f"InvokeSubTask {st_func_name}, Locals: ", caller_locals, "SubTaskInfo: ", sub_task_info)
        taskfunc = getattr(self.runner, st_func_name)
        stid = sub_task_info['taskid']
        task_input_params = self.all_tasks[stid].get("input_params", [])
        task_output_params = self.all_tasks[stid].get("output_params", [])

        input_defaults = {}
        for inparam in task_input_params:
            def_val = inparam.get("default_value", "").strip()
            if def_val == "" or is_identifier(def_val): continue
            input_defaults[inparam["name"]] = evalParamLiteral(def_val, runner=self.runner)

        ## Create a subtask context
        sub_task_context = self.new_context(stid, sub_task_info)

        ## copy inputs via in assignments
        stinputs = sub_task_info.get("inputs", {})

        input_asgns = {}
        for inparam in task_input_params:
            inpname = inparam.get("name", None)
            fromval = None
            if inpname in stinputs:
                fromval = stinputs[inpname]
            if not fromval: fromval = inpname
            if not is_identifier(fromval):
                fromval = inpname
            input_asgns[fromval] = inpname

        sub_task_context.called_with = sub_task_context.copy_with_assignments(input_asgns, self.vars, caller_locals, self.runner.special_param_values, input_defaults)

        # Call the task
        if not taskfunc(sub_task_context): return False

        ## copy outputs via out assignments
        stoutputs = sub_task_info.get("outputs", {})
        output_asgns = {outparam["name"]: 
                                (stoutputs.get(outparam["name"], None) or
                                 outparam["name"])
                        for outparam in task_output_params}
        self.copy_with_assignments(output_asgns, sub_task_context.vars)

        # Not really required as output asgns are in the client but send
        # for convinience
        for from_child, to_parent in output_asgns.items():
            if from_child != to_parent and from_child in sub_task_context.vars:
                sub_task_context.export_to_parent[to_parent] = sub_task_context.vars[from_child]

        return True

    def postStartedResponse(self, msg):
        msg = f"Task [{self.task_id}]: {msg}"
        resp = {"req": 'taskStarted'}
        resp["job_id"] = self.runner.job_id
        resp["job_iter"] = self.runner.curr_iter
        resp["conv_id"] = self.runner.conv_id
        resp['user'] = self.runner.user_info
        resp["msg"] = msg
        resp["results"] = self.to_json(False)
        self.runner.postResponse(resp)

    def postResponse(self, success, msg):
        # TODO - replace this with a direct api call to PUT /api/jobs/jobid/results
        msg = f"Task [{self.task_id}]: {msg}"
        resp = {"req": 'taskExecuted'}
        resp["job_id"] = self.runner.job_id
        resp["job_iter"] = self.runner.curr_iter
        resp["conv_id"] = self.runner.conv_id
        resp['user'] = self.runner.user_info
        resp["msg"] = msg
        resp["success"] = success
        resp["results"] = self.to_json(False)
        self.runner.postResponse(resp)

    def set_finished(self):
        self.finished_at = time.time()
        self.finish_order = self.root.finish_seq.next

    def taskStarted(self, caller_locals):
        self.postStartedResponse("Task Started")

    def taskFinished(self, success, localvars, output_params):
        self.completed = success
        self.set_finished()
        self.runner.debugprint(f"TASK SUCCESS ({self.task_id}, {self.task_index}), Locals: ", localvars, "OutputParams: ", output_params)
        #----------------------------------------------------------------
        # save locals to context so parent can read it as outputs
        #----------------------------------------------------------------
        for outparam in output_params:
            pname = outparam['name']
            if pname in localvars:
                self.vars[pname] = localvars[pname]

        self.postResponse(success, "Task Finished")
        return success

    def taskFailed(self, localvars, exc_info):
        self.runner.debugprint(traceback.format_exc())
        self.set_finished()
        exc_type, exc_value, exc_tb = exc_info
        # _exception_msg = 
        excmsg = traceback.format_exception(exc_type, exc_value, exc_tb)
        self.exception = {
            # "type": exc_type,
            "value": exc_value.args,
            # "tb": exc_tb,
            "msg": excmsg,
        }
        self.runner.debugprint("TASK FAILED ({self.task_id}, {self.task_index}) ....", self.exception)
        self.postResponse(False, "Task Failed: \n" + "\n".join(excmsg))
        return False

    def copy_with_assignments(self, var_assignments, *values_dicts):
        found = {}
        for inparam, outparam in var_assignments.items():
            for vdict in values_dicts:
                if inparam in vdict:
                    found[outparam] = self.vars[outparam] = vdict[inparam]
                    break
        return found

    def postMessage(self, cmd, **payload):
        payload["index_path"] = self.index_path
        payload["task_id"] = self.task_id
        self.runner.postMessage(cmd, **payload)

    def getlastval(self, varname, start_iter, end_iter=-1):
        """ Returns results between start_iter and end_iter inclusive. """
        if False:
            # Need to see how to cache this properly without running into boundary cases
            refresh_cache = False
            if end_iter < 0:
                return self.rescache.get(varname, {}).get(start_iter, None)
            else:
                out = []
                for i in range(start_iter, end_iter + 1):
                    out.append(self.rescache.get(varname, {}).get(i, None))
                return out
        prevresults = (self.runner.getresults(self.job_id, start_iter, end_iter) or {}).get("results", [])
        rootresults = [r for r in prevresults if r["task_id"] == self.runner.runbook_task_id and r["index_path"] == self.index_path]
        lastvals = [x.get("var_values", {}).get(varname, None) for x in rootresults]
        if end_iter < 0:
            return None if not lastvals else lastvals[0]
        else:
            return lastvals

    def getresults(self, start_iter, end_iter=-1):
        """ Returns results between start_iter and end_iter inclusive. """
        out = self.runner.getresults(self.job_id, start_iter, end_iter) or {}
        results = out.get("results", [])
        return out

class JobStoppedException(Exception):
    pass

class BaseJobRunner(object):
    def __init__(self, daglib, respq):
        self.hit_tasksvc_directly = True # For dev time only
        self.cmd_exec_url = os.environ.get('CMD_EXEC_URL', 'http://cmd-exec:7777/')
        self.stopped = False
        self._iter_id = 0
        self.daglib = daglib
        self.respq = respq
        self.starting_func_name = None
        self.starting_task_id = None
        self.starting_task_param_values = {}
        self.special_param_values = {}
        self.msgsender = None
        self.resp_sender = None
        self.command_caller = None
        self.job_stopped_file = None
        for name in dir(self.daglib):
            if not name.startswith("__"):
                globals()["_"+name] = getattr(self.daglib, name)

    def getresults(self, job_id, start_iter, end_iter=-1):
        """ Returns results between start_iter and end_iter inclusive. """
        dagknows_url = self.urlForJob(job_id, "results")
        headers = {
            'Authorization': 'Bearer ' + self.daglib.jwt,
            'Content-Type': "application/json"
        }
        resp = requests.get(f"{dagknows_url}?start_iter={start_iter}&end_iter={end_iter}", verify=False, headers=headers)
        return resp.json()

    def postMessage(self, cmd, **payload):
        if self.msgsender:
            self.msgsender.send(cmd, **payload)
        else:
            session_key = f"{self.starting_task_id}:{self.curr_iter}"
            payload["job_id"] = self.job_id
            payload["curr_iter"] = self.curr_iter
            payload["starting_task_id"] = self.starting_task_id
            print(f"postMessage: [{session_key}]: {cmd}: ", payload)

        # TODO - sent on WS if it is there

    def get_vault_key(self, key):
        resp = requests.post(self.cmd_exec_url + 'getVaultKey', json={
            "key": key,
            "jwt": self.daglib.jwt,
        })
        if resp.status_code != 200:
            print("CMD-EXEC ERROR: ", resp.status_code, resp.content)
            sys.stdout.flush()
            return None
        out = resp.json()
        return out["value"]

    @property
    def is_stopped(self):
        return self.stopped or (self.job_stopped_file and os.path.isfile(self.job_stopped_file))

    @property
    def curr_iter(self):
        return self._iter_id

    def debug(self):
        import ipdb ; ipdb.set_trace()

    def dispatchCommand(self, cmdParams, interactive=False):
        if self.command_caller:
            return self.command_caller(cmdParams, interactive)

        if interactive:
            return requests.post(self.cmd_exec_url + 'executeCommandInteractive', json=cmdParams)
        else:
            return requests.post(self.cmd_exec_url + 'executeCommand', json=cmdParams)

    def handleMessage(self, cmd, values):
        """ Note this method will be calledin script_exec so a lot of your cool dependencies may not exist """
        if cmd == "PRINT":
            print("PRINTING: ", values)
            sys.stdout.flush()
        elif cmd == "POST_RESPONSE":
            orig_response, token = values
            # print("TOKEN: ", token)
            # print("FULL RESPONSE: ", orig_response) 
            response = only_jsonable(orig_response)
            # print("ONLY JSONABLE RESPONSE: ", response)
            sys.stdout.flush()
            headers = {
                'Authorization': token,
                'Content-Type': "application/json"
            }
            try:
                reqname = orig_response.get("req", None)
                jsonbody = json.dumps(response, cls=CustomJsonEncoder)
                if reqname in ("taskExecuted", "taskStarted", "jobStarted", "jobFinished"):
                    # Use jobs api directly if we want
                    job_id = orig_response["job_id"]
                    dagknows_url = self.urlForJob(job_id, reqname)
                    rsp = requests.put(dagknows_url, data=jsonbody, verify=False, headers=headers)
                else:
                    response['proxy_session_id'] = os.environ['PROXY_SESSION_ID']
                    rsp = requests.post(os.environ['DAGKNOWS_URL'] + "/handleExecResponse", data=jsonbody, verify=False, headers=headers)
            except Exception as exc:
                print("Error posting response to dagknows: ", traceback.format_exc())

    def urlForJob(self, job_id, action="execsraw"):
        if self.hit_tasksvc_directly and os.environ.get("DAGKNOWS_TASKSVC_URL", "").strip():
            dagknows_url = os.environ["DAGKNOWS_TASKSVC_URL"].strip() + f"/jobs/{job_id}/{action}/"
        else:
            dagknows_url = os.environ['DAGKNOWS_URL'] + f"/api/jobs/{job_id}/{action}/"
        return dagknows_url

    def debugprint(self, *values):
        if self.respq:
            self.respq.put((f"[Stopped: {self.is_stopped}] PRINT", self, values))
        else:
            self.handleMessage(f"[Stopped: {self.is_stopped}] PRINT", values)

    def postResponse(self, resp):
        if self.resp_sender:
            self.resp_sender(self, resp)
            return

        tkn = 'Bearer ' + self.daglib.jwt
        if self.respq:
            self.respq.put(("POST_RESPONSE", self, (resp, tkn)))
        else:
            self.handleMessage("POST_RESPONSE", (resp, tkn))

    def ensureNotStopped(self):
        if self.is_stopped:
            raise JobStoppedException(f"##########       Job {self.job_id} stopped by user         ##########")

    #-------------------------------
    # run script and get results
    #-------------------------------
    def run(self, job_id=None, conv_id=None, user_info=None, iter_id=0):
        self.debugprint("Run Job Args: ", job_id, conv_id, iter_id)
        gb = globals()["__builtins__"]
        if hasattr(gb, "print"):
            self.orig_print = getattr(gb, "print")
        elif "print" in gb:
            self.orig_print = gb["print"]
        else:
            raise Exception("Invalid builtins")
        self.debugprint(f"Job {job_id} Run Started....")
        self._iter_id = iter_id
        self.job_id = job_id
        self.conv_id = conv_id
        self.user_info = {k: v for k,v in (user_info or {}).items() if k != "uname"}
        response = { "user_info": user_info }
        started_at = time.time()
        self.context = TaskContext(self, self.job_id, "", "<root>", 0, "", ALLTASKS)
        try:
            self.postResponse({
                "req": "jobStarted",
                "msg": f"Job Started: {job_id}",
                "iter": iter_id,
                "job_id": job_id,
                "started_at": started_at,
                "conv_id": conv_id,
                "user": {k: v for k,v in user_info.items() if k != "uname"},
                "task_id": self.starting_task_id ,
                "task_param_values": self.starting_task_param_values,
                "special_param_values": self.special_param_values,
            })
            tpv = self.starting_task_param_values
            self.debugprint("TASK PARAMS BEFORE EVAL: ", tpv)
            # for k,v in tpv.items(): tpv[k] = evalParamLiteral(v, runner=self)
            self.debugprint("TASK PARAMS AFTER EVAL: ", tpv)
            success = self.context.invoke_task(self.starting_task_id, self.starting_func_name, tpv)
            response['responsecode'] = f'{success}'
        except:
            response['responsecode'] = 'False'
            exc_type, exc_value, exc_tb = sys.exc_info()
            response['formatted_exc'] = traceback.format_exception(exc_type, exc_value, exc_tb)
            self.debugprint(f"Job {job_id} Exception: ", response['formatted_exc'])
            if self.daglib:
                response['formatted_lcls'] = self.daglib.formatLocals(exc_tb)
            else:
                response['formatted_lcls'] = exc_tb
            response['error_msg'] = ''.join(response['formatted_exc'])
        # response['exec_context'] = self.context.to_json()
        self.debugprint(f"Job {job_id} Run Finished....")
        self.postResponse({
            "req": "jobFinished",
            "msg": f"Job Finished: {job_id}",
            "job_id": job_id,
            "iter": iter_id,
            "started_at": started_at,
            "finished_at": time.time(),
            "conv_id": conv_id,
            "user": {k: v for k,v in user_info.items() if k != "uname"},
            "task_id": self.starting_task_id ,
            "task_param_values": self.starting_task_param_values,
            "special_param_values": self.special_param_values,
            "results": response,
        })
        # globals()["print"] = self.orig_print
        return response

class WSSender:
    def __init__(self, ws, runner):
        self.runner = runner
        self.ws = ws
        self.msgindex = 0

    def send(self, cmd, **payload):
        payload["job_id"] = self.runner.job_id
        payload["curr_iter"] = self.runner.curr_iter
        payload["runbook_task_id"] = self.runner.runbook_task_id
        payload["starting_child_path"] = self.runner.starting_child_path
        payload["starting_task_id"] = self.runner.starting_task_id
        self.msgindex += 1
        msg = json.dumps({
            "msgid": self.msgindex,
            "type": "cmd",
            "cmd": cmd,
            "payload": payload
        }, indent=2)
        # print("Sending Message: ", datetime.datetime.utcnow().isoformat(), msg)
        sys.stdout.flush()
        try:
            self.ws.send(msg)
        except Exception as e:
            print("Error sending on ws.  Will skip: ", e)
            sys.stdout.flush()

def runJob(job_class, iter_id, conv_id=None, user_info=None, token=None, execs_url=None, job_stopped_file = None, *args, **kwargs):
    global JOB_ID
    from daglib import daglib
    user_info = user_info or {}
    if type(user_info) is str:
        user_info = json.loads(user_info)
    builtins = globals()["__builtins__"]
    dlb = daglib(None, user=user_info.get("uname"), jwt=token)
    j = job_class(dlb, None)
    j.job_stopped_file = job_stopped_file
    ws = None
    if execs_url:
        # wsurl = f"{execs_url}/tasks/{j.starting_task_id}/execs/runner/connect"
        wsurl = f"{execs_url}/runners/connect"
        print("Creating WSConn to: ", wsurl)
        import websocket, ssl
        ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
        ws.connect(wsurl, header={"Authorization": f"Bearer {token}"})
        j.msgsender = WSSender(ws, j)
    results = j.run(JOB_ID, conv_id=conv_id, user_info=user_info, iter_id=int(iter_id))
    print("RunJob Results: ", results) 
    sys.stdout.flush()
    if ws: ws.close()
    return results

class MSGEcho:
    def __init__(self, runner):
        self.runner = runner
        self.msgindex = 0

    def send(self, cmd, **payload):
        payload["job_id"] = self.runner.job_id
        payload["curr_iter"] = self.runner.curr_iter
        payload["runbook_task_id"] = self.runner.runbook_task_id
        payload["starting_child_path"] = self.runner.starting_child_path
        payload["starting_task_id"] = self.runner.starting_task_id
        self.msgindex += 1
        msg = json.dumps({
            "msgid": self.msgindex,
            "type": "cmd",
            "cmd": cmd,
            "payload": payload
        }, indent=2)
        m = json.loads(msg)
        if m["cmd"] == "print":
            payload = m.get("payload", {})
            print(*payload.get("args", []), *payload.get("kwargs", {}))
        else:
            # print("Sending Message: ", datetime.datetime.utcnow().isoformat(), msg)
            pass
        sys.stdout.flush()

def subprocess_caller(cmdParams, interactive=False):
    import subprocess
    p = subprocess.run(cmdParams['cmd'],
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        shell=True
    )
    stdout_contents = p.stdout.decode('utf-8')
    stderr_contents = p.stderr.decode('utf-8')
    print(stdout_contents)
    print(stderr_contents)
    class MockResponse:
        def __init__(self, code, mocked_json):
            self.status_code = code
            self.mocked_json = mocked_json

        def json(self):
            return self.mocked_json

        @property
        def content(self):
            return bytes(json.dumps(self.mocked_json), "utf-8")
    # import ipdb ; ipdb.set_trace()
    return MockResponse(200, {"responsecode": "True", "msg": stdout_contents + stderr_contents})

def runJobLocally(job_class, conv_id=None, user_info=None, token=None, *args, **kwargs):
    global JOB_ID
    from daglib import daglib
    user_info = user_info or {}
    if type(user_info) is str:
        user_info = json.loads(user_info)
    dlb = daglib(None, user=user_info.get("uname"), jwt=token)
    j = job_class(dlb, None)
    j.msgsender = MSGEcho(j)
    results = j.run(JOB_ID, conv_id=conv_id, user_info=user_info, iter_id=0)
    print("Results: ", results) 
    sys.stdout.flush()
    return results


class job_EpNW2mm6qOjIq7ExrVXu(BaseJobRunner):
    def __init__(self, *args):
        super().__init__(*args)
        self.runbook_task_id = ''
        self.starting_child_path = ''
        self.starting_task_id = 'FuzNnhLQ8MIdNwtw2mED'
        self.starting_func_name = 'task_FuzNnhLQ8MIdNwtw2mED'
        self.starting_task_param_values = {}
        self.special_param_values = {}

    ### defs for each task goes here

    def task_FuzNnhLQ8MIdNwtw2mED(self, context):
        """ Check Elasticsearch Cluster Health
        <p>This script checks the health of an Elasticsearch cluster by making an HTTP GET request to the cluster's health endpoint. It uses basic authentication with a username and password to access the cluster. The script outputs the JSON response from the Elasticsearch cluster health API.</p>
        """
        self.debugprint("ENTERING task_FuzNnhLQ8MIdNwtw2mED....", context, context.vars)
        print = context.ctxprint
        # TODO - import other "magic" variables - eg _xyz
        def getParamValue(paramname):
            print("CV: ", context.vars)
            if paramname in context.vars:
                return typecasted(context.vars[paramname])
            out = PARAM_VALUES.get(paramname, "")
            if out: return out
            PARAM_VALUES[paramname] = input(f"Enter value for " + paramname + ": ").strip()
            return PARAM_VALUES[paramname]
        def getEnvVar(varname):
            return os.environ.get(varname)
    
        try:
        
            if 'elastic_url' in context.vars: elastic_url = typecasted(context.vars['elastic_url'], 'String')
            self.debugprint("SETTING INPUT PARAMS task_FuzNnhLQ8MIdNwtw2mED elastic_url = ", context.vars.get('elastic_url', None), "HasIt?: ", 'elastic_url' in context.vars)
            if 'elastic_user_name' in context.vars: elastic_user_name = typecasted(context.vars['elastic_user_name'], 'String')
            self.debugprint("SETTING INPUT PARAMS task_FuzNnhLQ8MIdNwtw2mED elastic_user_name = ", context.vars.get('elastic_user_name', None), "HasIt?: ", 'elastic_user_name' in context.vars)
            if 'elastic_password' in context.vars: elastic_password = typecasted(context.vars['elastic_password'], 'String')
            self.debugprint("SETTING INPUT PARAMS task_FuzNnhLQ8MIdNwtw2mED elastic_password = ", context.vars.get('elastic_password', None), "HasIt?: ", 'elastic_password' in context.vars)
            context.taskStarted(locals())
            import os
            import requests
            from requests.auth import HTTPBasicAuth
            PARAM_VALUES = {
                'elastic_url': getEnvVar('ELASTIC_URL'),
                'elastic_user_name': getEnvVar('ELASTIC_USER_NAME'),
                'elastic_password': getEnvVar('ELASTIC_PASSWORD')
            }
            elastic_url = getParamValue('elastic_url')
            elastic_user_name = getParamValue('elastic_user_name')
            elastic_password = getParamValue('elastic_password')
            url = f"{elastic_url}/_cluster/health"
            response = requests.get(url, auth=HTTPBasicAuth(elastic_user_name, elastic_password))
            print(response.json())
            if context.skip_sub_tasks: return context.taskFinished(True, locals(), [{'name': 'response', 'param_type': 'String', 'default_value': '', 'required': False}])
            return context.taskFinished(True, locals(), [{'name': 'response', 'param_type': 'String', 'default_value': '', 'required': False}])
            
        except Exception as e:
        
            return context.taskFailed(locals(), sys.exc_info())
            
ALLTASKS = {'FuzNnhLQ8MIdNwtw2mED': {'id': 'FuzNnhLQ8MIdNwtw2mED', 'conv_id': '', 'title': 'Check Elasticsearch Cluster Health', 'task_type': '', 'task_category': '', 'script_type': 'python', 'script': {'code': 'import os\nimport requests\nfrom requests.auth import HTTPBasicAuth\n\nPARAM_VALUES = {\n    \'elastic_url\': getEnvVar(\'ELASTIC_URL\'),\n    \'elastic_user_name\': getEnvVar(\'ELASTIC_USER_NAME\'),\n    \'elastic_password\': getEnvVar(\'ELASTIC_PASSWORD\')\n}\n\n\nelastic_url = getParamValue(\'elastic_url\')\nelastic_user_name = getParamValue(\'elastic_user_name\')\nelastic_password = getParamValue(\'elastic_password\')\n\nurl = f"{elastic_url}/_cluster/health"\nresponse = requests.get(url, auth=HTTPBasicAuth(elastic_user_name, elastic_password))\n\nprint(response.json())\n'}, 'description': "<p>This script checks the health of an Elasticsearch cluster by making an HTTP GET request to the cluster's health endpoint. It uses basic authentication with a username and password to access the cluster. The script outputs the JSON response from the Elasticsearch cluster health API.</p>", 'description_type': '', 'num_voters': 0, 'num_parents': 0, 'parent_tasks': [], 'extras': {}, 'tags': [], 'workspace_ids': [''], 'input_params': [{'name': 'elastic_url', 'param_type': 'String', 'default_value': '', 'required': False}, {'name': 'elastic_user_name', 'param_type': 'String', 'default_value': '', 'required': False}, {'name': 'elastic_password', 'param_type': 'String', 'default_value': '', 'required': False}], 'output_params': [{'name': 'response', 'param_type': 'String', 'default_value': '', 'required': False}], 'permissions': [], 'workspace_status': [], 'commands': [], 'created_at': 1720652741.847644, 'updated_at': 1720652741.851582, 'creator': '1', 'sub_tasks': [], 'source_info': {'source_url': '', 'source_name': '', 'source_id': '', 'source_version': '', 'last_synced_at': 1720652741.848286}, 'ref_task_ids': [], 'created_at_bucket': 28677545, 'metadata': {'last_vectorized': 1720652741.8516731, 'vec_version': 0, '_seq_no': 99, '_primary_term': 5}}}

JOB_ID = 'EpNW2mm6qOjIq7ExrVXu'


def echo_resp_sender(self, resp):
    print(f"[{resp['req']}]: ", resp['msg'])

job_class= eval(f"job_{JOB_ID}")
from daglib import daglib
user_info = {'uid': 666, "first_name": "User", "last_name": "None"}
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkYWdrbm93cy5jb20iLCJzdWIiOiJzcmlAZGFna25vd3MuY29tIiwibmJmIjoxNzE1Mjk0OTYyLCJleHAiOjE3NDY4MzExNDIsImp0aSI6ImY3MjdkcHNEMFplVnFVeFQiLCJhdWQiOiJkYWdrbm93cyIsInJvbGUiOiJzdXByZW1vIiwidXNlcl9jbGFpbXMiOnsidWlkIjoiMSIsInVuYW1lIjoic3JpQGRhZ2tub3dzLmNvbSIsIm9yZyI6IkRhZ0tub3dzIiwiZmlyc3RfbmFtZSI6IlNyaSIsImxhc3RfbmFtZSI6IlBhbnlhbSIsInJvbGUiOiJTdXByZW1vIiwiYWVzX2tleSI6IkxZbUFYaTR5MllEYWVmLUMvVDJ4bitzWVRPc2F5aG85Iiwib2ZzdCI6WzQzOCwxMjYsMjA3LDE2MSwyNDAsMjUwLDE3MCwyNjcsMTQ1LDE0OCwzMzksMTY2LDMzMiwyNjgsNDI2LDE4NiwxMTEsOTgsMjcwLDMzNiwzODMsMzE3LDg4LDE4OCwxODIsMTQyLDE2NSwxNjYsMTc2LDE4OSwxODMsMjAzXX19.vHuNd5l4zGfbnqBwxZ_apXvVcEqces-LLFAWYUEcE9utv5LJkBW_L0uPMWHYCB0oBD2tMfbGeTaWgCmIrb2Nhe7uHsu_8tEuR9lxAiblq6zRBeUJ-xd3CExswCNPWMNQCasskqWRcv7uo3OJClx8IG9DdNs7h6augOU6RLXjHkyg6xj-47eDzvYHqVJRmlbSbK3-olDainxMt6Vqn2QTa0DjtsKVswVw3S5HdyBbuynIw1bvb_xCMbq4ph3SXy_8USvcpdXdv8e0JVOkzTGRYiM6TUOQsuISH41wjkAN6zf7wSuLsjyLctPugdykL4QcP9luIH6TkIZ9yy7vtAoChQ"
dlb = daglib(None, user=None, jwt=token)
dlb.command_caller = subprocess_caller
j = job_class(dlb, None)
j.starting_task_param_values = {}
j.msgsender = MSGEcho(j)
j.command_caller = subprocess_caller
j.resp_sender = echo_resp_sender
j.run(JOB_ID, conv_id="", user_info=user_info, iter_id=0)
