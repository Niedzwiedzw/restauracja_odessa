"""restauracjaodessa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from odessaapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^strona-w-budowie$', views.site_maintenence, name='maintenence'),
    url('^kontakt$', views.contact_us, name='contact_us'),
    url('^dzis$', views.daily_dish, name='daily_dish'),
    url('^dzis/add$', views.add_dish, name='add_dish'),
    url('^change_dish/(?P<dish_id>\d+)', views.change_dish, name='change_dish'),
]
