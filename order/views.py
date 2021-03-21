from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderList(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderCreate(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=201)


class OrderRetrieve(APIView):
    def get(self, request, pk):
        try:
            queryset = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return HttpResponse(status=404)
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)


class OrderDestroy(APIView):
    def delete(self, request, pk):
        try:
            queryset = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return HttpResponse(status=404)
        queryset.remove()
        return HttpResponse(status=200)
