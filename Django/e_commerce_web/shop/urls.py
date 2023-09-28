from django.urls import path
from shop import views


urlpatterns = [
    path('', views.Shop, name= 'shop' ),
    path('checkout/', views.Checkout , name='checkout'),
    path('product-details/<str:slug>/', views.Product_Details, name='product_details'),
    
]

