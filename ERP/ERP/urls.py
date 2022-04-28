"""ERP URL Configuration

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

from Master import views  
from employee import views as eviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    
    path('emp', eviews.emp),  
    path('show',eviews.show, name="employee"),  
    path('edit/<int:id>', eviews.edit),  
    path('update/<int:id>', eviews.update),  
    path('delete/<int:id>', eviews.destroy),  
    path('export_pdf/<int:id>', eviews.export_pdf),
    #path('emp', views.emp),
    path('emp1', views.emp1, name="supplier"),
    path('emp2', views.emp2, name="customer"),
    path('emp3', views.emp3, name="material"),
    path('sub_contract',views.sub_contract),  
    path('supplier',views.supplier),  
    path('customer',views.customer),
    path('material',views.material),
    #path('edit/<int:id>', views.edit),  
    path('edit1/<int:id>', views.edit1),
    path('edit2/<int:id>', views.edit2),
    path('edit3/<int:id>', views.edit3),
    #path('update/<int:id>', views.update),
    path('update1/<int:id>', views.update1),  
    path('update2/<int:id>', views.update2),
    path('update3/<int:id>', views.update3),
    #path('delete/<int:id>', views.destroy), 
    path('delete1/<int:id>', views.destroy1), 
    path('delete2/<int:id>', views.destroy2),
    path('delete3/<int:id>', views.destroy3), 
]
