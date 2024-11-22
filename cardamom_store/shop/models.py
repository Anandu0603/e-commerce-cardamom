from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Cardamom(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    quantity = models.FloatField()  # in kg
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    date_harvested = models.DateField()

    def __str__(self):
        return f"{self.quantity} kg from {self.farmer.name}"

class Order(models.Model):
    cardamom = models.ForeignKey(Cardamom, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_address = models.TextField()
    quantity_ordered = models.FloatField()  # in kg
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.buyer_name} for {self.quantity_ordered} kg"