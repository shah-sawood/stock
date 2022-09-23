"""all backend regarding shop goes here"""
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from shop.utils import lookup
from django.db.models import Sum
from django.db import IntegrityError

from .models import History, Purchase, Portfolio

if os.environ.get("API_KEY") is None:
    raise RuntimeError(
        "API_KEY not set\nUSAGE: export API_KEY=VALUE\nor\nUSAGE: set API_KEY=VALUE"
    )

# Create your views here.
@login_required
def index(request):
    """displays the index page of the stock"""
    context = {}
    context["purchases"] = Purchase.purchases.filter(user=request.user).order_by("-id")
    return render(request, "shop/index.html", context)


@login_required
def quote(request):
    """allows a user to look up a stock’s current price"""
    context = {}
    context["title"] = "quote"
    if request.method == "POST":
        symbol = request.POST.get("symbol")
        if not symbol:
            messages.error(request, "Please provide an alphabetic symbol.")
        else:
            data = lookup(symbol)
            if data is not None:
                context["data"] = data
                return render(request, "shop/quoted.html", context)
            messages.error(request, "Invalid symbol")
    return render(request, "shop/quote.html", context)


@login_required
def buy(request):
    """buys shares of some symbol"""
    context = {"title": "buy"}
    if request.method == "POST":
        symbol = request.POST.get("symbol")
        shares = request.POST.get("shares")
        if not symbol:
            messages.error(request, "Missing symbol.")
        elif not shares:
            messages.error(request, "Missing shares.")
        else:
            data = lookup(symbol)
            if data is not None:
                try:
                    total = int(shares) * data.get("price")
                    portfolio = Portfolio.objects.get(user=request.user)
                    cash = portfolio.get_cash()

                    if total > cash:
                        messages.error(
                            request,
                            "You have insufficient cash for this transaction to perform",
                        )
                    else:
                        purchase = Purchase.purchases.create(
                            user=request.user,
                            symbol=symbol,
                            name=data.get("name"),
                            shares=shares,
                            price=data.get("price"),
                        )
                except IntegrityError:
                    purchase = Purchase.purchases.select_for_update().get(
                        user=request.user, symbol=symbol
                    )
                    portfolio.cash -= total
                    portfolio.save()
                    purchase.shares += int(shares)
                    purchase.save()
                return HttpResponseRedirect(reverse("shop:index"))
            messages.error(request, "Something went wrong. Please try again later.")

    symbol = request.GET.get("symbol")
    if symbol is not None:
        data = lookup(symbol)
        if data is not None:
            context["data"] = data
    return render(request, "shop/buy.html", context)


def history(request):
    """returns the transactions history of current user"""
    context = {}
    context["title"] = "history"
    context["histories"] = History.histories.filter(user=request.user).order_by("-id")
    return render(request, "shop/history.html", context)
