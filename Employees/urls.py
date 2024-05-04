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



    # ! Set Salary APIs
    
    # ? Basic Salary APIs
    path('set-salary/get-basic-salary/', get_basic_salaries, name="get-basic-salary"),
    path('set-salary/get-basic-salary/<str:pk>', get_basic_salary, name="get-basic-salary"),
    path('set-salary/create-basic-salary/', create_basic_salary, name="create-basic-salary"),
    path('set-salary/edit-basic-salary/<str:pk>', edit_basic_salary, name="edit-basic-salary"),
    path('set-salary/delete-basic-salary/<str:pk>', delete_basic_salary, name="delete-basic-salary"),
    
    # ? Allowance APIs
    path('set-salary/get-allowance/', get_allowances, name="get-allowance"),
    path('set-salary/get-allowance/<str:pk>', get_allowance, name="get-allowance"),
    path('set-salary/create-allowance/', create_allowance, name="create-allowance"),
    path('set-salary/edit-allowance/<str:pk>', edit_allowance, name="edit-allowance"),
    path('set-salary/delete-allowance/<str:pk>', delete_allowance, name="delete-allowance"),
    
    # ? Commission APIs
    path('set-salary/get-commission/', get_commissions, name="get-commission"),
    path('set-salary/get-commission/<str:pk>', get_commission, name="get-commission"),
    path('set-salary/create-commission/', create_commission, name="create-commission"),
    path('set-salary/edit-commission/<str:pk>', edit_commission, name="edit-commission"),
    path('set-salary/delete-commission/<str:pk>', delete_commission, name="delete-commission"), 
    
    # ? Loans APIs
    path('set-salary/get-loan/', get_loans, name="get-loan"),
    path('set-salary/get-loan/<str:pk>', get_loan, name="get-loan"),
    path('set-salary/create-loan/', create_loan, name="create-loan"),
    path('set-salary/edit-loan/<str:pk>', edit_loan, name="edit-loan"),
    path('set-salary/delete-loan/<str:pk>', delete_loan, name="delete-loan"),
    
    # ? StatutoryDeductions APIs
    path('set-salary/get-statutory-deduction/', get_statutory_deductions, name="get-statutory-deduction"),
    path('set-salary/get-statutory-deduction/<str:pk>', get_statutory_deduction, name="get-statutory-deduction"),   
    path('set-salary/create-statutory-deduction/', create_statutory_deduction, name="create-statutory-deduction"),
    path('set-salary/edit-statutory-deduction/<str:pk>', edit_statutory_deduction, name="edit-statutory-deduction"),
    path('set-salary/delete-statutory-deduction/<str:pk>', delete_statutory_deduction, name="delete-statutory-deduction"),
    
    # ? OtherPayments APIs
    path('set-salary/get-other-payment/', get_other_payments, name="get-other-payment"),
    path('set-salary/get-other-payment/<str:pk>', get_other_payment, name="get-other-payment"),
    path('set-salary/create-other-payment/', create_other_payment, name="create-other-payment"),
    path('set-salary/edit-other-payment/<str:pk>', edit_other_payment, name="edit-other-payment"),
    path('set-salary/delete-other-payment/<str:pk>', delete_other_payment, name="delete-other-payment"),
    
    # ? Overtime APIs
    path('set-salary/get-overtime/', get_overtimes, name="get-overtime"),
    path('set-salary/get-overtime/<str:pk>', get_overtime, name="get-overtime"),
    path('set-salary/create-overtime/', create_overtime, name="create-overtime"),
    path('set-salary/edit-overtime/<str:pk>', edit_overtime, name="edit-overtime"),
    path('set-salary/delete-overtime/<str:pk>', delete_overtime, name="delete-overtime"),
    
    # ? SalaryPension APIs
    path('set-salary/get-salary-pension/', get_salary_pensions, name="get-salary-pension"),
    path('set-salary/get-salary-pension/<str:pk>', get_salary_pension, name="get-salary-pension"),
    path('set-salary/create-salary-pension/', create_salary_pension, name="create-salary-pension"),
    path('set-salary/edit-salary-pension/<str:pk>', edit_salary_pension, name="edit-salary-pension"),
    path('set-salary/delete-salary-pension/<str:pk>', delete_salary_pension, name="delete-salary-pension"),
    
    
    
]