from django.urls import path
from. import views 
urlpatterns = [
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
#----------------------------------------------------product_material                              #看这要不要
#    path('product_material',views.product_material),
#    path('edit_product_material/<str:product_material_id>', views.edit_product_material),
#    path('emp_product_material', views.emp_product_material),
#    path('update_product_material/<str:product_material_id>', views.update_product_material),
#    path('delete_product_material/<str:product_material_id>', views.destroy_product_material), 
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
#-------------------------------------------------------------------------------------------
    path('multi_table_view_product_inspection', views.multi_table_view_product_inspection),
]