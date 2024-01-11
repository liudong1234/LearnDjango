from django.urls import path, re_path
from . import views

app_name = 'tasks'

urlpatterns = [
    #create tasks
    path('create/', views.task_create, name='task_create'),
    #delete tasks
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
    #updata tasks
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    #retrieve single task
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    path('', views.task_list, name='task_list'),
]