"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic.base import TemplateView 

from ERPSystem import views    


from django.contrib import admin
from django.urls import re_path

from django.conf import settings

from django.conf.urls.static import static

#from django.views.static import serve  #图片显示


urlpatterns = [
     
    path("accounts/", include("accounts.urls")),  
    path("accounts/", include("django.contrib.auth.urls")),
       
    path("marketing/", include("marketing.urls")),
    path("warehouse/", include("warehouse.urls")),
    path("purchasing/", include("purchasing.urls")),
    path("production/", include("production.urls")), 
    path("calculator/", include("calculator.urls")),

    path('', include("myGallery.urls")), 
    path('', include('demo.urls')),
    
    path('admin/', admin.site.urls),  
    
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 

    path('history',views.history),

    path('main_page', views.main_page),
    path('REP_mind_map', views.REP_mind_map),
    
]  

 