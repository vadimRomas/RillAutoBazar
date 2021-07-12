from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.response import Response

from apps.Car.models import CarsModel, ImagesCarModel
from apps.Car.serializers import CarSerializer, ImagesCarSerializer


class CarView(RetrieveAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]


class AllCarsListView(ListAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        qs = CarsModel.objects.all()
        city = self.request.query_params.get('city')
        brand = self.request.query_params.get('brand')

        if city:
            qs = qs.filter(city__iexact=city)

        if brand:
            qs = qs.filter(brand__iexact=brand)

        res = CarSerializer(qs, many=True).data
        return Response(res, status.HTTP_200_OK)


class GetCreateImagesCarView(ListCreateAPIView):
    queryset = ImagesCarModel.objects.all()
    serializer_class = ImagesCarSerializer

    def perform_create(self, serializer):
        user_id = self.request.user.id
        pk = self.kwargs.get('pk')
        car = get_object_or_404(CarsModel, pk=pk)
        serializer.save(car=car)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        car = get_object_or_404(CarsModel, pk=pk)
        return car
