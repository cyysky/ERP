from django.urls import path, include

from warehouse import views 

urlpatterns = [

#----------------------------------------------------Material    
    path('material',views.material),
    path('edit_material/<int:material_id>', views.edit_material),
    path('emp_material', views.emp_material),
    path('update_material/<int:material_id>', views.update_material),    
    path('delete_material/<int:material_id>', views.destroy_material),
#----------------------------------------------------Material_Location    
    path('material_stock',views.material_stock),
    path('edit_material_stock/<int:material_stock_id>', views.edit_material_stock),
    path('emp_material_stock', views.emp_material_stock),
    path('update_material_stock/<int:material_stock_id>', views.update_material_stock),    
    path('delete_material_stock/<int:material_stock_id>', views.destroy_material_stock),

] 