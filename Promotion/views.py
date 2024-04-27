from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Promotion.serializers import PromotionSerializer
from Promotion.models import Promotion




@api_view(['GET'])
def get_promotions(request):
    try:
        promotion = Promotion.objects.all()
        serializer = PromotionSerializer(promotion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_promotion(request, pk):
    try:
        promotion = Promotion.objects.get(uuid=pk)
        serializer = PromotionSerializer(promotion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except promotion.DoesNotExist:
        return Response({'message': 'Promotion Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_promotion(request):
    try:
        data = request.data
        serializer = PromotionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Promotion Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_promotion(request, pk):
    try:
        promotion = Promotion.objects.get(uuid=pk)
        serializer = PromotionSerializer(instance=promotion, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Promotion Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Promotion.DoesNotExist:
        return Response({'message': 'Promotion Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_promotion(request, pk):
    try:
        promotion = Promotion.objects.get(uuid = pk)
        promotion.delete()
        return Response({'message': 'Promotion Deleted'}, status=status.HTTP_200_OK)
    except Promotion.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
