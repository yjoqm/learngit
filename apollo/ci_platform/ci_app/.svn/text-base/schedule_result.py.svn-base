from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from models import Schedule
import json

def schedule_result(request, schedule_id):
    schedule_result = Schedule.objects.filter(id=schedule_id)
    if 0 == len(schedule_result):
        raise Http404()
    schedule_status = schedule_result[0].status
    current_case = schedule_result[0].current_case
    if schedule_status == "new":
        case_plan = json.loads(schedule_result[0].case_plan).values()
        case_num = 0
        for i in range(len(case_plan)):
            if case_plan[i] == "true":
                case_num += 1
        exe_num = 0
        suc_num = 0
        fail_num = 0
        noExe_num = 0
        bad_num = 0
        fail_list = []
        suc_list = []
        noExe_list = []
        bad_list = []
    else:
        case_num = json.loads(schedule_result[0].result).get("total")
        exe_num = json.loads(schedule_result[0].result).get("exed")
        suc_num = json.loads(schedule_result[0].result).get("successful")
        fail_num = json.loads(schedule_result[0].result).get("failed")
        noExe_num = json.loads(schedule_result[0].result).get("noExe")
        bad_num = json.loads(schedule_result[0].result).get("bad")
        fail_list = json.loads(schedule_result[0].result).get("fail_list")
        suc_list = json.loads(schedule_result[0].result).get("suc_list")
        noExe_list = json.loads(schedule_result[0].result).get("noExe_list")
        bad_list = json.loads(schedule_result[0].result).get("bad_list")
        duration = schedule_result[0].duration
        started_at = schedule_result[0].started_at
    return render_to_response("schedule_result.html", locals())
    
    #return HttpResponse(html)
