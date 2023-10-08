from django.urls import path
from . import views

urlpatterns=[
    path('addTask/', views.addTask, name='addTask'),
    path('markDone/<int:pk>', views.markDone, name='markDone'),
    path('markUnone/<int:pk>', views.markUndone, name='markUndone'),
    path('editTask/<int:pk>', views.editTask, name='editTask'),
    path('deleteTask/<int:pk>', views.deleteTask, name='deleteTask'),
]