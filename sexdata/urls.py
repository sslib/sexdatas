"""sexdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.index),
    url(r'^qb/', view.qb),
    url(r'^sa/', view.sa),
    url(r'^signup/', view.signup),
    url(r'^signin/', view.signin),
    url(r'^search/', view.search),
    url(r'^actress/', view.actress),
    url(r'^firm/', view.firm),
    url(r'^sort/', view.sort),
    url(r'^sale/', view.sale),
    url(r'^rank/', view.rank),
    url(r'^api/', view.api)
]
