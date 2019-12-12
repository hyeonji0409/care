from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('account/',include('account.urls')),
]
