"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to url patterns:  path('', views.home, name='home')
Class-based viewsssA
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
#from django.urls import re_path

from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),  
    path("accounts/", include("accounts.urls")),  
    path("accounts/", include("django.contrib.auth.urls")),
       
    path("product_quotation_detail/", include("product_quotation_detail.urls")),
    path("project_management/", include("project_management.urls")),
    path("production_product/", include("production_product.urls")),
    path("product_inspection/", include("product_inspection.urls")),
    path("company_information/", include("company_information.urls")),
    path("inventory_management/", include("inventory_management.urls")),
    path("purchasing_material/", include("purchasing_material.urls")),

    path('update_to_process/<str:RequireID>/<str:BOMID>/<str:ProjectSalesItemID>/<str:MaterialID>',views.update_to_require),
    path('update_to_require/<str:RequireID>/<str:BOMID>/<str:ProjectSalesItemID>/<str:MaterialID>',views.update_to_require),
    path('update_to_purchase/<str:PurchaseID>/<str:RequireID>',views.update_to_purchase), 

    path('', include("myGallery.urls")), 
    path('', include('demo.urls')),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),  

    path('history',views.history),

    #------------------------------------------------------------------------------------------------------------------
    path('Progress_Table', views.Progress_Table),
    path('product_quotation_detail', views.product_quotation_detail),#project_sales_item,customer,seles,product,process,material
    

    path('edit_product_quotation/<str:id>', views.edit_product_quotation),
    path('emp_product_quotation', views.emp_product_quotation),
    path('update_product_quotation/<str:id>', views.update_product_quotation),
    path('delete_product_quotation', views.destroy_product_quotation),


    path('edit_product_quotation_detail_process/<str:id>', views.edit_product_quotation_detail_process),
    path('emp_product_quotation_detail_process', views.emp_product_quotation_detail_process),
    path('update_product_quotation_detail_process/<str:id>', views.update_product_quotation_detail_process),
    path('delete_product_quotation_detail_process', views.destroy_product_quotation_detail_process),
  

    path('edit_product_quotation_detail_material/<str:id>', views.edit_product_quotation_detail_material),
    path('emp_product_quotation_detail_material', views.emp_product_quotation_detail_material),
    path('update_product_quotation_detail_material/<str:id>', views.update_product_quotation_detail_material),
    path('delete_product_quotation_detail_material', views.destroy_product_quotation_detail_material),


    path('Product_Quotation_Grand/', views.Grand_Total),
    path('delete_Product_Quotation_Grand/', views.destroy_product_quotation_detail),

    #---------------------------------------------------------------------------------
    path('qq', views.qq),

    path('zz', views.zz),
    #--------------------------------------------------------------------------------------------------------------------

    path('REP_mind_map', views.REP_mind_map),

    path('Website_Layout_Test',views.Website_Layout_Test),
   
]  

 