from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    # path for about
    path('about.html', views.about, name="about" ),

    
]
