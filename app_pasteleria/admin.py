from django.contrib import admin
from .models import Producto, Empleado, Orden, Sucursal, Proveedor

admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Orden)
admin.site.register(Sucursal)
admin.site.register(Proveedor)