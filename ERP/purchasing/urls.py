from django.urls import path

from purchasing import views 

urlpatterns = [
#----------------------------------------------------    
    path('supplier',views.supplier),
    path('edit_supplier/<str:SupplierID>', views.edit_supplier),
    path('emp_supplier', views.emp_supplier),
    path('update_supplier/<str:SupplierID>', views.update_supplier),
    path('delete_supplier/<str:SupplierID>', views.destroy_supplier),
#----------------------------------------------------    
    path('material_supplier',views.material_supplier),
    path('edit_material_supplier/<str:MaterialSupplierID>', views.edit_material_supplier),
    path('emp_material_supplier', views.emp_material_supplier),
    path('update_material_supplier/<str:MaterialSupplierID>', views.update_material_supplier),    
    path('delete_material_supplier/<str:MaterialSupplierID>', views.destroy_material_supplier),
#----------------------------------------------------    
    path('purchase',views.purchase),
    path('edit_purchase/<str:PurchaseID>', views.edit_purchase),
    path('emp_purchase', views.emp_purchase),
    path('update_purchase/<str:PurchaseID>', views.update_purchase),
    path('delete_purchase/<str:PurchaseID>', views.destroy_purchase),
#----------------------------------------------------    
    path('require',views.require),
    path('edit_require/<str:RequireID>', views.edit_require),
    path('emp_require', views.emp_require),
    path('update_require/<str:RequireID>', views.update_require),
    path('delete_require/<str:RequireID>', views.destroy_require),
#----------------------------------------------------
    path('receive',views.receive),
    path('edit_receive/<str:ReceiveID>', views.edit_receive),
    path('emp_receive', views.emp_receive),
    path('update_receive/<str:ReceiveID>', views.update_receive),
    path('delete_receive/<str:ReceiveID>', views.destroy_receive),
]
