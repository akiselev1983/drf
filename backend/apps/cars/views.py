from django.utils.decorators import method_decorator

from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser

from drf_yasg.utils import swagger_auto_schema

from core.permission.is_superuser import IsSuperUser

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarListView(GenericAPIView, ListModelMixin):
    """
    Get all cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.my_objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get Car by id
    put:
        Full update Car by id
    patch:
        Partial update Car by id
    delete:
        Delete Car by id
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

