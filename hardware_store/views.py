import django_filters
from django.db.models import Max
from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets, generics
from hardware_store.serializers import ConsignmentSerializer, GoodsSerializer, ProducerSerializer, DepartmentSerializer, \
    SalesLogSerializer, OrdersSerializer, OrderitemsSerializer, FilterMaxSerializer
from hardware_store.models import Consignment, Goods, Producer, Department, SalesLog, Orders, Orderitems,  \
    GoodsFilter


class ConsignmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать поставки
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Consignment.objects.all().order_by('date_consignment')
    serializer_class = ConsignmentSerializer  # Сериализатор для модели

class GoodsViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать поставки
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Goods.objects.all().order_by('id_good')
    serializer_class = GoodsSerializer  # Сериализатор для модели

class ProducerViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать поставки
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Producer.objects.all().order_by('id_producer')
    serializer_class = ProducerSerializer  # Сериализатор для модели

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать поставки
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Department.objects.all().order_by('id_department')
    serializer_class = DepartmentSerializer  # Сериализатор для модели

class SalesLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать поставки
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = SalesLog.objects.all().order_by('id_log')
    serializer_class = SalesLogSerializer  # Сериализатор для модели
class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать поставки
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Orders.objects.all().order_by('id_order')
    serializer_class = OrdersSerializer  # Сериализатор для модели
class OrdersItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать поставки
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Orderitems.objects.all().order_by('id_orderitem')
    serializer_class = OrderitemsSerializer  # Сериализатор для модели

class GoodsSearchViewSet(generics.ListCreateAPIView):
    search_fields = ['name_good']
    ordering_fields = ['price']
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, )
    filterset_class = GoodsFilter
    queryset = Goods.objects.all()
    name = 'Medicine'
    serializer_class = GoodsSerializer




