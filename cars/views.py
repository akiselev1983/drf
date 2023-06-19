from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import CarModel
from .serializers import CarSerializer, CarAllSerializer

class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarAllSerializer(cars, many=True)
        return Response(serializer.data, status=200)
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializer(car)
        return Response(serializer.data, status=200)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarSerializer(car, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()
        return Response(status=204)