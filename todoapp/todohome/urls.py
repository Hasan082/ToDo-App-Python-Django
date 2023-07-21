from django.urls import path
from todohome import views

urlpatterns = [
    path('', views.index, name='home'),
]
