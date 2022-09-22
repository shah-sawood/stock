"""docstring for views.py"""
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
# from django.contrib.auth.password_validation import MinimumLengthValidator
# from django.contrib.auth.password_validation import CommonPasswordValidator
# from django.contrib.auth.password_validation import NumericPasswordValidator

# Create your views here.
def login_user(request):
    """logs a user in"""
    context = {}
    context["title"] = "login"

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        print(user, username, password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("shop:index"))
        messages.error(request, "Invalid credentials")
    return render(request, "user/login.html", context)


def logout_user(request):
    """logs a user out"""
    logout(request)
    return HttpResponseRedirect(reverse("shop:index"))


def register_user(request):
    """registers a user"""
    context = {}
    context["title"] = "register"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")

        if not username:
            messages.error(request, "Username can't be empty.")
        elif not (password or confirmation):
            messages.error(request, "Password(s) can't be empty.")
        elif password != confirmation:
            messages.error(request, "Passwords must match.")
        else:
            try:
                user = User.objects.create(username=username, password=password)
            except IntegrityError:
                messages.error(request, "Username already taken.")
            else:
                login(request, user)
                messages.success(request, "Registered successfully.")
                return HttpResponseRedirect(reverse("shop:index"))
    return render(request, "user/register.html", context)
