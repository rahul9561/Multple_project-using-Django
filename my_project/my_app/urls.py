from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="home"),
    path('signup/', signup,name='signup'),
    path('login/', login,name='login'),  
    path('logout/', logout,name='logout'),  
    path('cart/', cart,name='cart'),  
    path('delete/<int:pk>/', delete_view,name='delete'),
    path('products/<int:id>/', products_view,name='products'),
    path('update/<int:pk>/', update_view,name='update'),  
    path('dashboard/', dashboard,name='dashboard'),  
    path('home/',home,name="index"),
    path('api/get/',call_external_api,name="api_get"),
    path('youtube_thub/',youtube_thub,name="youtube")
]