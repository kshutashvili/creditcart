from django.shortcuts import render
from django.shortcuts import render
from django.urls.base import reverse
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime, timedelta
from api.models import Rewiew, Advantage, Faq, CreditRequest
from django.contrib.auth.decorators import login_required
from .goods_parcer import *
import main_app.goods_parcer
from pytz import timezone, utc, tzinfo
import pytz
from creditcard import settings

# Create your views here.

def apple(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'apple.html',
        {
            'title':'Карточка товара',
            'year':datetime.now().year,
        }
    )

def application_accepted(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'application_accepted.html',
        {
            'title':'Ваша заявка на покупку товара в кредит принята',
            'year':datetime.now().year,
        }
    )
def application_not_accepted(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'application_not_accepted.html',
        {
            'title':'Ваша заявка не одобрена',
            'year':datetime.now().year,
        }
    )

def catalog(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'catalog.html',
        {
            'title':'Каталог товаров',
            'year':datetime.now().year,
        }
    )

def contacts(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contacts.html',
        {
            'title':'Контакты',
            'year':datetime.now().year,
        }
    )

def create_order(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'create_order.html',
        {
            'title':'Создать заказ',
            'year':datetime.now().year,
        }
    )

def create_order_2(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return render(request, 'not_logined.html')
    goods_link = request.POST.get('links')
    good = getGoodFromSite(goods_link)
    print(request.POST.get('links'))
    return render(
        request,
        'create_order_2.html',
        {
            'title' : 'Создать заказ',
            'good': good, 
            'goods_link': goods_link,
        }
    )

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    r = Rewiew.objects.all()[0]
    return render(
        request,
        'index.html',
        {
            'title': 'Главная страница',
            'year': datetime.now().year,
            'reviews' : Rewiew.objects.all()[:10],
            'advantages' : Advantage.objects.all()[:10],
            'faques' : Faq.objects.all()[:10],
        }
    )

def instruction(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'instruction.html',
        {
            'title':'Как это работает?',
            'year':datetime.now().year,
        }
    )

def my_booking(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    requests = CreditRequest.objects.filter(user = request.user)
    all = []
    timer = True
    min = 0
    sec = 0
    for r in requests:
        time_past = (datetime.now().replace(tzinfo=None) - 
                    r.date_time_requested.astimezone(pytz.timezone(settings.TIME_ZONE)).replace(tzinfo=None))
        if (int(time_past.total_seconds()/60)>30):
            timer = False
        else:
            timer = True
            dif = 1800 - time_past.total_seconds()
            min = int(dif/60)
            sec = int(dif - min*60)
        all.append({"good":getGoodFromSite(r.requested_good), 
                    "request":r, 
                    "timer": timer,
                    "minutes_left":min,
                    "seconds_left":sec, 
                    "is_accepted":False,
                    })

    return render(
        request,
        'my_booking.html',
        {
            'title':'Мои закази',
            'year':datetime.now().year,
            'bids':all

        }
    )

def my_credits(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'my_credits.html',
        {
            'title':'Мои кредиты'
        }
    )

def page_credit(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'page_credit.html',
        {
            'title':'Мои кредиты',
            'year':datetime.now().year,
        }
    )

def personal_area(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'personal_area.html',
        {
            'title':'Личный кабинет',
            'year':datetime.now().year,
        }
    )

def text(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'text.html',
        {
            'title':'Текстовая страница',
            'year':datetime.now().year,
        }
    )
    