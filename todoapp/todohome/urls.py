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
    path('edit/<int:id>', views.editdata, name='editdata'),
    path('update/<int:id>/', views.updatedata, name='updatedata'),
    path('delete/<int:id>', views.deletedata, name='deletedata'),
    path('statusdata/<int:id>', views.statusdata, name='statusdata'),
    path('completed_tasks/', views.completed_tasks, name='completedtasks'),
    path('remaining_task/', views.remaining_tasks, name='remainingtask'),
]
