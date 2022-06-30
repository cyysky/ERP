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
    path('material_location',views.material_location),
    path('edit_material_location/<int:material_location_id>', views.edit_material_location),
    path('emp_material_location', views.emp_material_location),
    path('update_material_location/<int:material_location_id>', views.update_material_location),    
    path('delete_material_location/<int:material_location_id>', views.destroy_material_location),

] 