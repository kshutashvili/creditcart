from django.shortcuts import render
from django.shortcuts import render
from django.urls.base import reverse
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from api.models import Rewiew, Advantage, Faq

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
    return render(
        request,
        'create_order_2.html',
        {
            'title':'Создать заказ',
            'year':datetime.now().year,
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
    return render(
        request,
        'my_booking.html',
        {
            'title':'Мои закази',
            'year':datetime.now().year,
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
    