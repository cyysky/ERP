from django.urls import path

from calculator import views 

urlpatterns = [
#----------------------------------------------------calculator    
    path('calculator',views.calculator),
    path('edit_calculator/<int:id>', views.edit_calculator),
    path('emp_calculator', views.emp_calculator),
    path('update_calculator/<int:id>', views.update_calculator),
    path('delete_calculator/<int:id>', views.destroy_calculator), 
    
    path('delete_calculate/<int:id>', views.destroy_calculate),
#----------------------------------------------------

]