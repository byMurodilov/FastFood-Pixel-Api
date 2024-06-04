from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from .models import FastFoodType, Food, Review
from .serializers import FFTypeSerializer, FoodSerializer, ReviewSerializer


class FastFoodTypeViewSet(viewsets.ModelViewSet):
    
    queryset = FastFoodType.objects.all()
    serializer_class = FFTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]




class FoodViewSet(viewsets.ModelViewSet):

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]



class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication  ,TokenAuthentication]



def index(request):
    return render(request, 'index.html')