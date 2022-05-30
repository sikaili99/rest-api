from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import (
    EmailTokenObtainPairView, ListAccountsView,)
from django.urls import path


urlpatterns = [
    path('api/token/', EmailTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('accounts/list/', ListAccountsView.as_view()),
]
