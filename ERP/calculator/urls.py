from django.urls import path

from calculator import views 

urlpatterns = [
#----------------------------------------------------calculator    
    path('calculator',views.calculator),
    path('edit_calculator/<str:id>', views.edit_calculator),
    path('emp_calculator', views.emp_calculator),
    path('update_calculator/<str:id>', views.update_calculator),
    path('delete_calculator/<str:id>', views.destroy_calculator), 
    
    path('delete_calculate/<str:id>', views.destroy_calculate),
#----------------------------------------------------

]