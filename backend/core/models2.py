from django.db import models

# Modelo tabla clientes
class Cliente(models.Moldel):
    nombre_cliente = models.models.CharField(max_length=100),
    documento_cliente = models.models.CharField(max_length=20, unique=True, null=True, blank=True),
    telefono_cliente = models.models.CharField(max_length=20),
    direccion_cliente = models.models.CharField(max_length=150),
    email_cliente = models.models.EmailField(max_length=50, null=True, blank=True),
    estado_activo_cliente = models.models.BooleanField(default = True),
    fecha_creacion_cliente = models.models.DateTimeField(auto_now_add=True),
    fecha_actualizacion_cliente = models.models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nombre_cliente

# Modelo tabla proveedor