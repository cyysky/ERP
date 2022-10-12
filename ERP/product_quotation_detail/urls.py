from django.urls import path
from. import views 

urlpatterns = [

    path('marketing_order',views.marketing_order), 
    
#-------------------------------------------------------------------------sales_order
    path('sales_order',views.sales_order),  
    path('edit_sales_order/<str:SalesOrderID>', views.edit_sales_order),
    path('emp_sales_order', views.emp_sales_order),
    path('update_sales_order/<str:SalesOrderID>', views.update_sales_order),   
    path('delete_sales_order/<str:SalesOrderID>', views.destroy_sales_order),
#-----------------------------------------------------------------------------
    path('product_sales_records',views.product_sales_records),  

]