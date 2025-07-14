from django.db import models
from django.views.generic import ListView

# Aca creo los modelos
class VehicleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()  # <-- ahora es year
    version = models.CharField(max_length=100, blank=True, null=True)
    kilometers = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='vehicles/', null=True, blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.version or ''} {self.year}, {self.kilometers}km, ${self.price}"

class VehicleImage(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicles/')

    def __str__(self):
        return f"Imagen de {self.vehicle}"

class BrandVehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicles/brand_vehicle_list.html'  # usa tu plantilla
    context_object_name = 'vehicles'

    def get_queryset(self):
        # Obtén la marca de la URL y filtra
        brand_name = self.kwargs.get('brand_name')
        return Vehicle.objects.filter(brand__name__iexact=brand_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = self.kwargs.get('brand_name').capitalize()
        return context