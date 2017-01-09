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

class Members(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L, unique=True, blank=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'members'

class Platform(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L, unique=True, blank=True)
    total_case = models.IntegerField(null=True, blank=True)
    total_auto_case = models.IntegerField(null=True, blank=True)
    finished_auto_case = models.IntegerField(null=True, blank=True)
    develop_time = models.CharField(max_length=255L, blank=True)
    total_bugs = models.IntegerField(null=True, blank=True)
    auto_bugs = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'platform'

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L, unique=True, blank=True)
    platform_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=6L)
    total_case = models.IntegerField(null=True, blank=True)
    total_auto_case = models.IntegerField(null=True, blank=True)
    finished_auto_case = models.IntegerField(null=True, blank=True)
    develop_time = models.CharField(max_length=255L, blank=True)
    total_bugs = models.IntegerField(null=True, blank=True)
    auto_bugs = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'product'

class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=255L, unique=True, blank=True)
    member_id = models.IntegerField(null=True, blank=True)
    platform_id = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    total_case = models.IntegerField(null=True, blank=True)
    new_case = models.IntegerField(null=True, blank=True)
    total_auto_case = models.IntegerField(null=True, blank=True)
    new_auto_case = models.IntegerField(null=True, blank=True)
    finished_auto_case = models.IntegerField(null=True, blank=True)
    develop_time = models.CharField(max_length=255L, blank=True)
    total_bugs = models.IntegerField(null=True, blank=True)
    auto_bugs = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'project'

