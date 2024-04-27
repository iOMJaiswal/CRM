"""
URL configuration for CRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Company.views import *
from Employees.views import *
from Promotion.views import *
from Client.views import *

urlpatterns = [
    
    # ! Company
    path('get-company/', get_companies, name="get-company"),
    path('get-company/<str:pk>', get_company, name="get-company"),
    path('create-company/', create_company, name="create-company"),
    path('edit-company/<str:pk>', edit_company, name="edit-company"),
    path('delete-company/<str:pk>', delete_company, name="delete-company"),
    
    # ! Employees
    path('get-employee/', get_employees, name="get-employee"),
    path('get-employee/<str:pk>', get_employee, name="get-employee"),
    path('create-employee/', create_employee, name="create-employee"),
    path('edit-employee/<str:pk>', edit_employee, name="edit-employee"),
    path('delete-employee/<str:pk>', delete_employee, name="delete-employee"), 
    
    # ! Promotion
    path('get-promotion/', get_promotions, name="get-promotion"),
    path('get-promotion/<str:pk>', get_promotion, name="get-promotion"),
    path('create-promotion/', create_promotion, name="create-promotion"),
    path('edit-promotion/<str:pk>', edit_promotion, name="edit-promotion"),
    path('delete-promotion/<str:pk>', delete_promotion, name="delete-promotion"),
     
    # ! Client
    path('get-client/', get_clients, name="get-client"),
    path('get-client/<str:pk>', get_client, name="get-client"),
    path('create-client/', create_client, name="create-client"),
    path('edit-client/<str:pk>', edit_client, name="edit-client"),
    path('delete-client/<str:pk>', delete_client, name="delete-client"),
    
]
