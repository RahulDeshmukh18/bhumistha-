# urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import index
from .views  import casestudy, careers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('casestudy/', casestudy, name='casestudy'),
    path('careers/', careers, name='careers'),
]

# Serve media files during development

