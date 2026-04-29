from django.db import models
from django.db.models import F, Q

# Create your models here.
class Product(models.Model):
    #identity
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    #price
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)

    #quantity
    stock = models.IntegerField(default=0)

    #demand
    views = models.IntegerField(default=0)
    purchased = models.IntegerField(default=0)

    #Time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        constraints = [
            models.CheckConstraint(
                check = Q(base_price__gte = 0),
                name = "base_price_non_negative"
            ),
            models.CheckConstraint(
                check = Q(current_price__gte = 0),
                name = "current_price_non_negative"
            ),
            models.CheckConstraint(
                check = Q(stock__gte = 0),
                name = "stock_non_negative"
            ),
            models.CheckConstraint(
                check = Q(views__gte = 0),
                name = "views_non_negative"
            ),
            models.CheckConstraint(
                check = Q(purchased__gte = 0),
                name = "purchased_non_negative"
            ),
            #logical constraint
            models.CheckConstraint(
                check = Q(purchased__lte = F('views')),
                name = "purchased_less_than_views"
            ),
        ]