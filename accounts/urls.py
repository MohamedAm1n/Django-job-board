from django.urls import path 
from . import views
app_name='accounts'
urlpatterns = [
    path('/SignUp',views.SignUp,name="Sign_up")
]