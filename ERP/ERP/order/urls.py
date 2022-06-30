from django.urls import path, include

from order import views 

urlpatterns = [

#-------------------------------------------------------sales
    path('sales',views.sales),  
    path('edit_sales/<int:sales_id>', views.edit_sales),
    path('emp_sales', views.emp_sales),
    path('update_sales/<int:sales_id>', views.update_sales),   
    path('delete_sales/<int:sales_id>', views.destroy_sales),
#----------------------------------------------------customer    
    path('customer',views.customer),
    path('edit_customer/<int:customer_id>', views.edit_customer),
    path('emp_customer', views.emp_customer),
    path('update_customer/<int:customer_id>', views.update_customer),
    path('delete_customer/<int:customer_id>', views.destroy_customer),
#-----------------------------------------------------supplier    
    path('supplier',views.supplier),  
    path('edit_supplier/<int:supplier_id>', views.edit_supplier),
    path('emp_supplier', views.emp_supplier),
    path('update_supplier/<int:supplier_id>', views.update_supplier),   
    path('delete_supplier/<int:supplier_id>', views.destroy_supplier),

#----------------------------------------------------Machine    
    path('machine',views.machine),
    path('edit_machine/<int:machine_id>', views.edit_machine),
    path('emp_machine', views.emp_machine),
    path('update_machine/<int:machine_id>', views.update_machine),    
    path('delete_machine/<int:machine_id>', views.destroy_machine),
#----------------------------------------------------Material    
    path('material',views.material),
    path('edit_material/<int:material_id>', views.edit_material),
    path('emp_material', views.emp_material),
    path('update_material/<int:material_id>', views.update_material),    
    path('delete_material/<int:material_id>', views.destroy_material),
#----------------------------------------------------Material_Location    
    path('material_location',views.material_location),
    path('edit_material_location/<int:material_location_id>', views.edit_material_location),
    path('emp_material_location', views.emp_material_location),
    path('update_material_location/<int:material_location_id>', views.update_material_location),    
    path('delete_material_location/<int:material_location_id>', views.destroy_material_location),
#----------------------------------------------------Material_Supplier    
    path('material_supplier',views.material_supplier),
    path('edit_material_supplier/<int:id>', views.edit_material_supplier),
    path('emp_material_supplier', views.emp_material_supplier),
    path('update_material_supplier/<int:id>', views.update_material_supplier),    
    path('delete_material_supplier/<int:id>', views.destroy_material_supplier),
     
#----------------------------------------------------process    
    path('process',views.process),
    path('edit_process/<int:process_id>', views.edit_process),
    path('emp_process', views.emp_process),
    path('update_process/<int:process_id>', views.update_process),
    path('delete_process/<int:process_id>', views.destroy_process),
#----------------------------------------------------product    
    path('product',views.product),
    path('edit_product/<int:product_id>', views.edit_product),
    path('emp_product', views.emp_product),
    path('update_product/<int:product_id>', views.update_product),
    path('delete_product/<int:product_id>', views.destroy_product),
#----------------------------------------------------product_good    
    path('product_good',views.product_good),
    path('edit_product_good/<int:product_good_id>', views.edit_product_good),
    path('emp_product_good', views.emp_product_good),
    path('update_product_good/<int:product_good_id>', views.update_product_good),
    path('delete_product_good/<int:product_good_id>', views.destroy_product_good),
#----------------------------------------------------product_material    
    path('product_material',views.product_material),
    path('edit_product_material/<int:product_material_id>', views.edit_product_material),
    path('emp_product_material', views.emp_product_material),
    path('update_product_material/<int:product_material_id>', views.update_product_material),
    path('delete_product_material/<int:product_material_id>', views.destroy_product_material),
#----------------------------------------------------product_reject    
    path('product_reject',views.product_reject),
    path('edit_product_reject/<int:id>', views.edit_product_reject),
    path('emp_product_reject', views.emp_product_reject),
    path('update_product_reject/<int:id>', views.update_product_reject),
    path('delete_product_reject/<int:id>', views.destroy_product_reject),
#----------------------------------------------------product_reject    
    path('product_reject',views.product_reject),
    path('edit_product_reject/<int:id>', views.edit_product_reject),
    path('emp_product_reject', views.emp_product_reject),
    path('update_product_material/<int:id>', views.update_product_material),
    path('delete_product_material/<int:id>', views.destroy_product_material),
#-------------------------------------------------------------------------------------project

    path('project',views.project),
    path('edit_project/<int:id>', views.edit_project),
    path('emp_project', views.emp_project),
    path('update_project/<int:id>', views.update_project),
    path('delete_project/<int:id>', views.destroy_project),

#-----------------------------------------------------------------------------------bom

    path('bom',views.bom),
    path('edit_bom/<int:id>', views.edit_bom),
    path('emp_bom', views.emp_bom),
    path('update_bom/<int:id>', views.update_bom),
    path('delete_bom/<int:id>', views.destroy_bom),

#-------------------------------------------------------------------------------

    path('delivery',views.delivery),
    path('edit_delivery/<int:id>', views.edit_delivery),
    path('emp_delivery', views.emp_delivery),
    path('update_delivery/<int:id>', views.update_delivery),
    path('delete_delivery/<int:id>', views.destroy_delivery),

#----------------------------------------------------------------------------------

    path('packaging',views.packaging),
    path('edit_packaging/<int:id>', views.edit_packaging),
    path('emp_packaging', views.emp_packaging),
    path('update_packaging/<int:id>', views.update_packaging),
    path('delete_packaging/<int:id>', views.destroy_packaging),

#-------------------------------------------------------------------------------------


]