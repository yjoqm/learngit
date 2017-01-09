from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render_to_response
from models import Testcase
from django.utils import timezone
from datetime import datetime
import time
import json

def case_delete(request, *args):
    case_id = args[0]
    echo = {}
    if request.method == "DELETE":
        try:
            test_cases = Testcase.objects.filter(case_id = case_id)
            if len(test_cases) == 0:
                echo["code"] = "400"
                echo["msg"] = "%s does not exist" % case_id
                return HttpResponseBadRequest(json.dumps(echo))
            
            for case in test_cases:
                case.delete()
                
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

