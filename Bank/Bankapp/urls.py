from django.urls import path
from . import views

app_name = 'Bankapp'

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    #path('login/', views.login, name='login'),
    #path('register/', views.reg, name='register'),
    path('tofill/', views.tofill, name='tofill'),
    path('adddetails/fill/', views.adddet, name='AddDet'),
    path('adddetails/ajax/load_branches/', views.load_branches, name='ajax_load_branches'),
    path('accepted/', views.accept, name='accept'),
    
]
