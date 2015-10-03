# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Events(models.Model):
    eveid = models.IntegerField(db_column='eveId', primary_key=True)  # Field name made lowercase.
    evename = models.CharField(db_column='eveName', max_length=35, blank=True, null=True)  # Field name made lowercase.
    fee = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Events'


class Groupregistration(models.Model):
    grpid = models.IntegerField(db_column='grpId', blank=True, null=True)  # Field name made lowercase.
    eveid = models.ForeignKey(Events, db_column='eveId', blank=True, null=True)  # Field name made lowercase.
    pids = models.CharField(db_column='pIds', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupRegistration'


class Grpids(models.Model):
    grpid = models.IntegerField(db_column='grpId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grpids'


class Logintable(models.Model):
    pid = models.ForeignKey('People', db_column='pId', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=40, blank=True, null=True)
    csrftoken = models.CharField(db_column='csrfToken', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoginTable'


class People(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    pid = models.IntegerField(db_column='pId', primary_key=True)  # Field name made lowercase.
    college = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    mobile = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    feepaid = models.IntegerField(db_column='feePaid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'People'
    def __str__(self):
        return self.name+" "+str( self.pid )


class Pids(models.Model):
    pid = models.IntegerField(db_column='pId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pids'


class Registration(models.Model):
    eveid = models.ForeignKey(Events, db_column='eveId', blank=True, null=True)  # Field name made lowercase.
    pid = models.ForeignKey(People, db_column='pId', blank=True, null=True)  # Field name made lowercase.
    grpid = models.IntegerField(db_column='grpId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Registration'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
