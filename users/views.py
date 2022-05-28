from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import CustomUser


@csrf_exempt
def register_user(request):
    logout(request)
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        CustomUser.objects.create_user(email=email, password=password)
        return redirect("login")
    return render(request, "signup.html")


@csrf_exempt
def login_user(request):
    logout(request)
    context = {}
    username = password = ""
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            context = {"wrong_auth_cred": True}
    return render(request, "registration/login.html", context)


@csrf_exempt
@login_required
def logout_user(request):
    logout(request)
    return redirect("login")
