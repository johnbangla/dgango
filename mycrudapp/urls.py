"""mycrudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.emp_home,name='emp_home'),
    path('newentry/', views.emp_form,name='emp_insert'),
  
    path('list/',views.emp_list,name='emp_list'),
    path('<int:id>',views.emp_form, name= 'emp_update'),
    path('delete/<int:id>', views.emp_delete,name='emp_delete'),
    path('details/<int:id>', views.emp_details,name='emp_details'),
   
  
]
