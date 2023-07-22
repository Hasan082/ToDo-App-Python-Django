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
    # ... other URL patterns ...
]
