from django.urls import path
from. import views 

urlpatterns = [
#-------------------------------------------------------------------------employee
    path('employee',views.employee),
    path('edit_employee/<str:EmployeeID>', views.edit_employee),
    path('emp_employee', views.emp_employee),
    path('update_employee/<str:EmployeeID>', views.update_employee),
    path('delete_employee/<str:EmployeeID>', views.destroy_employee),
#-------------------------------------------------------------------------customer    
    path('customer',views.customer),
    path('edit_customer/<str:CustomerID>', views.edit_customer),
    path('emp_customer', views.emp_customer),
    path('update_customer/<str:CustomerID>', views.update_customer),
    path('delete_customer/<str:CustomerID>', views.destroy_customer),
#--------------------------------------------------------------------------product    
    path('product',views.product),
    path('edit_product/<str:ProductID>', views.edit_product),
    path('emp_product', views.emp_product),
    path('update_product/<str:ProductID>', views.update_product),
    path('delete_product/<str:ProductID>', views.destroy_product),
#------------------------------------------------------------------------supplier  
    path('supplier',views.supplier),
    path('edit_supplier/<str:SupplierID>', views.edit_supplier),
    path('emp_supplier', views.emp_supplier),
    path('update_supplier/<str:SupplierID>', views.update_supplier),
    path('delete_supplier/<str:SupplierID>', views.destroy_supplier),
#-------------------------------------------------------------------------------------------
    path('multi_table_view_company_information', views.multi_table_view_company_information),
]