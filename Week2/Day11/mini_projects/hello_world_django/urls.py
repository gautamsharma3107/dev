"""
Hello World Django - Example URLs
==================================
Copy this code to your hello/urls.py file
"""

from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    # Home page: /
    path('', views.home, name='home'),
    
    # About page: /about/
    path('about/', views.about, name='about'),
    
    # Dynamic greeting: /greet/YourName/
    path('greet/<str:name>/', views.greet, name='greet'),
    
    # Current time: /time/
    path('time/', views.current_time, name='current_time'),
]
