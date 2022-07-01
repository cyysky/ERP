from django.urls import path, include

from purchasing import views 

urlpatterns = [


#-----------------------------------------------------supplier    
    path('supplier',views.supplier),  
    path('edit_supplier/<int:supplier_id>', views.edit_supplier),
    path('emp_supplier', views.emp_supplier),
    path('update_supplier/<int:supplier_id>', views.update_supplier),   
    path('delete_supplier/<int:supplier_id>', views.destroy_supplier),

#----------------------------------------------------Material_Supplier    
    path('material_supplier',views.material_supplier),
    path('edit_material_supplier/<int:id>', views.edit_material_supplier),
    path('emp_material_supplier', views.emp_material_supplier),
    path('update_material_supplier/<int:id>', views.update_material_supplier),    
    path('delete_material_supplier/<int:id>', views.destroy_material_supplier),

#--------------------------------------------------------purchase
    path('purchase',views.purchase),
    path('edit_purchase/<int:id>', views.edit_purchase),
    path('emp_purchase', views.emp_purchase),
    path('update_purchase/<int:id>', views.update_purchase),    
    path('delete_purchase/<int:id>', views.destroy_purchase),

]