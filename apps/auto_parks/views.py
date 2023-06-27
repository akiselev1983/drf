from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import AutoParkModel
from .serializers import AutoParkSerializer
from rest_framework.response import Response
from apps.cars.serializers import CarSerializer
from django.http import Http404
from apps.cars.models import CarModel
from rest_framework.mixins import ListModelMixin, CreateModelMixin
class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

    # def get(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     qs = AutoParkModel.objects.all()
    #     serializer = AutoParkSerializer(qs, many=True)
    #     return Response(serializer.data, status=200)

    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = AutoParkSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=201)
class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
class AutoParkCarListCreateView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    def get(self,*args,**kwargs):
        pk = kwargs['pk']
        if not AutoParkModel.objects.filter(pk=pk).exists():
            raise Http404
        cars = CarModel.objects.filter(auto_park_id=pk)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=200)

    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # auto_park = self.get_object()
        exists = AutoParkModel.objects.filter(pk=pk).exists()
        if not exists:
            raise Http404()
        serializer.save(auto_park_id=pk)
        return Response(serializer.data, status=201)





