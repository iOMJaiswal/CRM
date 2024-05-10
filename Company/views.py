from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Company.serializers import CompanySerializer
from Company.models import Company


@api_view(['GET'])
def get_companies(request):
    try:
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_company(request, pk):
    try:
        company = Company.objects.get(uuid=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except company.DoesNotExist:
        return Response({'message': 'Company Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_company(request):
    try:
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Company Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def edit_company(request, pk):
    try:
        company = Company.objects.get(uuid=pk)
        serializer = CompanySerializer(
            instance=company, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Company Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Company.DoesNotExist:
        return Response({'message': 'Company Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def delete_company(request, pk):
    try:
        company = Company.objects.get(uuid = pk)
        company.delete()
        return Response({'message': 'Company Deleted'}, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
