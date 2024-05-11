from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from CoreHR.serializers import *
from CoreHR.models import *





# ! Promotion API's
@api_view(['GET'])
def get_promotions(request):
    try:
        promotion = Promotion.objects.all()
        serializer = PromotionSerializer(promotion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_promotions_by_employee(request, pk):
    try:
        promotion = Promotion.objects.filter(employee=pk)
        serializer = PromotionSerializer(promotion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
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


# ! Award API's

@api_view(['GET'])
def get_awards(request):
    try:
        award = Award.objects.all()
        serializer = AwardSerializer(award, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_awards_by_employee(request, pk):
    try:
        award = Award.objects.filter(employee=pk)
        serializer = AwardSerializer(award, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_award(request, pk):
    try:
        award = Award.objects.get(uuid=pk)
        serializer = AwardSerializer(award)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except award.DoesNotExist:
        return Response({'message': 'Award Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_award(request):
    try:
        data = request.data
        serializer = AwardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Award Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_award(request, pk):
    try:
        award = Award.objects.get(uuid=pk)
        serializer = AwardSerializer(instance=award, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Award Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Award.DoesNotExist:
        return Response({'message': 'Award Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def delete_award(request, pk):
    try:
        award = Award.objects.get(uuid = pk)
        award.delete()
        return Response({'message': 'Award Deleted'}, status=status.HTTP_200_OK)
    except Award.DoesNotExist:  
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# ! Travel API's

@api_view(['GET'])
def get_travels(request):
    try:
        travel = Travel.objects.all()
        serializer = TravelSerializer(travel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_travel(request, pk):
    try:
        travel = Travel.objects.get(uuid=pk)
        serializer = TravelSerializer(travel)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except travel.DoesNotExist:
        return Response({'message': 'Travel Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_travels_by_employee(request, pk):
    try:
        travel = Travel.objects.filter(employee=pk) 
        serializer = TravelSerializer(travel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_travel(request):
    try:
        data = request.data
        serializer = TravelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Travel Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_travel(request, pk):
    try:
        travel = Travel.objects.get(uuid=pk)
        serializer = TravelSerializer(instance=travel, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Travel Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Travel.DoesNotExist:
        return Response({'message': 'Travel Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_travel(request, pk):
    try:
        travel = Travel.objects.get(uuid = pk)
        travel.delete()
        return Response({'message': 'Travel Deleted'}, status=status.HTTP_200_OK)
    except Travel.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ! Transfer API's

@api_view(['GET'])
def get_transfers(request):
    try:
        transfer = Transfer.objects.all()
        serializer = TransferSerializer(transfer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_transfer(request, pk):
    try:
        transfer = Transfer.objects.get(uuid=pk)
        serializer = TransferSerializer(transfer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except transfer.DoesNotExist:
        return Response({'message': 'Transfer Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_transfers_by_employee(request, pk):
    try:
        transfer = Transfer.objects.filter(employee=pk)
        serializer = TransferSerializer(transfer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
 
@api_view(['POST'])
def create_transfer(request):
    try:
        data = request.data
        serializer = TransferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Transfer Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_transfer(request, pk):
    try:
        transfer = Transfer.objects.get(uuid=pk)
        serializer = TransferSerializer(instance=transfer, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Transfer Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:  
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Transfer.DoesNotExist:
        return Response({'message': 'Transfer Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_transfer(request, pk):
    try:
        transfer = Transfer.objects.get(uuid = pk)
        transfer.delete()
        return Response({'message': 'Transfer Deleted'}, status=status.HTTP_200_OK)
    except Transfer.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# ! Resignation API's

@api_view(['GET'])
def get_resignations(request):
    try:
        resignation = Resignation.objects.all()
        serializer = ResignationSerializer(resignation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_resignation(request, pk):
    try:
        resignation = Resignation.objects.get(uuid=pk)
        serializer = ResignationSerializer(resignation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except resignation.DoesNotExist:
        return Response({'message': 'Resignation Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_resignation(request):
    try:
        data = request.data
        serializer = ResignationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Resignation Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_resignation(request, pk):
    try:
        resignation = Resignation.objects.get(uuid=pk)
        serializer = ResignationSerializer(instance=resignation, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Resignation Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Resignation.DoesNotExist:
        return Response({'message': 'Resignation Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def delete_resignation(request, pk):
    try:
        resignation = Resignation.objects.get(uuid = pk)
        resignation.delete()
        return Response({'message': 'Resignation Deleted'}, status=status.HTTP_200_OK)
    except Resignation.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# ! Complaints API's

@api_view(['GET'])
def get_complaints(request):
    try:
        complaint = Complaint.objects.all()
        serializer = ComplaintSerializer(complaint, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_complaint(request, pk):
    try:
        complaint = Complaint.objects.get(uuid=pk)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except complaint.DoesNotExist:
        return Response({'message': 'Complaint Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def get_complaints_by_employee(request, pk):
    try:
        complaint = Complaint.objects.filter(employee=pk)  
        serializer = ComplaintSerializer(complaint, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)    
    
@api_view(['POST'])
def create_complaint(request):
    try:
        data = request.data
        serializer = ComplaintSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Complaint Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_complaint(request, pk):
    try:
        complaint = Complaint.objects.get(uuid=pk)
        serializer = ComplaintSerializer(instance=complaint, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Complaint Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Complaint.DoesNotExist:
        return Response({'message': 'Complaint Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST']) 
def delete_complaint(request, pk):
    try:
        complaint = Complaint.objects.get(uuid = pk)
        complaint.delete()
        return Response({'message': 'Complaint Deleted'}, status=status.HTTP_200_OK)
    except Complaint.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# ! Warning API's

@api_view(['GET'])
def get_warnings(request):
    try:
        warning = Warning.objects.all()
        serializer = WarningSerializer(warning, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_warning(request, pk):
    try:
        warning = Warning.objects.get(uuid=pk)
        serializer = WarningSerializer(warning)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except warning.DoesNotExist:
        return Response({'message': 'Warning Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def get_warnings_by_employee(request, pk):
    try:
        warning = Warning.objects.filter(employee=pk)  
        serializer = WarningSerializer(warning, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Something Went Wrong', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)    
       
@api_view(['POST'])
def create_warning(request):
    try:
        data = request.data
        serializer = WarningSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Warning Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_warning(request, pk):
    try:
        warning = Warning.objects.get(uuid=pk)
        serializer = WarningSerializer(instance=warning, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Warning Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Warning.DoesNotExist:
        return Response({'message': 'Warning Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_warning(request, pk):
    try:
        warning = Warning.objects.get(uuid = pk)
        warning.delete()
        return Response({'message': 'Warning Deleted'}, status=status.HTTP_200_OK)
    except Warning.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# ! Termination API's

@api_view(['GET'])
def get_terminations(request):
    try:
        termination = Termination.objects.all()
        serializer = TerminationSerializer(termination, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_termination(request, pk):
    try:
        termination = Termination.objects.get(uuid=pk)
        serializer = TerminationSerializer(termination)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except termination.DoesNotExist:
        return Response({'message': 'Termination Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_termination(request):
    try:
        data = request.data
        serializer = TerminationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Termination Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def edit_termination(request, pk):
    try:
        termination = Termination.objects.get(uuid=pk)
        serializer = TerminationSerializer(instance=termination, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Termination Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Termination.DoesNotExist:   
        return Response({'message': 'Termination Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def delete_termination(request, pk):
    try:
        termination = Termination.objects.get(uuid = pk)
        termination.delete()
        return Response({'message': 'Termination Deleted'}, status=status.HTTP_200_OK)
    except Termination.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    




# ! Specific to Employee Section 

@api_view(['GET'])
def get_trainings(request):
    try:
        training = Training.objects.all()
        serializer = TrainingSerializer(training, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_training(request, pk):
    try:
        training = Training.objects.get(uuid=pk)
        serializer = TrainingSerializer(training)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except training.DoesNotExist:
        return Response({'message': 'Training Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_trainings_by_employee(request, pk):
    try:
        employee = Employee.objects.get(uuid=pk)
        training = Training.objects.filter(employee=employee)
        serializer = TrainingSerializer(training, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_training(request):
    try:
        data = request.data
        serializer = TrainingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Training Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Wrong data recieved', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def edit_training(request, pk):
    try:
        training = Training.objects.get(uuid=pk)
        serializer = TrainingSerializer(instance=training, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Training Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong data received', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Training.DoesNotExist:
        return Response({'message': 'Training Not Found, Please Enter Valid UUID'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def delete_training(request, pk):
    try:
        training = Training.objects.get(uuid = pk)
        training.delete()
        return Response({'message': 'Training Deleted'}, status=status.HTTP_200_OK)
    except Training.DoesNotExist:
        return Response({'message': 'Please enter valid uuid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message' : 'Something Went Wrong', 'error' : str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)














