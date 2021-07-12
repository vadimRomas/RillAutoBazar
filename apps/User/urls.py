from django.urls import path

from apps.User.views import UserListView, UserProfileView, UserProfileRetrieveUpdateDestroyView, GetUserCarsView, \
    SaveCarsView

urlpatterns = [
    path('', UserListView.as_view()),
    path('/profile', UserProfileView.as_view()),
    path('/info', UserProfileRetrieveUpdateDestroyView.as_view()),
    path('/cars', GetUserCarsView.as_view()),
    path('/save/car<int:pk>', SaveCarsView.as_view())
]
