from rest_framework import serializers
from .models import FastFoodType, Food, Review


class FFTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastFoodType
        fields = '__all__'



class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
