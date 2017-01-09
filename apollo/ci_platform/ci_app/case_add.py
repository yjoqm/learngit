from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render_to_response
from models import Testcase
from django.utils import timezone
from datetime import datetime
import time
import json

def case_add(request):
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
            case = Testcase(module_name = params.get("module_name"), case_id = params.get("case_id"), created_at = datetime.now())
            case.save()
            echo["code"] = 200
            echo["msg"] = "Successful"
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
    if params.has_key("case_id") and params.has_key("module_name"):
        if Testcase.objects.filter(case_id = params.get("case_id")):
            echo["code"] = "400"
            echo["msg"] = "%s has exist" % str(params.get("case_id"))
            return False
        else:
            return True
    else:
        echo["code"] = "400"
        echo["msg"] = "Params error"
        return False


