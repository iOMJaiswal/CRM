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
from django.urls import path
from CoreHR.views import *

urlpatterns = [
    
    # ! Promotion
    path('get-promotion/', get_promotions, name="get-promotion"),
    path('get-promotion/<str:pk>', get_promotion, name="get-promotion"),
    path('get-promotion-by-employee/<str:pk>', get_promotions_by_employee, name="get-promotion-by-employee"),
    path('create-promotion/', create_promotion, name="create-promotion"),
    path('edit-promotion/<str:pk>', edit_promotion, name="edit-promotion"),
    path('delete-promotion/<str:pk>', delete_promotion, name="delete-promotion"),
    
    
    # ! Award
    path('get-award/', get_awards, name="get-award"),
    path('get-award/<str:pk>', get_award, name="get-award"),
    path('get-award-by-employee/<str:pk>', get_awards_by_employee, name="get-award-by-employee"),
    path('create-award/', create_award, name="create-award"),
    path('edit-award/<str:pk>', edit_award, name="edit-award"),
    path('delete-award/<str:pk>', delete_award, name="delete-award"),
    
    # ! Travel 
    path('get-travel/', get_travels, name="get-travel"),
    path('get-travel/<str:pk>', get_travel, name="get-travel"),
    path('get-travel-by-employee/<str:pk>', get_travels_by_employee, name="get-travel-by-employee"),
    path('create-travel/', create_travel, name="create-travel"),
    path('edit-travel/<str:pk>', edit_travel, name="edit-travel"),
    path('delete-travel/<str:pk>', delete_travel, name="delete-travel"),
    
    # ! Transfer
    path('get-transfer/', get_transfers, name="get-transfer"),
    path('get-transfer/<str:pk>', get_transfer, name="get-transfer"),
    path('get-transfer-by-employee/<str:pk>', get_transfers_by_employee, name="get-transfer-by-employee"),
    path('create-transfer/', create_transfer, name="create-transfer"),
    path('edit-transfer/<str:pk>', edit_transfer, name="edit-transfer"),
    path('delete-transfer/<str:pk>', delete_transfer, name="delete-transfer"),
    
    # ! Resignation
    path('get-resignation/', get_resignations, name="get-resignation"),
    path('get-resignation/<str:pk>', get_resignation, name="get-resignation"),
    path('create-resignation/', create_resignation, name="create-resignation"),
    path('edit-resignation/<str:pk>', edit_resignation, name="edit-resignation"),
    path('delete-resignation/<str:pk>', delete_resignation, name="delete-resignation"),
    
    # ! Complaint
    path('get-complaint/', get_complaints, name="get-complaint"),
    path('get-complaint/<str:pk>', get_complaint, name="get-complaint"),
    path('get-complaint-by-employee/<str:pk>', get_complaints_by_employee, name="get-complaint-by-employee"),
    path('create-complaint/', create_complaint, name="create-complaint"),
    path('edit-complaint/<str:pk>', edit_complaint, name="edit-complaint"),
    path('delete-complaint/<str:pk>', delete_complaint, name="delete-complaint"),
    
    # ! Warning
    path('get-warning/', get_warnings, name="get-warning"),
    path('get-warning/<str:pk>', get_warning, name="get-warning"),
    path('get-warning-by-employee/<str:pk>', get_warnings_by_employee, name="get-warning-by-employee"),
    path('create-warning/', create_warning, name="create-warning"),
    path('edit-warning/<str:pk>', edit_warning, name="edit-warning"),
    path('delete-warning/<str:pk>', delete_warning, name="delete-warning"),
    
    # ! Termination
    path('get-termination/', get_terminations, name="get-termination"),
    path('get-termination/<str:pk>', get_termination, name="get-termination"),
    path('create-termination/', create_termination, name="create-termination"),
    path('edit-termination/<str:pk>', edit_termination, name="edit-termination"),
    path('delete-termination/<str:pk>', delete_termination, name="delete-termination"),
    
    
    
    # ! Specific to Employee Section 
    
    # ? Training
    path('get-training/', get_trainings, name="get-training"),
    path('get-training/<str:pk>', get_training, name="get-training"),
    path('get-training-by-employee/<str:pk>', get_trainings_by_employee, name="get-training-by-employee"),
    path('create-training/', create_training, name="create-training"),
    path('edit-training/<str:pk>', edit_training, name="edit-training"),
    path('delete-training/<str:pk>', delete_training, name="delete-training"),
    
    
]
