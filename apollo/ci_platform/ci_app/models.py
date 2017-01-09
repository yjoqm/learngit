# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Caseresult(models.Model):
    #id = models.IntegerField(primary_key=True)
    case_id = models.CharField(max_length=255L, blank=True)
    schedule_id = models.CharField(max_length=255L, blank=True)
    result = models.CharField(max_length=10L)
    log_info = models.TextField(blank=True)
    duration = models.CharField(max_length=255L, blank=True)
    started_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'caseResult'

class Schedule(models.Model):
    #id = models.IntegerField(primary_key=True)
    module_name = models.CharField(max_length=255L, blank=True)
    status = models.CharField(max_length=8L)
    current_case = models.CharField(max_length=255L, blank=True)
    case_plan = models.TextField(blank=True)
    result = models.TextField(blank=True)
    duration = models.CharField(max_length=255L, blank=True)
    started_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'schedule'

class Testcase(models.Model):
    #id = models.IntegerField(primary_key=True)
    case_id = models.CharField(max_length=255L, unique=True, blank=True)
    module_name = models.CharField(max_length=255L, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'testCase'

