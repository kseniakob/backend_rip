from hardware_store.models import Consignment, Department, SalesLog
from hardware_store.models import Goods
from hardware_store.models import Producer
from hardware_store.models import Orders
from hardware_store.models import Orderitems
from rest_framework import serializers


class ConsignmentSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Consignment
        # Поля, которые мы сериализуем
        fields = ["id_consignment", "date_consignment", "amount", "purchase_price"]

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Goods
        # Поля, которые мы сериализуем
        fields = ["id_good", "id_producer", "id_consignment", "id_department", "name_good", "price", "amount", "image"]

class FilterMaxSerializer(serializers.ModelSerializer):
    price__max = serializers.IntegerField
    class Meta:
        fields = ["price__max"]

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Producer
        # Поля, которые мы сериализуем
        fields = ["id_producer", "name_producer", "contry_produser"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Department
        # Поля, которые мы сериализуем
        fields = ["id_department", "name_department", "employee"]

class SalesLogSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = SalesLog
        # Поля, которые мы сериализуем
        fields = ["id_log", "id_good", "id_customer", "amount", "date_log"]

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Orders
        # Поля, которые мы сериализуем
        fields = ["id_order", "id_customer", "date_order"]

class OrderitemsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Orderitems
        # Поля, которые мы сериализуем
        fields = ["id_orderitem", "id_order", "id_good", "amount"]
