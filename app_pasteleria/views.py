from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Empleado, Orden, Sucursal, Proveedor

# ==========================================
# VISTA DE INICIO
# ==========================================
def inicio(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS PARA PRODUCTOS
# ==========================================
def inicio_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/ver_producto.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        producto = Producto(
            nombre=request.POST['nombre'],
            categoria=request.POST['categoria'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            unidad=request.POST['unidad'],
            icono=request.POST['icono']
        )
        producto.save()
        # Agregar proveedores seleccionados
        proveedores_ids = request.POST.getlist('proveedores')
        for proveedor_id in proveedores_ids:
            proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
            producto.proveedores.add(proveedor)
        return redirect('inicio_productos')
    
    proveedores = Proveedor.objects.all()
    return render(request, 'productos/agregar_producto.html', {'proveedores': proveedores})

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    proveedores = Proveedor.objects.all()
    return render(request, 'productos/actualizar_producto.html', {
        'producto': producto,
        'proveedores': proveedores
    })

def realizar_actualizacion_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.categoria = request.POST['categoria']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.unidad = request.POST['unidad']
        producto.icono = request.POST['icono']
        producto.save()
        
        # Actualizar proveedores
        producto.proveedores.clear()
        proveedores_ids = request.POST.getlist('proveedores')
        for proveedor_id in proveedores_ids:
            proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
            producto.proveedores.add(proveedor)
    return redirect('inicio_productos')

def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('inicio_productos')
    return render(request, 'productos/borrar_producto.html', {'producto': producto})

# ==========================================
# VISTAS PARA EMPLEADOS
# ==========================================
def inicio_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/ver_empleado.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        empleado = Empleado(
            nombre=request.POST['nombre'],
            telefono=request.POST['telefono'],
            puesto=request.POST['puesto'],
            email=request.POST['email'],
            salario=request.POST['salario']
        )
        empleado.save()
        return redirect('inicio_empleados')
    return render(request, 'empleados/agregar_empleado.html')

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    return render(request, 'empleados/actualizar_empleado.html', {'empleado': empleado})

def realizar_actualizacion_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.telefono = request.POST['telefono']
        empleado.puesto = request.POST['puesto']
        empleado.email = request.POST['email']
        empleado.salario = request.POST['salario']
        empleado.save()
    return redirect('inicio_empleados')

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('inicio_empleados')
    return render(request, 'empleados/borrar_empleado.html', {'empleado': empleado})

# ==========================================
# VISTAS PARA ÓRDENES
# ==========================================
def inicio_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'ordenes/ver_orden.html', {'ordenes': ordenes})

def agregar_orden(request):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['empleado'])
        orden = Orden(
            cliente=request.POST['cliente'],
            telefono=request.POST['telefono'],
            direccion=request.POST['direccion'],
            total=request.POST['total'],
            tipo_pago=request.POST['tipo_pago'],
            empleado=empleado
        )
        orden.save()
        productos_ids = request.POST.getlist('productos')
        for producto_id in productos_ids:
            producto = get_object_or_404(Producto, id_producto=producto_id)
            orden.productos.add(producto)
        return redirect('inicio_ordenes')
    
    empleados = Empleado.objects.all()
    productos = Producto.objects.all()
    return render(request, 'ordenes/agregar_orden.html', {
        'empleados': empleados,
        'productos': productos
    })

def actualizar_orden(request, id):
    orden = get_object_or_404(Orden, id_orden=id)
    empleados = Empleado.objects.all()
    productos = Producto.objects.all()
    return render(request, 'ordenes/actualizar_orden.html', {
        'orden': orden,
        'empleados': empleados,
        'productos': productos
    })

def realizar_actualizacion_orden(request, id):
    orden = get_object_or_404(Orden, id_orden=id)
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['empleado'])
        orden.cliente = request.POST['cliente']
        orden.telefono = request.POST['telefono']
        orden.direccion = request.POST['direccion']
        orden.total = request.POST['total']
        orden.tipo_pago = request.POST['tipo_pago']
        orden.empleado = empleado
        orden.save()
        
        orden.productos.clear()
        productos_ids = request.POST.getlist('productos')
        for producto_id in productos_ids:
            producto = get_object_or_404(Producto, id_producto=producto_id)
            orden.productos.add(producto)
    return redirect('inicio_ordenes')

def borrar_orden(request, id):
    orden = get_object_or_404(Orden, id_orden=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('inicio_ordenes')
    return render(request, 'ordenes/borrar_orden.html', {'orden': orden})

# ==========================================
# VISTAS PARA SUCURSALES
# ==========================================
def inicio_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales/ver_sucursal.html', {'sucursales': sucursales})

def agregar_sucursal(request):
    if request.method == 'POST':
        encargado_id = request.POST.get('encargado')
        encargado = get_object_or_404(Empleado, id_empleado=encargado_id) if encargado_id else None
        
        sucursal = Sucursal(
            nombre=request.POST['nombre'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            horario=request.POST['horario'],
            encargado=encargado
        )
        sucursal.save()
        return redirect('inicio_sucursales')
    
    empleados = Empleado.objects.all()
    return render(request, 'sucursales/agregar_sucursal.html', {'empleados': empleados})

def actualizar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id)
    empleados = Empleado.objects.all()
    return render(request, 'sucursales/actualizar_sucursal.html', {
        'sucursal': sucursal,
        'empleados': empleados
    })

def realizar_actualizacion_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id)
    if request.method == 'POST':
        encargado_id = request.POST.get('encargado')
        encargado = get_object_or_404(Empleado, id_empleado=encargado_id) if encargado_id else None
        
        sucursal.nombre = request.POST['nombre']
        sucursal.direccion = request.POST['direccion']
        sucursal.telefono = request.POST['telefono']
        sucursal.horario = request.POST['horario']
        sucursal.encargado = encargado
        sucursal.save()
    return redirect('inicio_sucursales')

def borrar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('inicio_sucursales')
    return render(request, 'sucursales/borrar_sucursal.html', {'sucursal': sucursal})

# ==========================================
# VISTAS PARA PROVEEDORES
# ==========================================
def inicio_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/ver_proveedor.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        proveedor = Proveedor(
            nombre=request.POST['nombre'],
            telefono=request.POST['telefono'],
            cantidad=request.POST['cantidad'],
            producto=request.POST['producto'],
            fecha_entrega=request.POST['fecha_entrega'],
            tipo_pago=request.POST['tipo_pago'],
            total=request.POST['total']
        )
        proveedor.save()
        return redirect('inicio_proveedores')
    return render(request, 'proveedores/agregar_proveedor.html')

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    return render(request, 'proveedores/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.telefono = request.POST['telefono']
        proveedor.cantidad = request.POST['cantidad']
        proveedor.producto = request.POST['producto']
        proveedor.fecha_entrega = request.POST['fecha_entrega']
        proveedor.tipo_pago = request.POST['tipo_pago']
        proveedor.total = request.POST['total']
        proveedor.save()
    return redirect('inicio_proveedores')

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('inicio_proveedores')
    return render(request, 'proveedores/borrar_proveedor.html', {'proveedor': proveedor})