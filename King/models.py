from django.db import models


class FastFoodType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name




class Food(models.Model):
    food_type = models.ForeignKey(FastFoodType, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100, unique=True)
    content = models.TextField()  
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.IntegerField()
    delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.food_name





class Review(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE) 
    prepared_by = models.CharField(max_length=33)
    created = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField()

    def __str__(self):
        return self.text