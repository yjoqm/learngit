from django.conf.urls import patterns, include, url
from ci_app.schedule_list import schedule_list
from ci_app.schedule_add import schedule_add
from ci_app.case_add import case_add
from ci_app.case_delete import case_delete
from ci_app.schedule_result import schedule_result
from ci_app.case_result import case_result
from index import index


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ci_platform.views.home', name='home'),
    # url(r'^ci_platform/', include('ci_platform.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', index),
    (r'^apollo/schedule/$', schedule_list),
    (r'^apollo/schedule/add/$', schedule_add),
    (r'^apollo/case/add/$', case_add),
    (r'^apollo/case/([a-zA-z0-9_]+)/delete/$', case_delete),
    (r'^apollo/schedule/(\d+)/$', schedule_result),
    (r'^apollo/schedule/(\d+)/case/([a-zA-z0-9_]+)/$', case_result)    
)
