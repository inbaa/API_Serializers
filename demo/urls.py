from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.apiOverview, name='api-overview'),
    path('task-list/',views.taskList, name='task-list'),
    path('task-detail/<str:key>',views.taskDetail, name='task-detail'),
    path('task-create/',views.taskCreate, name='task-create'),
    path('task-update/<str:key>',views.taskUpdate, name='task-update'),
    path('task-delete/<str:key>',views.taskDelete, name='task-delete'),
]
