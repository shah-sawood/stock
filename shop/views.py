"""all backend regarding shop goes here"""
import os
from django.shortcuts import render

if os.environ.get("API_KEY") is None:
    raise RuntimeError(
        "API_KEY not set\nUSAGE: export API_KEY=VALUE\nor\nUSAGE: set API_KEY=VALUE"
    )

# Create your views here.
def index(request):
    """displays the index page of the stock"""
    context = {}
    return render(request, "shop/index.html", context)


def quote(request):
    """allows a user to look up a stock’s current price"""
    context = {}
    return render(request, "shop/quote.html", context)
