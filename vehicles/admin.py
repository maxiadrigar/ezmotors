from django.contrib import admin
from .models import VehicleType, Brand, Vehicle, VehicleImage

# Inline para imágenes secundarias (en el mismo formulario del vehículo)
class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 1  # muestra un formulario vacío para agregar más fotos

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'version', 'year', 'vehicle_type', 'kilometers', 'price')
    list_filter = ('vehicle_type', 'brand', 'year')
    search_fields = ('version', 'brand__name')
    inlines = [VehicleImageInline]

    fieldsets = (
        (None, {
            'fields': ('brand', 'vehicle_type', 'version', 'year', 'kilometers', 'price', 'description')
        }),
        ('Imagen principal', {
            'fields': ('image',),
            'description': 'Seleccioná una imagen desde tu computadora. Se subirá y servirá desde tu servidor en Render.'
        }),
    )

@admin.register(VehicleImage)
class VehicleImageAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'image')
