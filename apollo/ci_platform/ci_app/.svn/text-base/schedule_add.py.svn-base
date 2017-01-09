from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render_to_response
from models import Schedule
from django.utils import timezone
from datetime import datetime
import time
import json

def schedule_add(request):
    echo = {}
    if request.method == "POST":
        try:
            try:
                params = json.loads(request.body)
            except Exception,ex:
                echo["code"] = "400"
                echo["msg"] = "Params is not JSON format"
                return HttpResponseBadRequest(json.dumps(echo))
            
            if not params_check(params, echo):
                return HttpResponseBadRequest(json.dumps(echo))
            
            schedule = Schedule(module_name = params.get("module_name"), status = "new", case_plan = json.dumps(params.get("case_plan")), 
                                created_at = datetime.now(), started_at = datetime.now())
            schedule.save()
            echo["code"] = 200
            echo["msg"] = {"schedule_id" : schedule.id}
            return HttpResponse(json.dumps(echo))
        except Exception, ex:
            echo["code"] = 500
            echo['msg'] = str(ex)
            return HttpResponseServerError(json.dumps(echo))
    else:
        echo["code"] = "400"
        echo["msg"] = "Method not allowed"
        return HttpResponseBadRequest(json.dumps(echo))

def params_check(params, echo):
    if params.has_key("module_name") and params.has_key("case_plan"):
        return True
    else:
        echo["code"] = "400"
        echo["msg"] = "Params error"         
        return False