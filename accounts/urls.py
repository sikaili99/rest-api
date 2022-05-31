from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import (
    EmailTokenObtainPairView, ListAccountsView, RegisterView,)
from django.urls import path


urlpatterns = [
    path('api/token/', EmailTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/list/', ListAccountsView.as_view()),
    path('api/register/', RegisterView.as_view()),
]
