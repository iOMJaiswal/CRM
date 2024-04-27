from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Client.serializers import ClientSerializer
from Client.models import Client

@api_view(['GET'])
def get_clients(request):
    try:
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({'message': 'Clients Not Found'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_client(request, pk):
    try:
        client = Client.objects.get(uuid=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({'message': 'Client Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_client(request):
    try:
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Client Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

@api_view(['POST'])
def edit_client(request, pk):
    try:
        client = Client.objects.get(uuid=pk)
        serializer = ClientSerializer(instance=client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Client Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Client.DoesNotExist:
        return Response({'message': 'Client Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_client(request, pk):
    try:
        client = Client.objects.get(uuid = pk)
        client.delete()
        return Response({'message': 'Client Deleted'}, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
