#!/usr/bin/python

import sys
import os
import time
from datetime import datetime
import json


#add user libsa
user_module_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert (0, user_module_path + "/../")
os.environ['DJANGO_SETTINGS_MODULE'] = 'ci_platform.settings'
from ci_platform import settings
from ci_app.models import *

from run_cmd import RunCmd






class ScheduleExe:
    def __init__(self):
        self.case_script_path = settings.SCRIPT_PATH
        self.pid = os.getpid()
        pass

    def get_one_schedule(self):
        ret = {}
        schedule_list = Schedule.objects.filter(status = "new").order_by("id")[:1]
        if schedule_list:
            ret[str(schedule_list[0].id)] = json.loads(schedule_list[0].case_plan)
            return ret
        else:
            return {}


    def schedule_result_update(self, schedule_id, status, **params):
        if params.has_key("msg"):
            msg = params.get("msg")
        else:
            msg = ""

        if params.has_key("current_case"):
             current_case = params.get("current_case")
        else:
            current_case = ""

        duration = time.time() - self.schedule_start
        
        schedules = Schedule.objects.filter(id = schedule_id)
        if schedules:
            schedule = schedules[0]
            
        schedule.result = "%s" % msg
        schedule.status = "%s" % status
        schedule.duration = "%.3f" % duration
        schedule.current_case = current_case
        schedule.updated_at = datetime.now()
        schedule.started_at = self.schedule_started_at
        schedule.save()
        


    def get_module(self, case_id):
        query_result = Testcase.objects.filter(case_id = case_id)
        return query_result


    def set_case_result(self, case_id, schedule_id, result, log_file = None):
        duration = time.time() - self.case_start
        case_result = Caseresult(case_id = case_id, schedule_id = str(schedule_id), result = result,
                                 log_info = "", duration = "%.3f" % duration, started_at = self.case_started_at, 
                                 created_at = datetime.now(), updated_at = datetime.now())
        case_result.save()
        if result == "noExe":
            case_result.log_info = case_result.log_info + 'Case is not registered or script file does not exist'
        elif result == "killed":
            case_result.log_info = case_result.log_info + 'Case timeout\r\n'
            case_result.result = "failed"
            if os.path.exists(log_file):
                case_result.log_info = case_result.log_info + open(log_file, "r").read()
        elif result == "bad":
            case_result.log_info = case_result.log_info + "Can't catch result 'case_name succeed' or 'case_name false' or can't find logfile\r\n"
            if os.path.exists(log_file):
                case_result.log_info = case_result.log_info + open(log_file, "r").read()
        else:
            if os.path.exists(log_file):
                case_result.log_info = case_result.log_info + open(log_file, "r").read()
            else:
                case_result.log_info = case_result.log_info + "Can't find logfile maybe there is something wrong with this script."
                case_result.result = "bad"
        case_result.save()
        
    def get_exe_list(self, content):
        exe_list = []
        for case_id in content.keys():
            if content.get(case_id) == "true":
                exe_list.append(case_id)
        return exe_list

    def case_exe(self, schedule_id, content):
        self.schedule_started_at = datetime.now()
        self.schedule_start = time.time()
        exe_list = self.get_exe_list(content)
        case_total = len(exe_list)
        case_pass = 0
        case_pass_list = []
        case_fail = 0
        case_fail_list = []
        case_miss = 0
        case_miss_list = []
        case_bad  = 0
        case_bad_list  = []
        case_exed = 0


        for case_id in exe_list:
            case_name = case_id
            now_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
            log_file = str("/tmp/%s_%s_%s" % (now_time, self.pid, case_name))
            query_result = self.get_module(case_id)

            msg = {}
            msg["exed"] = "%s" % case_exed
            msg["total"] = "%s" % case_total
            msg["successful"] = "%s" % case_pass
            msg["failed"] = "%s" % case_fail
            msg["noExe"] = "%s" % case_miss
            msg["bad"] = "%s" % case_bad
            msg["suc_list"] = case_pass_list
            msg["fail_list"] = case_fail_list
            msg["noExe_list"] = case_miss_list
            msg["bad_list"] = case_bad_list

            msg = json.dumps(msg)
            self.schedule_result_update(schedule_id, "testing", msg = msg, current_case = case_name)
            
            case_result = "noExe"
            self.case_started_at = datetime.now()
            self.case_start = time.time()
            if query_result == []:
                print "*" * 100
                print "case " + case_name + " is running (%s/%s)..." % (case_exed + 1, case_total)
                print "cannot found " + case_name
                print "case " + case_name + " end..."
                case_exed += 1
                case_result = "noExe"
                case_miss += 1
                case_miss_list.append(case_name)
            else:
                module = query_result[0].module_name
                case_path = self.case_script_path % module
                if os.path.exists(case_path + case_name + ".py"):
                    cmd = ("python", case_path + case_name + ".py", log_file)
                    print "*" * 100
                    print "case " + case_name + " is running (%s/%s)..." % (case_exed + 1, case_total)
                    process = RunCmd(" ".join(cmd), 300)
                    return_code = process.run()
                    #item = run_cmd(" ".join(cmd))
                    print "case " + case_name + " end..."
                    case_exed += 1
                    if return_code != -9:
                        if -1 != process.stdout.find("%s false" % case_name) and os.path.exists(log_file):
                            case_result = 'failed'
                            case_fail += 1
                            case_fail_list.append(case_name)
                            print "case " + case_name + " fail..."
                        elif -1 != process.stdout.find("%s succeed" % case_name) and os.path.exists(log_file):
                            case_result = "successful"
                            case_pass += 1
                            case_pass_list.append(case_name)
                            print "case " + case_name + " succeed..."
                        else:
                            case_result = 'bad'
                            case_bad += 1
                            case_bad_list.append(case_name)
                            print "case " + case_name + " bad..."
                    else:
                        case_result = "killed"
                        case_fail += 1
                        case_fail_list.append(case_name)
                        print "case " + case_name + " killed..."

                else:
                    case_result = "noExe"
                    case_exed += 1
                    case_miss += 1
                    case_miss_list.append(case_name)
            
            self.set_case_result(case_id, schedule_id, case_result, log_file)
            if log_file is not None:
                if os.path.exists(log_file):
                    os.remove(log_file)

        msg = {}
        msg["exed"] = "%s" % case_exed
        msg["total"] = "%s" % case_total
        msg["successful"] = "%s" % case_pass
        msg["failed"] = "%s" % case_fail
        msg["noExe"] = "%s" % case_miss
        msg["bad"] = "%s" % case_bad
        msg["suc_list"] = case_pass_list
        msg["fail_list"] = case_fail_list
        msg["noExe_list"] = case_miss_list
        msg["bad_list"] = case_bad_list

        msg = json.dumps(msg)
        print "*" * 100
        self.schedule_result_update(schedule_id, "finished", msg = msg)
        
        
    

def main ():
    schedule_exe = ScheduleExe()
    """
    schedule_list = schedule_exe.get_schedule()
    schedule_id_list = schedule_list.keys()
    schedule_id_list.sort()
    for i in schedule_id_list:
        print datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + " ************************ schedule %s begin ************************" % i
        schedule_exe.case_exe(i, schedule_list[i])
        print datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + " ************************ schedule %s end ************************" % i
        time.sleep(3)
    print datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + " all schedules is finished !!"
    """

    while True:
        schedule = schedule_exe.get_one_schedule()
        if schedule == {}:
            break
        else:
            schedule_id = schedule.keys()[0]
            print datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + " ************************ schedule %s begin ************************" % schedule_id
            schedule_exe.case_exe(schedule_id, schedule[schedule_id])
            print datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + " ************************ schedule %s end ************************" % schedule_id
    print datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + " all schedules is finished !!"




if __name__ == '__main__':
    main ()
