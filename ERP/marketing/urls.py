from django.urls import path
from marketing import views 

urlpatterns = [
#-------------------------------------------------------------------------sales
    path('sales',views.sales),  
    path('edit_sales/<str:SalesID>', views.edit_sales),
    path('emp_sales', views.emp_sales),
    path('update_sales/<str:SalesID>', views.update_sales),   
    path('delete_sales/<str:SalesID>', views.destroy_sales),
#-------------------------------------------------------------------------customer    
    path('customer',views.customer),
    path('edit_customer/<str:CustomerID>', views.edit_customer),
    path('emp_customer', views.emp_customer),
    path('update_customer/<str:CustomerID>', views.update_customer),
    path('delete_customer/<str:CustomerID>', views.destroy_customer),
#--------------------------------------------------------------------------project
    path('project',views.project),
    path('edit_project/<str:ProjectID>', views.edit_project),
    path('emp_project', views.emp_project),
    path('update_project/<str:ProjectID>', views.update_project),
    path('delete_project/<str:PROJECTID>', views.destroy_project),
#----------------------------------------------------------------------------bom
    path('bom',views.bom),
    path('edit_bom/<str:BOMID>', views.edit_bom),
    path('emp_bom', views.emp_bom),
    path('update_bom/<str:BOMID>', views.update_bom),
    path('delete_bom/<str:BOMID>', views.destroy_bom),


]