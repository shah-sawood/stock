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
        return self.user

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


class Portfolio(models.Model):
    """portfolio"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    total = models.PositiveIntegerField(default=10000)
    cash = models.PositiveIntegerField(default=10000, validators=[MinValueValidator(0)])

    def get_user(self):
        """returns the user of this portfolio"""
        return self.user

    def get_total(self):
        """returns the total amount of this account"""
        return self.total

    def get_cash(self):
        """returns the remaining cash of this portfolio"""
        return self.cash

    def __str__(self):
        """returns the string representation of the portfolio"""
        return f"{self.user} -> {self.cash}"


class History(models.Model):
    """history model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history")
    symbol = models.CharField(max_length=7, unique=True)
    shares = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0)])
    date_transacted = models.DateTimeField(auto_now_add=True)

    histories = models.Manager()

    def get_symbol(self):
        """returns the symbol of history"""
        return self.symbol

    def get_shares(self):
        """returns the shares of history"""
        return self.shares

    def get_price(self):
        """returns the price of history"""
        return self.price

    def get_date_transacted(self):
        """returns the date_transacted of history"""
        return self.date_transacted
