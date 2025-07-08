from django.contrib import admin
from. models import *

# Register your models here.
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

# Si quieres, puedes registrar VehicleImage para verlo como lista aparte:
@admin.register(VehicleImage)
class VehicleImageAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'image')
