from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from models import Caseresult
import json

def case_result(request, scheduleId, caseId):
    case_result_list = Caseresult.objects.filter(schedule_id = scheduleId, case_id = caseId).order_by("-updated_at")
    for i in range(len(case_result_list)):
        case_result_list[i].log_info = case_result_list[i].log_info.replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&nbsp;").replace("\r\n", "<br>").replace("\n", "<br>")
    return render_to_response("case_result.html", locals())
    
