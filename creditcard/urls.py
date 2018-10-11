from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main_app import views as main_app_views
from main_app import urls as main_app_urls
from api import urls as api_urls
from django.contrib import admin

urlpatterns = [
    path('', include(main_app_urls)),
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
