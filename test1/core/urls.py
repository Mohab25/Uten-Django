from django.urls import path,re_path
from .views import BootstrapForm

urlpatterns = [
  path('',BootstrapForm,name='bootstrap_form')  
] 