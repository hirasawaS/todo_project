from django.urls import path 
from . import views
app_name = "todoapp"

urlpatterns = [
    path("" , views.IndexView.as_view() , name="index") , 
    path("detail/<int:pk>/", views.TaskDetail.as_view() , name="detail" ) , 
    path("createTaskBottom/" , views.CreateBottomTaskView.as_view() , name="create_bottom_task" )    
]