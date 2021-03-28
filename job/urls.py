from django.urls import path 
from . import views
app_name='job'
urlpatterns = [
    path('',views.job_list_view),
    path('<str:slug>',views.job_details_view,name='job_detail'),
]