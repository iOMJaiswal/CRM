from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Employees.serializers import *
from Employees.models import *

@api_view(['GET'])
def get_employees(request):
    try:
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except :
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_employee(request, pk):
    try:
        employee = Employee.objects.get(uuid=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except employee.DoesNotExist:
        return Response({'message': 'Employee Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message' : 'Something Went Wrong'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_employee(request):
    try:
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def edit_employee(request, pk):
    try:
        employee = Employee.objects.get(uuid=pk)
        serializer = EmployeeSerializer(
            instance=employee, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Employee.DoesNotExist:
        return Response({'message': 'Employee Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(uuid = pk)
        employee.delete()
        return Response({'message': 'Employee Deleted'}, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# ! General
# ? Immigration APIs

@api_view(['GET'])
def get_immigrations(request):
    try:
        imms = Immigration.objects.all()
        serializer = ImmigrationSerializer(imms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except :
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_immigration(request, pk):
    try:
        imm = Immigration.objects.get(uuid=pk)
        serializer = ImmigrationSerializer(imm)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except imm.DoesNotExist:
        return Response({'message': 'Immigration Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message' : 'Something Went Wrong'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_immigration(request):
    try:
        data = request.data
        serializer = ImmigrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Immigration Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def edit_immigration(request, pk):
    try:
        imm = Immigration.objects.get(uuid=pk)
        serializer = ImmigrationSerializer(
            instance=imm, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Immigration Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except imm.DoesNotExist:
        return Response({'message': 'Immigration Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_immigration(request, pk):
    try:
        imm = Immigration.objects.get(uuid = pk)
        imm.delete()
        return Response({'message': 'Immigration Deleted'}, status=status.HTTP_200_OK)
    except imm.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# ? Contact APIs

@api_view(['GET'])
def get_contacts(request):
    try:
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except :
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_contact(request, pk):
    try:
        contact = Contact.objects.get(uuid=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except contact.DoesNotExist:
        return Response({'message': 'Contact Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_contact(request):
    try:
        data = request.data
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Contact Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def edit_contact(request, pk):
    try:
        contact = Contact.objects.get(uuid=pk)
        serializer = ContactSerializer(
            instance=contact, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Contact Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except contact.DoesNotExist:
        return Response({'message': 'Contact Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_contact(request, pk):
    try:
        contact = Contact.objects.get(uuid = pk)
        contact.delete()
        return Response({'message': 'Contact Deleted'}, status=status.HTTP_200_OK)
    except contact.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


# ? Qualification APIs
    
@api_view(['GET'])
def get_qualifications(request):
    try:
        qualifications = Qualification.objects.all()
        serializer = QualificationSerializer(qualifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_qualification(request, pk):
    try:
        qualification = Qualification.objects.get(uuid=pk)
        serializer = QualificationSerializer(qualification)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except qualification.DoesNotExist:
        return Response({'message': 'Qualification Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_qualification(request):
    try:
        data = request.data
        serializer = QualificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Qualification Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def edit_qualification(request, pk):
    try:
        qualification = Qualification.objects.get(uuid=pk)
        serializer = QualificationSerializer(
            instance=qualification, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Qualification Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except qualification.DoesNotExist:
        return Response({'message': 'Qualification Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_qualification(request, pk):
    try:
        qualification = Qualification.objects.get(uuid = pk)
        qualification.delete()
        return Response({'message': 'Qualification Deleted'}, status=status.HTTP_200_OK)
    except qualification.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# ? Work Experience APIs

@api_view(['GET'])
def get_work_experiences(request):
    try:
        work_experiences = WorkExperience.objects.all()
        serializer = WorkExperienceSerializer(work_experiences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_work_experience(request, pk):
    try:
        work_experience = WorkExperience.objects.get(uuid=pk)
        serializer = WorkExperienceSerializer(work_experience)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except work_experience.DoesNotExist:
        return Response({'message': 'Work Experience Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_work_experience(request):
    try:
        data = request.data
        serializer = WorkExperienceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Work Experience Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_work_experience(request, pk):
    try:
        work_experience = WorkExperience.objects.get(uuid=pk)
        serializer = WorkExperienceSerializer(
            instance=work_experience, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Work Experience Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except work_experience.DoesNotExist:
        return Response({'message': 'Work Experience Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_work_experience(request, pk):
    try:
        work_experience = WorkExperience.objects.get(uuid = pk)
        work_experience.delete()
        return Response({'message': 'Work Experience Deleted'}, status=status.HTTP_200_OK)
    except work_experience.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# ? Bank Account APIs

@api_view(['GET'])
def get_bank_accounts(request):
    try:
        bank_accounts = BankAccount.objects.all()
        serializer = BankAccountSerializer(bank_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_bank_account(request, pk):
    try:
        bank_account = BankAccount.objects.get(uuid=pk)
        serializer = BankAccountSerializer(bank_account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except bank_account.DoesNotExist:
        return Response({'message': 'Bank Account Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_bank_account(request):
    try:
        data = request.data
        serializer = BankAccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Bank Account Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def edit_bank_account(request, pk):
    try:
        bank_account = BankAccount.objects.get(uuid=pk)
        serializer = BankAccountSerializer(
            instance=bank_account, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Bank Account Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except bank_account.DoesNotExist:
        return Response({'message': 'Bank Account Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_bank_account(request, pk):
    try:
        bank_account = BankAccount.objects.get(uuid = pk)
        bank_account.delete()
        return Response({'message': 'Bank Account Deleted'}, status=status.HTTP_200_OK)
    except bank_account.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
# ! Set Salary APIs

# ? BasicSalary
@api_view(['GET'])
def get_basic_salaries(request):
    try:
        basic_salaries = BasicSalary.objects.all()
        serializer = BasicSalarySerializer(basic_salaries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_basic_salary(request, pk):
    try:
        basic_salary = BasicSalary.objects.get(uuid=pk)
        serializer = BasicSalarySerializer(basic_salary)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except basic_salary.DoesNotExist:
        return Response({'message': 'Basic Salary Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_basic_salary(request):
    try:
        data = request.data
        serializer = BasicSalarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Basic Salary Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_basic_salary(request, pk):
    try:   
        basic_salary = BasicSalary.objects.get(uuid=pk)
        serializer = BasicSalarySerializer(
            instance=basic_salary, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Basic Salary Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except basic_salary.DoesNotExist:
        return Response({'message': 'Basic Salary Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_basic_salary(request, pk):
    try:
        basic_salary = BasicSalary.objects.get(uuid = pk)
        basic_salary.delete()
        return Response({'message': 'Basic Salary Deleted'}, status=status.HTTP_200_OK)
    except basic_salary.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ? Allowances
@api_view(['GET'])
def get_allowances(request):
    try:
        allowances = Allowances.objects.all()
        serializer = AllowancesSerializer(allowances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_allowance(request, pk):
    try:
        allowance = Allowances.objects.get(uuid=pk)
        serializer = AllowancesSerializer(allowance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except allowance.DoesNotExist:
        return Response({'message': 'Allowance Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_allowance(request):
    try:
        data = request.data
        serializer = AllowancesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Allowance Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_allowance(request, pk):
    try:   
        allowance = Allowances.objects.get(uuid=pk)
        serializer = AllowancesSerializer(
            instance=allowance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Allowance Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except allowance.DoesNotExist:
        return Response({'message': 'Allowance Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_allowance(request, pk):
    try:
        allowance = Allowances.objects.get(uuid = pk)
        allowance.delete()
        return Response({'message': 'Allowance Deleted'}, status=status.HTTP_200_OK)
    except allowance.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
# ? Commissions
@api_view(['GET'])
def get_commissions(request):
    try:
        commissions = Commissions.objects.all()
        serializer = CommissionsSerializer(commissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_commission(request, pk):
    try:
        commission = Commissions.objects.get(uuid=pk)
        serializer = CommissionsSerializer(commission)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except commission.DoesNotExist:
        return Response({'message': 'Commission Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_commission(request):
    try:
        data = request.data
        serializer = CommissionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Commission Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_commission(request, pk):
    try:
        commission = Commissions.objects.get(uuid=pk)
        serializer = CommissionsSerializer(
            instance=commission, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Commission Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except commission.DoesNotExist:
        return Response({'message': 'Commission Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

@api_view(['POST'])
def delete_commission(request, pk):
    try:
        commission = Commissions.objects.get(uuid = pk)
        commission.delete()
        return Response({'message': 'Commission Deleted'}, status=status.HTTP_200_OK)
    except commission.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# ? Loans
@api_view(['GET'])
def get_loans(request):
    try:
        loans = Loans.objects.all()
        serializer = LoansSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_loan(request, pk):
    try:
        loan = Loans.objects.get(uuid=pk)
        serializer = LoansSerializer(loan)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except loan.DoesNotExist:
        return Response({'message': 'Loan Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_loan(request):
    try:
        data = request.data
        serializer = LoansSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Loan Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def edit_loan(request, pk):
    try:
        loan = Loans.objects.get(uuid=pk)
        serializer = LoansSerializer(
            instance=loan, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Loan Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except loan.DoesNotExist:
        return Response({'message': 'Loan Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_loan(request, pk):
    try:
        loan = Loans.objects.get(uuid = pk)
        loan.delete()
        return Response({'message': 'Loan Deleted'}, status=status.HTTP_200_OK)
    except loan.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# ? StatutoryDeductions
@api_view(['GET'])
def get_statutory_deductions(request):
    try:
        statutorydeductions = StatutoryDeductions.objects.all()
        serializer = StatutoryDeductionsSerializer(statutorydeductions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_statutory_deduction(request, pk):
    try:
        statutorydeduction = StatutoryDeductions.objects.get(uuid=pk)
        serializer = StatutoryDeductionsSerializer(statutorydeduction)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except statutorydeduction.DoesNotExist:
        return Response({'message': 'StatutoryDeduction Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_statutory_deduction(request):
    try:
        data = request.data
        serializer = StatutoryDeductionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'StatutoryDeduction Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_statutory_deduction(request, pk):
    try:
        statutorydeduction = StatutoryDeductions.objects.get(uuid=pk)
        serializer = StatutoryDeductionsSerializer(
            instance=statutorydeduction, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'StatutoryDeduction Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except statutorydeduction.DoesNotExist:
        return Response({'message': 'StatutoryDeduction Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_statutory_deduction(request, pk):
    try:
        statutorydeduction = StatutoryDeductions.objects.get(uuid = pk)
        statutorydeduction.delete()
        return Response({'message': 'StatutoryDeduction Deleted'}, status=status.HTTP_200_OK)
    except statutorydeduction.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# ? OtherPayments
@api_view(['GET'])
def get_other_payments(request):
    try:
        otherpayments = OtherPayments.objects.all()
        serializer = OtherPaymentsSerializer(otherpayments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_other_payment(request, pk):
    try:
        otherpayment = OtherPayments.objects.get(uuid=pk)
        serializer = OtherPaymentsSerializer(otherpayment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except otherpayment.DoesNotExist:
        return Response({'message': 'OtherPayment Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_other_payment(request):
    try:
        data = request.data
        serializer = OtherPaymentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'OtherPayment Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_other_payment(request, pk):
    try:
        otherpayment = OtherPayments.objects.get(uuid=pk)
        serializer = OtherPaymentsSerializer(
            instance=otherpayment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'OtherPayment Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except otherpayment.DoesNotExist:   
        return Response({'message': 'OtherPayment Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_other_payment(request, pk):
    try:
        otherpayment = OtherPayments.objects.get(uuid = pk)
        otherpayment.delete()
        return Response({'message': 'OtherPayment Deleted'}, status=status.HTTP_200_OK)
    except otherpayment.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# ? Overtime
@api_view(['GET'])
def get_overtimes(request):
    try:
        overtimes = Overtime.objects.all()
        serializer = OvertimeSerializer(overtimes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_overtime(request, pk):
    try:
        overtime = Overtime.objects.get(uuid=pk)
        serializer = OvertimeSerializer(overtime)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except overtime.DoesNotExist:
        return Response({'message': 'Overtime Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_overtime(request):
    try:
        data = request.data
        serializer = OvertimeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Overtime Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_overtime(request, pk):
    try:
        overtime = Overtime.objects.get(uuid=pk)
        serializer = OvertimeSerializer(
            instance=overtime, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Overtime Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except overtime.DoesNotExist:   
        return Response({'message': 'Overtime Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_overtime(request, pk):
    try:
        overtime = Overtime.objects.get(uuid = pk)
        overtime.delete()
        return Response({'message': 'Overtime Deleted'}, status=status.HTTP_200_OK)
    except overtime.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ? SalaryPension
@api_view(['GET'])
def get_salary_pensions(request):
    try:
        salarypension = SalaryPension.objects.all()
        serializer = SalaryPensionSerializer(salarypension, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_salary_pension(request, pk):
    try:
        salarypension = SalaryPension.objects.get(uuid=pk)
        serializer = SalaryPensionSerializer(salarypension)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except salarypension.DoesNotExist:
        return Response({'message': 'SalaryPension Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_salary_pension(request):
    try:
        data = request.data
        serializer = SalaryPensionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'SalaryPension Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_salary_pension(request, pk):
    try:
        salarypension = SalaryPension.objects.get(uuid=pk)
        serializer = SalaryPensionSerializer(
            instance=salarypension, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'SalaryPension Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except salarypension.DoesNotExist:   
        return Response({'message': 'SalaryPension Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_salary_pension(request, pk):
    try:
        salarypension = SalaryPension.objects.get(uuid = pk)
        salarypension.delete()
        return Response({'message': 'SalaryPension Deleted'}, status=status.HTTP_200_OK)
    except salarypension.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)








