"""missingKids URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from travellerinf import views
from django.conf import settings
from django.views.static import serve  # 处理静态文件
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from travellerinf.views import Vippage, logins, regist, log_out, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('regist/', views.regist, name="regist"),
    path('login/', views.logins, name="login"),
    path('vippage/', Vippage.as_view(), name='vippage'),
    #re_path(r'^vippage/(.*?)/', views.Vippage, name='vippage'),
    path('logout/', views.log_out),
    path('contactus/', ContactView.as_view(), name='contactus'),   # 接收用户留言
    path('healthcode/', views.healthcode, name="healthcode"),
    path('travelcode/', views.travelcode, name="travelcode"),
    path('travelguide/', views.travelguide, name="travelguide"),
    path('pcs/', views.pcs, name="pcs"),
    path('chpolicy/', views.chpolicy, name="chpolicy"),
    path('auspolicy/', views.auspolicy, name="auspolicy"),
]


if settings.DEBUG:
    #  配置静态文件访问处理
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))



