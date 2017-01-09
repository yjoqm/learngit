# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Members
from models import Project
from models import Product
from django.utils import timezone
from datetime import datetime
import time
import json

def roadmap(request):
    print request.POST.items()
    add_err = False
    err_msg = ""
    
    
    if request.method == "POST":
        for k, v in request.POST.items():
            if k.startswith("addplt"):
                plt_id = int(k[6:])
                product_name = v
                added_products = Product.objects.filter(platform_id = plt_id, name = product_name)
                if 0 != len(added_products):
                    add_err = True
                    err_msg = product_name
                    return render_to_response("roadmap.html", locals(), context_instance = RequestContext(request))
                else:
                    new_product = Product(name = v, platform_id = plt_id, status = "new", total_case = 0,
                                          total_auto_case = 0, finished_auto_case = 0, develop_time = "0", 
                                          total_bugs = 0, auto_bugs = 0, created_at = datetime.now())
                    new_product.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        pass
    elif request.method == "GET":
        products_id1 = Product.objects.order_by("name").filter(platform_id = 1)
        row_array_id1 = get_array(products_id1)
        products_id2 = Product.objects.order_by("name").filter(platform_id = 2)
        row_array_id2 = get_array(products_id2)        
        return render_to_response("roadmap.html", locals(), context_instance = RequestContext(request))


def get_array(query_obj):
    col_num = 3
    pruduct_list = []
    for product in query_obj:
        pruduct_list.append(product)
    pruduct_list.append("")
    row_num = len(pruduct_list) / col_num + int((len(pruduct_list) % col_num) ** 0.01)
    row_array = []
    for i in range(row_num):
        row_array.append(pruduct_list[i * 3:i * 3 + 3])
    for i in range(col_num - len(row_array[-1])):
        row_array[-1].append("extra")
    return row_array