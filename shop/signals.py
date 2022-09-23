"""signals"""
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from shop.models import History, Purchase, Portfolio


@receiver(post_save, sender=User)
def create_portfolio(sender, instance, created, **kwargs):
    """creates a portfolio for a newly registered user"""
    if created:
        Portfolio.objects.create(
            user=instance,
            cash=10000,
            total=10000,
        )


@receiver(post_save, sender=Purchase)
def add_history(sender, instance, created, **kwargs):
    """adds current purchase to history"""
    if created:
        History.histories.create(
            user=instance.get_purchaser(),
            symbol=instance.get_symbol(),
            shares=instance.get_shares(),
            price=instance.get_price(),
        )
