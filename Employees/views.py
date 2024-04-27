from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Employees.serializers import EmployeeSerializer
from Employees.models import Employee

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
    except:
        return Response({'message' : 'Something Went Wrong'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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