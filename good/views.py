from django.http import HttpResponse
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from good.models import Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'


class GoodViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def list(self, request):
        queryset = Good.objects.all()
        serializer = GoodSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create(self, request):
        serializer = GoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=201)

    @action(detail=True, methods=['get'])
    def retrieve(self, request, pk):
        try:
            queryset = Good.objects.get(pk=pk)
        except Good.DoesNotExist:
            return HttpResponse(status=404)
        serializer = GoodSerializer(queryset)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def destroy(self, request, pk):
        try:
            queryset = Good.objects.get(pk=pk)
        except Good.DoesNotExist:
            return HttpResponse(status=404)
        queryset.remove()
        return HttpResponse(status=200)

