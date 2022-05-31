from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/v1/', include('accounts.urls')),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
]
