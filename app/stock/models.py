from datetime import date
from django.db import models
from maestro.models import Medicamento, Institucion


class Lote(models.Model):
    codigo = models.CharField(max_length=255)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=500)
    fecha_vencimiento = models.DateField()

    def __str__(self) -> str:
        return f"{self.codigo}"


class Consumo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.cantidad}"


class Stock(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    has_quiebre = models.BooleanField(default=False)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.has_quiebre}"


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, unique=True)
    fecha = models.DateField(default=date.today)

    class Meta:
        unique_together = [("lote")]

    def __str__(self) -> str:
        return f"{self.fecha}"
