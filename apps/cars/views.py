from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import PageNumberPagination

from .filters import car_filtered_queryset
from .models import CarModel
from .serializers import CarSerializer


class CarListView(GenericAPIView, ListModelMixin):
    serializer_class = CarSerializer
    # pagination_class = PageNumberPagination


    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

# def get(self, *args, **kwargs):
    #     qs = car_filtered_queryset(self.request.query_params)
    #     serializer = CarSerializer(qs, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)

class CarRetrieveUpdateDestroyView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     # pk = kwargs['pk']
    #     # car = get_object_or_404(CarModel, pk=pk)
    #     car = self.get_object()
    #     serializer = CarSerializer(car)
    #     return Response(serializer.data, status.HTTP_200_OK)


    # def put(self, *args, **kwargs):
    #     # pk = kwargs['pk']
    #     # # try:
    #     # #     car = CarModel.objects.get(pk=pk)
    #     # # except CarModel.DoesNotExist:
    #     # #     raise Http404()
    #     # car = get_object_or_404(CarModel, pk=pk)
    #     car = self.get_object()
    #     data = self.request.data
    #     serializer = CarSerializer(car, data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)
    # def patch(self, request, *args, **kwargs):
    #     # pk = kwargs['pk']
    #     # car = get_object_or_404(CarModel, pk=pk)
    #     car = self.get_object()
    #     data = self.request.data
    #     serializer = CarSerializer(car, data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)
    # def delete(self, *args, **kwargs):
    #     # pk = kwargs['pk']
    #     # car = get_object_or_404(CarModel, pk=pk)
    #     car = self.get_object()
    #     car.delete()
    #     return Response(status.HTTP_204_NO_CONTENT)