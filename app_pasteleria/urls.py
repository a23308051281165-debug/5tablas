from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # Productos
    path('productos/', views.inicio_productos, name='inicio_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('productos/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),
    
    # Empleados
    path('empleados/', views.inicio_empleados, name='inicio_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
    
    # Órdenes
    path('ordenes/', views.inicio_ordenes, name='inicio_ordenes'),
    path('ordenes/agregar/', views.agregar_orden, name='agregar_orden'),
    path('ordenes/actualizar/<int:id>/', views.actualizar_orden, name='actualizar_orden'),
    path('ordenes/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_orden, name='realizar_actualizacion_orden'),
    path('ordenes/borrar/<int:id>/', views.borrar_orden, name='borrar_orden'),
    
    # Sucursales
    path('sucursales/', views.inicio_sucursales, name='inicio_sucursales'),
    path('sucursales/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursales/actualizar/<int:id>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursales/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('sucursales/borrar/<int:id>/', views.borrar_sucursal, name='borrar_sucursal'),
    
    # Proveedores
    path('proveedores/', views.inicio_proveedores, name='inicio_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedores/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),
]