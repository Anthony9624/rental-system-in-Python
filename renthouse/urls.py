"""renthouse URL Configuration

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
from django.urls import re_path
from house import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login$', views.loginSystem),  # 调用登录url；
    re_path(r'^main$', views.mainPageSystem),
    re_path(r'^register', views.registerSystem),  # 注册
    re_path(r'^sell', views.sell),  # 注册
    re_path(r'^rent', views.rent),  # 注册
    re_path(r'^sell', views.analyze),
    # re_path(r'^show_some/$', views.show_some),
    re_path(r'^sumbmitdone/$', views.sell_gain),
    # re_path(r'^search/$',views.search),
    # re_path(r'^screen/$',views.screen)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
