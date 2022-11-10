"""dj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# 已移除，使用repath
# from django.conf.urls import url
from django.urls import re_path
from . import views,search,search2,index
from django.urls import path
from dj1 import views


urlpatterns = [
    # url(r'^$', views.hello),
    re_path(r'^search-form/$', search.search_form),
    re_path(r'^search/$', search.search),
    # path('page/',views.page2),
    # path('view/',views.hello),
    path('admin/', admin.site.urls),
    re_path(r'^search-post/$', search2.search_post),
    re_path(r'^index/$', index.inedx_page),
    re_path(r'^function_list/$', index.function_list),
    re_path(r'^function_list_plsql/$', index.function_list_plsql),
]
