from django.urls import path
from creds import views

app_name = 'creds'

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]