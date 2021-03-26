from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoTask.helpers import SuccessfulResponse, ERROR
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListCreateAPIView(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return SuccessfulResponse(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessfulResponse(serializer.data)


class OrderRetrieveDestroyAPIView(APIView):
    def get(self, request, pk):
        try:
            queryset = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return ERROR.ORDER_DOES_NOT_EXIST
        serializer = OrderSerializer(queryset)
        return SuccessfulResponse(serializer.data)

    def delete(self, request, pk):
        try:
            queryset = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return ERROR.ORDER_DOES_NOT_EXIST
        queryset.delete()
        return SuccessfulResponse()

