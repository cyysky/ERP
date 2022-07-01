from django.urls import path

from production import views 

urlpatterns = [
#----------------------------------------------------process    
    path('process',views.process),
    path('edit_process/<int:process_id>', views.edit_process),
    path('emp_process', views.emp_process),
    path('update_process/<int:process_id>', views.update_process),
    path('delete_process/<int:process_id>', views.destroy_process),
#----------------------------------------------------Machine    
    path('machine',views.machine),
    path('edit_machine/<int:machine_id>', views.edit_machine),
    path('emp_machine', views.emp_machine),
    path('update_machine/<int:machine_id>', views.update_machine),    
    path('delete_machine/<int:machine_id>', views.destroy_machine),
#----------------------------------------------------product    
    path('product',views.product),
    path('edit_product/<int:product_id>', views.edit_product),
    path('emp_product', views.emp_product),
    path('update_product/<int:product_id>', views.update_product),
    path('delete_product/<int:product_id>', views.destroy_product),
#----------------------------------------------------product_good    
    path('product_good',views.product_good),
    path('edit_product_good/<int:goodbatch_id>', views.edit_product_good),
    path('emp_product_good', views.emp_product_good),
    path('update_product_good/<int:goodbatch_id>', views.update_product_good),
    path('delete_product_good/<int:goodbatch_id>', views.destroy_product_good),
#----------------------------------------------------product_reject    
    path('product_reject',views.product_reject),
    path('edit_product_reject/<int:rejectbatch_id>', views.edit_product_reject),
    path('emp_product_reject', views.emp_product_reject),
    path('update_product_reject/<int:rejectbatch_id>', views.update_product_reject),
    path('delete_product_reject/<int:rejectbatch_id>', views.destroy_product_reject),   
#----------------------------------------------------product_material    
    path('product_material',views.product_material),
    path('edit_product_material/<int:product_material_id>', views.edit_product_material),
    path('emp_product_material', views.emp_product_material),
    path('update_product_material/<int:product_material_id>', views.update_product_material),
    path('delete_product_material/<int:product_material_id>', views.destroy_product_material), 
#----------------------------------------------------------packaging
    path('packaging',views.packaging),
    path('edit_packaging/<int:id>', views.edit_packaging),
    path('emp_packaging', views.emp_packaging),
    path('update_packaging/<int:id>', views.update_packaging),
    path('delete_packaging/<int:id>', views.destroy_packaging),    
#---------------------------------------------------------deliver
    path('delivery',views.delivery),
    path('edit_delivery/<int:id>', views.edit_delivery),
    path('emp_delivery', views.emp_delivery),
    path('update_delivery/<int:id>', views.update_delivery),
    path('delete_delivery/<int:id>', views.destroy_delivery),
#-------------------------------------------------------------------------------------


]