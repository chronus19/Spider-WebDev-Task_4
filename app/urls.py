"""bulletin_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include

from . import views

urlpatterns = [
    url(r'^register/',views.register),
    url(r'^login/',views.login),
    url(r'^logout/',views.logout),
    url(r'^dashboard/',views.dashboard),
    url(r'^add_post/$',views.add_post),
    url(r'^delete_post/$',views.delete_post),
    url(r'^admin_panel/$',views.admin_panel),
    url(r'^update_access_level/$',views.update_access_level),
    url(r'^',views.login),
]
