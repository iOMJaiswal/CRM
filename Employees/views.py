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





# ! Immigration APIs

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




# ! Contact APIs

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
        


# ! Qualification APIs
    
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




# ! Work Experience APIs

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



# ! Bank Account APIs

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
    
    















