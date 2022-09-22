"""all custom filters for shop goes here"""
from django import template

register = template.Library()


@register.filter
def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


@register.filter
def multiply(value, arg):
    """multiplies first value by second value"""
    return value * arg


@register.filter
def subtract(value, arg):
    """subtracts second value from first value"""
    return value - arg
