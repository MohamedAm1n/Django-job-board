from django.urls import path 
from . import views
app_name='accounts'
urlpatterns = [
    path('SignUp',views.SignUp,name="Sign_up"),
    path('profile',views.profile,name="profile"),
    path('edit',views.EditProfile,name='profile_edit')
]