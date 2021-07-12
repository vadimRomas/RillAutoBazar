from django.urls import path

from apps.Car.views import AllCarsListView, CarView, GetCreateImagesCarView
from apps.User.views import CreateCarView

urlpatterns = [
    path('/create', CreateCarView.as_view()),
    path('/all', AllCarsListView.as_view()),
    path('/<int:pk>', CarView.as_view()),
    path('/<int:pk>/images', GetCreateImagesCarView.as_view())
]
