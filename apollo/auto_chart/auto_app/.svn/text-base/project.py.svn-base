# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Members
from models import Project
from models import Platform
from models import Product
from django.utils import timezone
from datetime import datetime
import time
import json

def project(request, platform, product):
    #print request.POST.items()
    add_err = False
    add_err_msg = ""
    member_list = Members.objects.order_by("name")
    plt_name = Platform.objects.filter(id = int(platform))[0].name
    pd_name = Product.objects.filter(id = int(product))[0].name
    if request.method == "POST":
        if request.POST.get("sub") == "Add":
            add_err, add_err_msg, arg_dict = add_arg_check(request.POST.items())
            if add_err:
                return render_to_response("project.html", locals(), context_instance = RequestContext(request))
            else:
                project_name = "%s %s.%s.%s.%s%s" % (arg_dict["project_name"], arg_dict["fir"], arg_dict["sec"], arg_dict["thir"], arg_dict["four"], arg_dict["patch"].replace("null", ""))
                new_project = Project(project_name = project_name, member_id = int(arg_dict["owner"]), platform_id = int(platform),
                                      product_id = int(product), total_case = int(arg_dict["total_case"]),
                                      new_case = int(arg_dict["new_case"]), total_auto_case = int(arg_dict["total_auto"]), new_auto_case = int(arg_dict["new_auto"]),
                                      finished_auto_case = int(arg_dict["finished"]), develop_time = arg_dict["time"], total_bugs = int(arg_dict["total_bug"]),
                                      auto_bugs = int(arg_dict["auto_bug"]), updated_at = datetime.now(), created_at = datetime.now())
                new_project.save()
                product_obj = Product.objects.filter(id = int(product), platform_id = int(platform))
                platform_obj = Platform.objects.filter(id = int(platform))
                
                if 0 != len(product_obj):
                    product_obj[0].status = "deving"
                    product_obj[0].total_case += int(arg_dict["new_case"])
                    product_obj[0].total_auto_case += int(arg_dict["new_auto"])
                    product_obj[0].finished_auto_case += int(arg_dict["finished"])
                    product_obj[0].develop_time = str(float(product_obj[0].develop_time) + float(arg_dict["time"]))
                    product_obj[0].total_bugs += int(arg_dict["total_bug"])
                    product_obj[0].auto_bugs += int(arg_dict["auto_bug"])
                    product_obj[0].save()
                    
                if 0 != len(platform_obj):
                    platform_obj[0].total_case += int(arg_dict["new_case"])
                    platform_obj[0].total_auto_case += int(arg_dict["new_auto"])
                    platform_obj[0].finished_auto_case += int(arg_dict["finished"])
                    platform_obj[0].develop_time = str(float(platform_obj[0].develop_time) + float(arg_dict["time"]))
                    platform_obj[0].total_bugs += int(arg_dict["total_bug"])
                    platform_obj[0].auto_bugs += int(arg_dict["auto_bug"])
                    platform_obj[0].save()                    
                    
                    
        elif request.POST.get("sub") == "Delete":
            delete_pj = Project.objects.filter(id = int(request.POST.get("pjid")))
            if len(delete_pj) != 0:
                product_obj = Product.objects.filter(id = int(product), platform_id = int(platform))
                platform_obj = Platform.objects.filter(id = int(platform))
                if 0 != len(product_obj):
                    product_obj[0].total_case -= delete_pj[0].new_case
                    product_obj[0].total_auto_case -= delete_pj[0].new_auto_case
                    product_obj[0].finished_auto_case -= delete_pj[0].finished_auto_case
                    product_obj[0].develop_time = str(float(product_obj[0].develop_time) - float(delete_pj[0].develop_time))
                    product_obj[0].total_bugs -= delete_pj[0].total_bugs
                    product_obj[0].auto_bugs -= delete_pj[0].auto_bugs
                    product_obj[0].save()
                                    
                if 0 != len(platform_obj):
                    platform_obj[0].total_case -= delete_pj[0].new_case
                    platform_obj[0].total_auto_case -= delete_pj[0].new_auto_case
                    platform_obj[0].finished_auto_case -= delete_pj[0].finished_auto_case
                    platform_obj[0].develop_time = str(float(platform_obj[0].develop_time) - float(delete_pj[0].develop_time))
                    platform_obj[0].total_bugs -= delete_pj[0].total_bugs
                    platform_obj[0].auto_bugs -= delete_pj[0].auto_bugs
                    platform_obj[0].save()                
                delete_pj[0].delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    elif request.method == "GET":
        project_list = Project.objects.order_by("-created_at").filter(platform_id = int(platform), product_id = int(product))
        for project in project_list:
            for member in member_list:
                if project.member_id == member.id:
                    project.member_id = member.name
        return render_to_response("project.html", locals(), context_instance = RequestContext(request))



def add_arg_check(arg_list):
    err = False
    err_msg = ""
    arg_dict = {}
    for k,v in arg_list:
        try:
            if k in ["project_name", "owner"]:
                if v == "":
                    raise Exception("请输入%s" % str(k).replace("_", " "))
                else:
                    arg_dict[k] = v
            elif k in ["fir", "sec", "thir", "four"]:
                if v == "":
                    raise Exception("请输入完整版本号")
                else:
                    try:
                        int(v)
                        arg_dict[k] = v
                    except ValueError,ex:
                        raise Exception("版本号请输入数字")
            elif k in ["total_case", "new_case", "total_auto", "new_auto", "finished", "time", "total_bug", "auto_bug"]:
                if v == "":
                    raise Exception("请输入%s" % str(k).replace("_", " "))
                else:
                    try:
                        float(v)
                        arg_dict[k] = v
                    except ValueError,ex:
                        raise Exception("%s请输入数字" % str(k).replace("_", " "))
            else:
                arg_dict[k] = v
        except Exception,ex:
            err = True
            err_msg = ex
            arg_dict = {}
    return err, err_msg, arg_dict
    