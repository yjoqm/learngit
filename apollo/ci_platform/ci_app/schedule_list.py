from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from models import Schedule

def schedule_list(request):
    search_err = False
    page_size = 20
    page = 1
    total_page = 0
    page_name = {}
    page_list = []
    filter_list = []
    filter_name = {}
    first_disable = False
    last_disable = False
    if "page" in request.GET:
        page = request.GET.get("page")
        try:
            page = int(page)
            if page <= 0:
                raise ValueError("page err")
        except ValueError,ex:
            raise Http404()
        
    schedule_list = Schedule.objects.order_by("-updated_at")
        
    if "module_name" in request.GET:
        module_name = request.GET.get("module_name")
        if not module_name:
            search_err = True
            schedule_list = [] #Schedule.objects.order_by("-updated_at").filter(module_name = "")[0:20]
            total_page = 0
        else:
            schedule_list = schedule_list.filter(module_name = module_name)
            filter_name = {}
            filter_name["name"] = "module_name"
            filter_name["value"] = module_name
            filter_list.append(filter_name)
            
    total_page = len(schedule_list) / page_size + int((len(schedule_list) % page_size) ** 0.01)
    
    if page == 1:
        first_disable = True
    if page == total_page:
        last_disable = True
    last_page = page - 1
    next_page = page + 1
    
    if total_page <= 5:
        range_num = total_page
        first_value = 1
    else:
        range_num = 5
        left_end = page - 1
        right_end = total_page - left_end - 1
        if left_end <= 2:
            first_value = 1
        elif right_end <= 2:
            first_value = page - 4 + right_end
        else:
            first_value = page - 2
    for i in range(range_num):
        page_name = {}
        page_name["value"] = first_value + i
        if page == page_name["value"]:
            page_name["disable"] = True
        else:
            page_name["disable"] = False
        page_list.append(page_name)
    
    schedule_list = schedule_list[(page - 1) * page_size : page * page_size]
    
    blank_nu = 20 - len(schedule_list)
    
    for i in range(blank_nu):
        schedule_list.append("")
        
    print schedule_list

    return render_to_response("schedule_list.html", locals())
