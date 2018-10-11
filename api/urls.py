from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from api import views as api_views

urlpatterns = [
    path('registrate', api_views.create_user),
    path('login', api_views.login, name = 'login'),
    path('update_user_info', api_views.update_user_info, name = 'update_user_info'),
]
