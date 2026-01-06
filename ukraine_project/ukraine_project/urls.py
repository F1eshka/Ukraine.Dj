from django.contrib import admin
from django.urls import path
from wiki import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index),
    path('facts/', views.facts),
    
    path('history/<int:year>/', views.history_year),
    path('history/', views.history_list),
    
    path('cities/<str:city_name>/<int:year>/', views.city_year_detail),
    
    path('cities/<str:city_name>/', views.city_detail),
    
    path('cities/', views.cities_list),
]