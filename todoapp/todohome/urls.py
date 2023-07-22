from django.urls import path
from todohome import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('alldata', views.alldata, name='alldata'),
# ]

# from django.urls import path
# from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('alldata/', views.alldata, name='alldata'),
    path('remaining_task/', views.alldata, name='remaining_task'),
    path('completed_tasks/', views.alldata, name='completed_tasks'),

]
