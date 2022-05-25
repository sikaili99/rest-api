from django.urls import path
from . views import ListUsersView

urlpatterns = [
    path('users/list/', ListUsersView.as_view()),
]
