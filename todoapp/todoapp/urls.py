from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todohome.urls')),
    path('', include('accounts.urls')),
]
