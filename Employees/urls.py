from django.urls import path
from Employees.views import *

urlpatterns = [
    
    # ! General APIs
    # ? Immigration APIs
    
    path('general/get-immigration/', get_immigrations, name="get-immigration"),
    path('general/get-immigration/<str:pk>', get_immigration, name="get-immigration"),
    path('general/create-immigration/', create_immigration, name="create-immigration"),
    path('general/edit-immigration/<str:pk>', edit_immigration, name="edit-immigration"),
    path('general/delete-immigration/<str:pk>', delete_immigration, name="delete-immigration"),  
    
    # ? Comtact APIs
    path('general/get-contact/', get_contacts, name="get-contact"),
    path('general/get-contact/<str:pk>', get_contact, name="get-contact"),
    path('general/create-contact/', create_contact, name="create-contact"),
    path('general/edit-contact/<str:pk>', edit_contact, name="edit-contact"),
    path('general/delete-contact/<str:pk>', delete_contact, name="delete-contact"),
    
    # ? Qualification APIs
    path('general/get-qualification/', get_qualifications, name="get-qualification"),
    path('general/get-qualification/<str:pk>', get_qualification, name="get-qualification"),
    path('general/create-qualification/', create_qualification, name="create-qualification"),
    path('general/edit-qualification/<str:pk>', edit_qualification, name="edit-qualification"),
    path('general/delete-qualification/<str:pk>', delete_qualification, name="delete-qualification"),
    
    # ? Work Experience APIs
    path('general/get-work-experience/', get_work_experiences, name="get-work-experience"),
    path('general/get-work-experience/<str:pk>', get_work_experience, name="get-work-experience"),
    path('general/create-work-experience/', create_work_experience, name="create-work-experience"),
    path('general/edit-work-experience/<str:pk>', edit_work_experience, name="edit-work-experience"),
    path('general/delete-work-experience/<str:pk>', delete_work_experience, name="delete-work-experience"),
 
    # ? Bank Account APIs
    path('general/get-bank-account/', get_bank_accounts, name="get-bank-account"),
    path('general/get-bank-account/<str:pk>', get_bank_account, name="get-bank-account"),
    path('general/create-bank-account/', create_bank_account, name="create-bank-account"),
    path('general/edit-bank-account/<str:pk>', edit_bank_account, name="edit-bank-account"),
    path('general/delete-bank-account/<str:pk>', delete_bank_account, name="delete-bank-account"),

    
]