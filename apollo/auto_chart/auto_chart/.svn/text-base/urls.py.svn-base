from django.conf.urls import patterns, include, url
from auto_app.project import project
from auto_app.roadmap import roadmap
from django.conf import settings
from django.conf.urls.static import static

#from auto_app.schedule_list import schedule_list
#from auto_app.schedule_add import schedule_add
#from auto_app.case_add import case_add
#from auto_app.case_delete import case_delete
#from auto_app.schedule_result import schedule_result
#from auto_app.case_result import case_result
#from index import index


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
    #(r'^$', index),
    #(r'^auto/$', index),
    (r'^roadmap/$', roadmap),
    (r'^project/([a-zA-z0-9_]+)/([a-zA-z0-9_]+)/$', project)
)


#from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
#urlpatterns += staticfiles_urlpatterns()
