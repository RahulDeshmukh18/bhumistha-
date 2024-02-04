# urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import index
from .views  import casestudy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('casestudy/', casestudy, name='casestudy'),
]

# Serve media files during development

