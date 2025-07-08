from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    vehicles = Vehicle.objects.all().order_by('-year')
    return render(request, 'vehicles/home.html', {
        'vehicles': vehicles
    })

def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-year')
    paginator = Paginator(vehicles, 12)  # Mostrar n vehiculos por página

    page_number = request.GET.get('page')  # ?page=2
    page_obj = paginator.get_page(page_number)

    return render(request, 'vehicles/vehicle_list.html', {'page_obj': page_obj})

# Detalle de un vehículo individual
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/vehicle_detail.html', {'vehicle': vehicle})

def vehicle_type_list(request, type_id):
    vehicle_type = get_object_or_404(VehicleType, id=type_id)
    vehicles = Vehicle.objects.filter(vehicle_type=vehicle_type).order_by('-year')
    return render(request, 'vehicles/vehicle_type_list.html', {
        'vehicle_type': vehicle_type,
        'vehicles': vehicles
    })

class BrandVehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicles/brand_list.html'
    context_object_name = 'vehicles'
    paginate_by = 12  # opcional: para paginar si tienes muchos autos

    def get_queryset(self):
        self.brand = get_object_or_404(Brand, name=self.kwargs['brand_name'])
        return Vehicle.objects.filter(brand=self.brand).order_by('-year')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = self.brand
        return context
    
def sucursales(request):
    return render(request, 'vehicles/sucursales.html')