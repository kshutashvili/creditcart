"""creditcard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main_app import views as main_app_views

urlpatterns = [
    path('apple', main_app_views.apple),
    path('application_accepted', main_app_views.application_accepted),
    path('application_not_accepted', main_app_views.application_not_accepted),
    path('catalog', main_app_views.catalog),
    path('contacts', main_app_views.contacts),
    path('create_order', main_app_views.create_order),
    path('create_order_2', main_app_views.create_order_2),
    path('index', main_app_views.index),
    path('', main_app_views.index),
    path('instruction', main_app_views.instruction),
    path('my_booking', main_app_views.my_booking, name = 'my_booking'),
    path('my_credits', main_app_views.my_credits),
    path('page_credit', main_app_views.page_credit),
    path('personal_area', main_app_views.personal_area, name='personal_area'),
    path('text', main_app_views.text),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
