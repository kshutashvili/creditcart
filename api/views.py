from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponseServerError
from api.models import CreditCardUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from datetime import datetime
from .models import CreditCardUser, CreditRequest
from urllib.parse import urlparse

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
    assert isinstance(request, HttpRequest)                                                                                                                       
    if request.method == 'POST':    
        user = authenticate(email=request.POST.get('login'), password=request.POST.get('pass'))   
        response_data = {}                                                                              
        if user != None:             
            user_login(request, user)              
            return JsonResponse({"Result":"Success"})
        else:
            return JsonResponse({"Result":"Login Error"})

def update_user_info(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        try:
            #Update users info for credit
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            second_name = request.POST.get('second_name')
            inn = request.POST.get('inn')
            passport_code = request.POST.get('passport_code')
            passport_number = request.POST.get('passport_number')
            birth_date = datetime(int(request.POST.get('date_year')), 
                                int(request.POST.get('date_month')), 
                                int(request.POST.get('date_day')),)
            user = CreditCardUser.objects.get(email = request.user.email)
            user.first_name = first_name
            user.second_name = second_name
            user.middle_name = middle_name
            user.inn = inn
            user.passport_code = passport_code
            user.passport_number = passport_number
            user.birth_date = birth_date
            user.save()
            #Creating request for credit
            goods_link = request.POST.get('goods_link')
            credit_request = CreditRequest(user = request.user,requested_good = goods_link, sellers_shop = urlparse(goods_link).netloc)
            credit_request.save()
            return redirect('my_booking')
        except Exception as ex:
            return HttpResponseServerError(ex)
