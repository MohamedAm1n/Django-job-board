from django.urls import path 
from . import views
urlpatterns = [
    path('',views.job_list_view),
    path('<int:id>',views.job_detail_view),
]