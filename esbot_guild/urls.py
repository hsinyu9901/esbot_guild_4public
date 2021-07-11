"""esbot_guild URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import url
from esapp import views, botviews
#from module import data

urlpatterns = [
    # 本機網址 http://127.0.0.1:8000/admin
    # 上線網址 domain網址/admin
    path('admin/', admin.site.urls),
    path('', include('esapp.urls')),
    path('liff/', botviews.test_getprofile, name="liff"),
    #url(r'^網址/$', 檔名.函式名稱),
    #    url(r'^trip/$', data.list_tripline),
    # url(r'^producer/index/$',views.index),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
