from django.urls import path
from accounts.views import login_view,register_view,profile_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About, name='about'),
    path('shop/', views.Shop, name='shop'),
    path('cart/', views.Cart_View, name='cart'),
    path('<int:id>/<slug:Product_slug>',
         views.Product_Details,
         name='product_detail'),
    path('checkout/', views.CheckOut, name='checkout'),
    path('contact/', views.Contact, name='contact'),
    path('login/', login_view, name='login'),
   
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile')
]
