from django.db import models

# Primero definimos Proveedor ya que Producto lo necesita
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=0)
    producto = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    tipo_pago = models.CharField(
        max_length=20,
        choices=[
            ('Efectivo', 'Efectivo'),
            ('Tarjeta', 'Tarjeta'),
            ('Transferencia', 'Transferencia'),
            ('Otro', 'Otro')
        ],
        default='Efectivo'
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# Luego Producto que usa Proveedor
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    unidad = models.CharField(
        max_length=10,
        choices=[
            ('kg', 'Kilogramos'),
            ('gr', 'Gramos'),
            ('l', 'Litros'),
            ('ml', 'Mililitros'),
            ('pz', 'Piezas'),
        ],
        default='pz'
    )
    icono = models.CharField(max_length=100, blank=True, null=True)
    # RELACIÓN CON PROVEEDORES (Muchos a Muchos)
    proveedores = models.ManyToManyField(Proveedor, related_name="productos", blank=True)

    def __str__(self):
        return self.nombre

# Luego Empleado que es usado por Sucursal y Orden
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    puesto = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Luego Sucursal que usa Empleado
class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    horario = models.CharField(max_length=100, blank=True, null=True)
    # RELACIÓN CON EMPLEADO (Foreign Key para el encargado)
    encargado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sucursales_encargadas"
    )

    def __str__(self):
        return self.nombre

# Finalmente Orden que usa Producto y Empleado
class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    productos = models.ManyToManyField(Producto, related_name="ordenes")
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pago = models.CharField(
        max_length=20,
        choices=[
            ('Efectivo', 'Efectivo'),
            ('Tarjeta', 'Tarjeta'),
            ('Transferencia', 'Transferencia'),
            ('Otro', 'Otro')
        ],
        default='Efectivo'
    )
    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name="ordenes"
    )

    def __str__(self):
        return f"Orden #{self.id_orden} - {self.cliente}"