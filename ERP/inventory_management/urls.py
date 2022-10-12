from django.urls import path
from. import views 

urlpatterns = [

#---------------------------------------------------------------------------------------Material  
    path('material',views.material),
    path('edit_material/<str:MaterialID>', views.edit_material),
    path('emp_material', views.emp_material),
    path('update_material/<str:MaterialID>', views.update_material),
    path('delete_material/<str:MaterialID>', views.destroy_material),
#--------------------------------------------------------------------------------------material_stock    
    path('material_stock',views.material_stock),
    path('edit_material_stock/<str:MaterialStockID>', views.edit_material_stock),
    path('emp_material_stock', views.emp_material_stock),
    path('update_material_stock/<str:MaterialStockID>', views.update_material_stock),
    path('delete_material_stock/<str:MaterialStockID>', views.destroy_material_stock),
#-------------------------------------------------------------------------------------------material_receive
    path('material_receive',views.material_receive),
    path('edit_material_receive/<str:MaterialReceiveID>', views.edit_material_receive),
    path('emp_material_receive', views.emp_material_receive),
    path('update_material_receive/<str:MaterialReceiveID>', views.update_material_receive),
    path('delete_material_receive/<str:MaterialReceiveID>', views.destroy_material_receive),
   
] 