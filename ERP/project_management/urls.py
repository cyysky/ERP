from django.urls import path
from. import views 

urlpatterns = [
#-----------------------------------------------------------------------------
    path('planning_new_product_projects',views.planning_new_product_projects),

#--------------------------------------------------------------------------project_sales_item
    path('project_sales_item',views.project_sales_item),
    path('edit_project_sales_item/<str:ProjectSalesItemID>', views.edit_project_sales_item),
    path('emp_project_sales_item', views.emp_project_sales_item),
    path('update_project_sales_item/<str:ProjectSalesItemID>', views.update_project_sales_item),
    path('delete_project_sales_item/<str:ProjectSalesItemID>', views.destroy_project_sales_item),
    path('update_project_to_require/<str:ProjectSalesItemID>', views.update_project_to_require),
#-------------------------------------------------------------------------------------
    path('project_dashboard',views.project_dashboard),

]