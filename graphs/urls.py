from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    # path for about
    path('about.html', views.about, name="about" ),
    # stock page
    path('stock.html', views.stock, name="stock" ),
    path('deleteStock/<stock_id>', views.deleteStock, name="deleteStock" ),

    
]
