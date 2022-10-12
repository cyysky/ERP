from django.urls import path
from. import views 

urlpatterns = [
    #---------------------------------------------------------bom
    path('bom',views.bom),
    path('edit_bom/<str:BOMID>', views.edit_bom),
    path('emp_bom', views.emp_bom),
    path('update_bom/<str:BOMID>', views.update_bom),
    path('delete_bom/<str:BOMID>', views.destroy_bom),
    path('update_bom_to_require/<str:BOMID>', views.update_bom_to_require),
    #---------------------------------------------------------process    
    path('process',views.process),
    path('edit_process/<str:ProcessID>', views.edit_process),
    path('emp_process', views.emp_process),
    path('update_process/<str:ProcessID>', views.update_process),
    path('delete_process/<str:ProcessID>', views.destroy_process),
    #---------------------------------------------------------resource
    path('resource',views.resource),
    path('edit_resource/<str:ResourceID>', views.edit_resource),
    path('emp_resource', views.emp_resource),
    path('update_resource/<str:ResourceID>', views.update_resource),
    path('delete_resource/<str:ResourceID>', views.destroy_resource),   
    #---------------------------------------------------------Machine    
    path('machine',views.machine),
    path('edit_machine/<str:MachineID>', views.edit_machine),
    path('emp_machine', views.emp_machine),
    path('update_machine/<str:MachineID>', views.update_machine),    
    path('delete_machine/<str:MachineID>', views.destroy_machine),
    #----------------------------------------------------------------------
    path('multi_table_view_production_product',views.multi_table_view_production_product),
]