"""models"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Purchase(models.Model):
    """purchase model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchases")
    symbol = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=75)
    shares = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0)])

    purchases = models.Manager()

    def get_purchaser(self):
        """returns the user who made this purchase"""

    def get_symbol(self):
        """returns symbol of this purchase"""
        return self.symbol

    def get_name(self):
        """returns name of this purchase"""
        return self.name

    def get_shares(self):
        """returns shares of this purchase"""
        return self.shares

    def get_price(self):
        """returns price of this purchase"""
        return self.price

    def __str__(self):
        """returns the string represention of this purchase"""
        return f"{self.symbol} ({self.name})"
