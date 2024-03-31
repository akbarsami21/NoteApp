from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.index,name='index'),
    path('completed/',views.completed,name='completed'),
    path('remaining',views.remaining,name='remaining'),
    path('add_task',views.add_task,name='add_task'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('detail/<int:id>',views.task_detail,name='task_detail'),
    path('toggle_complete/<int:id>',views.toggle_complete,name='toggle_complete'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('update/<int:id>',views.update,name='update'),
    
]
