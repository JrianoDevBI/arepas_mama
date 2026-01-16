from django.db import models

# Modelo tabla clientes
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    documento_cliente = models.CharField(max_length=20, unique=True, null=True, blank=True)
    telefono_cliente = models.CharField(max_length=20)
    direccion_cliente = models.CharField(max_length=150)
    email_cliente = models.EmailField(max_length=50, null=True, blank=True)
    estado_activo_cliente = models.BooleanField(default=True)
    fecha_creacion_cliente = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_cliente = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_cliente 


# Modelo tabla proveedor
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100)
    documento_proveedor = models.CharField(max_length=20, unique=True, null=True, blank=True)
    telefono_proveedor = models.CharField(max_length=20)
    direccion_proveedor = models.CharField(max_length=150)
    email_proveedor = models.EmailField(max_length=50, null=True, blank=True)
    estado_activo_proveedor = models.BooleanField(default=True)
    fecha_creacion_proveedor = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_proveedor = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_proveedor

# Modelo tabla producto
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    descripcion_producto = models.TextField(null=True, blank=True)
    precio_compra_producto = models.DecimalField(max_digits=12, decimal_places=2)
    precio_venta_producto = models.DecimalField(max_digits=12, decimal_places=2)
    stock_producto = models.IntegerField(default=0)
    estado_activo_producto = models.BooleanField(default=True)
    fecha_creacion_producto = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_producto = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_producto

# Modelo tabla Factura de Venta
class FacturaVenta(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.RESTRICT,
        related_name="facturas_venta"
    )
    fecha_factura_venta = models.DateTimeField(auto_now_add=True)
    total_factura_venta = models.DecimalField(max_digits=12, decimal_places=2)
    actualizacion_factura_venta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Factura Venta #{self.id}"


# Modelo tabla factura de Compra
class FacturaCompra(models.Model):
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.RESTRICT,
        related_name="facturas_compra"
    )
    fecha_factura_compra = models.DateTimeField(auto_now_add=True)
    total_factura_compra = models.DecimalField(max_digits=12, decimal_places=2)
    actualizacion_factura_compra = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Factura Compra #{self.id}"

# Modelo tabla detalle de Factura de Compra
class DetalleFacturaCompra(models.Model):
    factura_compra = models.ForeignKey(
        FacturaCompra,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.RESTRICT
    )
    cantidad_detalle_compra = models.IntegerField()
    precio_unitario_detalle_compra = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal_detalle_compra = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_creacion_detalle_compra = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_detalle_compra = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Detalle Compra #{self.id}"

# Modelo tabla detalle de Factura de Venta
class DetalleFacturaVenta(models.Model):
    factura_venta = models.ForeignKey(
        FacturaVenta,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.RESTRICT
    )
    cantidad_detalle_venta = models.IntegerField()
    precio_unitario_detalle_venta = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal_detalle_venta = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_creacion_detalle_venta = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_detalle_venta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Detalle Venta #{self.id}"

# Modelo tabla Pago de Venta
class PagoVenta(models.Model):
    factura_venta = models.ForeignKey(
        FacturaVenta,
        on_delete=models.RESTRICT,
        related_name="pagos"
    )
    monto = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_pago_venta = models.DateTimeField(auto_now_add=True)
    actualizacion_pago_venta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pago Venta #{self.id}"

# Modelo tabla Pago de Compra
class PagoCompra(models.Model):
    factura_compra = models.ForeignKey(
        FacturaCompra,
        on_delete=models.RESTRICT,
        related_name="pagos"
    )
    monto = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_pago_compra = models.DateTimeField(auto_now_add=True)
    actualizacion_pago_compra = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pago Compra #{self.id}"
