"""BigV_project URL Configuration

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
from BigV_app_map.views import home,formulario,sobre_map,vertentes_map

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name = 'url_home'),
    path('formulario/', formulario,name = 'url_formulario'),
    path('sobre_map/', sobre_map,name = 'url_sobre_map'),
    path('vertentes_map/', vertentes_map,name = 'url_vertente_map')

]
