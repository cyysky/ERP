from django.urls import path
from marketing import views 

urlpatterns = [
#-------------------------------------------------------------------------sales
    path('sales',views.sales),  
    path('edit_sales/<int:sales_id>', views.edit_sales),
    path('emp_sales', views.emp_sales),
    path('update_sales/<int:sales_id>', views.update_sales),   
    path('delete_sales/<int:sales_id>', views.destroy_sales),
#-------------------------------------------------------------------------customer    
    path('customer',views.customer),
    path('edit_customer/<int:customer_id>', views.edit_customer),
    path('emp_customer', views.emp_customer),
    path('update_customer/<int:customer_id>', views.update_customer),
    path('delete_customer/<int:customer_id>', views.destroy_customer),
#--------------------------------------------------------------------------project
    path('project',views.project),
    path('edit_project/<int:project_id>', views.edit_project),
    path('emp_project', views.emp_project),
    path('update_project/<int:project_id>', views.update_project),
    path('delete_project/<int:project_id>', views.destroy_project),
#----------------------------------------------------------------------------bom
    path('bom',views.bom),
    path('edit_bom/<int:id>', views.edit_bom),
    path('emp_bom', views.emp_bom),
    path('update_bom/<int:id>', views.update_bom),
    path('delete_bom/<int:id>', views.destroy_bom),

#---------------------------------------------------------------------------supplier    
    path('supplier',views.supplier),  
    path('edit_supplier/<int:supplier_id>', views.edit_supplier),
    path('emp_supplier', views.emp_supplier),
    path('update_supplier/<int:supplier_id>', views.update_supplier),   
    path('delete_supplier/<int:supplier_id>', views.destroy_supplier),

]