from django.urls import path
from. import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('upload_image/', views.uploadView, name= 'upload_image') # new
]