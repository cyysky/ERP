from django.urls import path

from production import views 

urlpatterns = [
#----------------------------------------------------process    
    path('process',views.process),
    path('edit_process/<str:ProcessID>', views.edit_process),
    path('emp_process', views.emp_process),
    path('update_process/<str:ProcessID>', views.update_process),
    path('delete_process/<str:ProcessID>', views.destroy_process),
#----------------------------------------------------Machine    
    path('machine',views.machine),
    path('edit_machine/<str:MachineID>', views.edit_machine),
    path('emp_machine', views.emp_machine),
    path('update_machine/<str:MachineID>', views.update_machine),    
    path('delete_machine/<str:MachineID>', views.destroy_machine),
#----------------------------------------------------product    
    path('product',views.product),
    path('edit_product/<str:ProductID>', views.edit_product),
    path('emp_product', views.emp_product),
    path('update_product/<str:ProductID>', views.update_product),
    path('delete_product/<str:ProductID>', views.destroy_product),
#----------------------------------------------------product_good    
    path('product_good',views.product_good),
    path('edit_product_good/<str:GoodbatchID>', views.edit_product_good),
    path('emp_product_good', views.emp_product_good),
    path('update_product_good/<str:GoodbatchID>', views.update_product_good),
    path('delete_product_good/<str:GoodbatchID>', views.destroy_product_good),
#----------------------------------------------------product_reject    
    path('product_reject',views.product_reject),
    path('edit_product_reject/<str:RejectbatchID>', views.edit_product_reject),
    path('emp_product_reject', views.emp_product_reject),
    path('update_product_reject/<str:RejectbatchID>', views.update_product_reject),
    path('delete_product_reject/<str:RejectbatchID>', views.destroy_product_reject),   
#----------------------------------------------------product_material    
    path('product_material',views.product_material),
    path('edit_product_material/<str:product_material_id>', views.edit_product_material),
    path('emp_product_material', views.emp_product_material),
    path('update_product_material/<str:product_material_id>', views.update_product_material),
    path('delete_product_material/<str:product_material_id>', views.destroy_product_material), 
#----------------------------------------------------------packaging
    path('packaging',views.packaging),
    path('edit_packaging/<str:PackagingID>', views.edit_packaging),
    path('emp_packaging', views.emp_packaging),
    path('update_packaging/<str:PackagingID>', views.update_packaging),
    path('delete_packaging/<str:PackagingID>', views.destroy_packaging),    
#---------------------------------------------------------deliver
    path('delivery',views.delivery),
    path('edit_delivery/<str:DeliveryID>', views.edit_delivery),
    path('emp_delivery', views.emp_delivery),
    path('update_delivery/<str:DeliveryID>', views.update_delivery),
    path('delete_delivery/<str:DeliveryID>', views.destroy_delivery),   

#---------------------------------------------------------resource
    path('resource',views.resource),
    path('edit_resource/<str:ResourceID>', views.edit_resource),
    path('emp_resource', views.emp_resource),
    path('update_resource/<str:ResourceID>', views.update_resource),
    path('delete_resource/<str:ResourceID>', views.destroy_resource),   


]