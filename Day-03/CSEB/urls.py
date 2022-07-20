"""CSEB URL Configuration

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
from django.urls import path
from gistapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.demo),
    path('b/<str:cge>/',views.demo1),
    path('v/<str:en>/<int:ea>/',views.trail),
    path('s/<str:name>/<str:dept>/<int:sno>/<int:marks>/',views.student),
    path('d/<int:r>/',views.ran),
    path('rt/<str:empname>/',views.edetails),
    path("pm/<str:j>/<int:a>/",views.fg),
    path('m/',views.gh),
    path('mt/<str:n>/',views.ghp),
    path('a/<str:deptname>/<int:deptno>/',views.g),
    path('p/<str:ename>/<int:eno>/<str:loc>/',views.ph),
]
