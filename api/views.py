from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponseServerError
from api.models import CreditCardUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as user_login
from datetime import datetime

# Create your views here.

def create_user(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    username = request.POST.get('username')
    email = request.POST.get('mail')
    duble_pass = request.POST.get('duble_pass')
    pas = request.POST.get('pass')
    try:
        user = CreditCardUser.objects.create_user(username = username, email = email, password = pas)
        user.is_staff = True
        user.is_active = True
        user.save()
    except Exception as e:
        return JsonResponse({"Status":"Fail", "Reason":str(e)})
    return redirect('personal_area')

def login(request):                                                                                                                         
    if request.method == 'POST':    
        user = authenticate(email=request.POST.get('login'), password=request.POST.get('pass'))   
        response_data = {}                                                                              
        if user != None:             
            user_login(request, user)              
            return JsonResponse({"Result":"Success"})
        else:
            return JsonResponse({"Result":"Login Error"})
