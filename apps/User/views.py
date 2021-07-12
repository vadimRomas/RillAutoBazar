from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView, \
    CreateAPIView, ListAPIView
from rest_framework.response import Response

from apps.Car.models import CarsModel
from apps.Car.serializers import CarSerializer
from apps.User.serializers import UserSerializers
from apps.UserProfile.models import UsersProfileModel
from apps.UserProfile.serializers import UserProfileSerializer

UserModel = get_user_model()


class UserListView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        return self.request.user


class UserProfileView(CreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UsersProfileModel.objects.all()

    def perform_create(self, serializer):
        pk = self.request.user.id
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)


class UserProfileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UsersProfileModel.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    # def perform_update(self, serializer):
    #     pk = self.request.user.id
    #     user = get_object_or_404(UsersProfileModel, pk=pk)
    #     serializer.save(user=user)

    def get_object(self):
        pk = self.request.user.id
        user = get_object_or_404(UsersProfileModel, pk=pk)
        return user


class CreateCarView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def perform_create(self, serializer):
        pk = self.request.user.id
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)


class GetUserCarsView(ListAPIView):
    serializer_class = CarSerializer
    # queryset = CarsModel.objects.all()

    def get(self, request, *args, **kwargs):
        qs = CarsModel.objects.all()
        pk = self.request.user.id
        qs = qs.filter(user_id=pk)
        res = CarSerializer(qs, many=True).data
        return Response(res, status.HTTP_200_OK)

    # def get_object(self):
    #     user = self.request.user.id
    #     cars = get_object_or_404(CarsModel, pk=user)
    #     return cars


class SaveCarsView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def perform_create(self, serializer):
        user = UserModel.objects.get(pk=self.request.user.id)
        car = CarsModel.objects.get(pk=self.kwargs.get('pk'))
        car.save_cars.add(user)

    def get(self, request, *args, **kwargs):
        qs = CarsModel.objects.all()
        pk = self.request.user.id
        qs = qs.filter(user_id=pk)
        res = CarSerializer(qs, many=True).data
        return Response(res, status.HTTP_200_OK)
