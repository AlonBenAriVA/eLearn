"""vids URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from learn import views

urlpatterns = [
    
    url(r'^learn/$', views.home, name = 'home'),
    url(r'^learn/(?P<pk>\d+)/$', views.get_discussion, name = 'get_discussion'),
    url(r'^thread/(?P<subject_id>\d+)/$', views.get_thread, name = 'get_thread'),
    url(r'^thread/(?P<subject_id>\d+)/add_comment$', views.add_comment, name = 'add_comment'),
    url(r'^learn/(?P<pk>\d+)/new_topic/$', views.new_topic,name = 'new_topic'),
    url('admin/', admin.site.urls),
]
