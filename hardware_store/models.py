from django.db import models
from rest_framework import filters
from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Consignment(models.Model):
    id_consignment = models.AutoField(primary_key=True)
    date_consignment = models.DateField(blank=True, null=True)
    amount = models.CharField(max_length=30, blank=True, null=True)
    purchase_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consignment'


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    name_department = models.CharField(max_length=30, blank=True, null=True)
    employee = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Goods(models.Model):
    id_good = models.AutoField(primary_key=True)
    id_producer = models.ForeignKey('Producer', models.DO_NOTHING, db_column='id_producer', blank=True, null=True)
    id_consignment = models.ForeignKey('Consignment', models.DO_NOTHING, db_column='id_consignment', blank=True, null=True)
    id_department = models.ForeignKey('Department', models.DO_NOTHING, db_column='id_department', blank=True, null=True)
    name_good = models.CharField(max_length=30)
    price = models.IntegerField()
    amount = models.CharField(max_length=30, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'



class Producer(models.Model):
    id_producer = models.AutoField(primary_key=True)
    name_producer = models.CharField(max_length=30)
    contry_produser = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producer'


class SalesLog(models.Model):
    id_log = models.AutoField(primary_key=True)
    id_good = models.ForeignKey(Goods, models.DO_NOTHING, db_column='id_good')
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer')
    amount = models.IntegerField()
    date_log = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_log'

class Orders(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer', blank=True, null=True)
    date_order = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'

class Orderitems(models.Model):
    id_orderitem = models.AutoField(db_column='id_orderItem', primary_key=True)  # Field name made lowercase.
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='id_order')
    id_good = models.ForeignKey(Goods, models.DO_NOTHING, db_column='id_good')
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderitems'

class GoodsFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Goods
        fields = [
            'min_price',
            'max_price'
        ]





