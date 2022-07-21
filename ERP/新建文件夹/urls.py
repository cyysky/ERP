from django.contrib import admin
from django.urls import path
from catrapp import views

urlpatterns =[
    
    path('admin/',admin.site.urls),
    path('/',views.index),
    path('index/',views.index),
    path('detail/<int:productid>/',views.index),
    path('addtocart/<str:ctype>/',views.addtocart), 
    path('addtocart/<str:ctype>/<int:productid>',views.addtocart), 
    path('cart/',views.cart),
    path('carttorder/',views.carttorder),
    path('cartok/',views.cartok),
    path('cartordercheck/',views.cartordercheck),
    ]