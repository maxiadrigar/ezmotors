from django.urls import path
from . import views
from .views import BrandVehicleListView

app_name = 'vehicles'

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles', views.vehicle_list, name='vehicle_list'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('type/<int:type_id>/', views.vehicle_type_list, name='vehicle_type_list'),
    path('modelos/<str:brand_name>/', BrandVehicleListView.as_view(), name='brand_list'),
    path('sucursales/', views.sucursales, name='sucursales')
]