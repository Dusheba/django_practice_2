from rest_framework import serializers, viewsets

from djangoTask.helpers import ERROR, SuccessfulResponse
from v1.apps.v1_goods.models import Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'


class GoodViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Good.objects.all()
        serializer = GoodSerializer(queryset, many=True)
        return SuccessfulResponse(serializer.data)

    def create(self, request):
        serializer = GoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessfulResponse()

    def retrieve(self, request, pk):
        try:
            queryset = Good.objects.get(pk=pk)
        except Good.DoesNotExist:
            return ERROR.GOOD_DOES_NOT_EXIST
        serializer = GoodSerializer(queryset)
        return SuccessfulResponse(serializer.data)

    def destroy(self, request, pk):
        try:
            queryset = Good.objects.get(pk=pk)
        except Good.DoesNotExist:
            return ERROR.GOOD_DOES_NOT_EXIST
        queryset.remove()
        return SuccessfulResponse()
