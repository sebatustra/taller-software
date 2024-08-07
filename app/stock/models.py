from datetime import date
from django.db import models
from maestro.models import Medicamento, Institucion, Quiebre


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original
        # Actualizar la cantidad del Stock asociado
        stock, created = Stock.objects.get_or_create(institucion=self.institucion, medicamento=self.medicamento)
        stock.cantidad -= self.cantidad
        stock.save()


class Stock(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    has_quiebre = models.BooleanField(default=False)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.has_quiebre}"

    def upd_cantidad(self):
        """
        Calcula la cantidad total del medicamento en el stock,
        basándose en los movimientos y consumos.
        """
        # Obtener todos los movimientos asociados a este stock
        movimientos = Movimiento.objects.filter(lote__medicamento=self.medicamento, lote__institucion=self.institucion)
        cantidad_entradas = sum(movimiento.lote.cantidad for movimiento in movimientos)

        # Obtener todos los consumos asociados a este stock
        consumos = Consumo.objects.filter(medicamento=self.medicamento, institucion=self.institucion)
        cantidad_salidas = sum(consumo.cantidad for consumo in consumos)

        # Calcular la cantidad total
        self.cantidad = cantidad_entradas - cantidad_salidas
        self.save()

    def save(self, *args, **kwargs):
        self.upd_has_quiebre()
        super().save(*args, **kwargs)

    def upd_has_quiebre(self):
        quiebre = Quiebre.objects.filter(institucion=self.institucion, medicamento=self.medicamento).first()
        if quiebre:
            self.has_quiebre = self.cantidad <= quiebre.cantidad


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, unique=True)
    fecha = models.DateField(default=date.today)

    class Meta:
        unique_together = [("lote")]

    def __str__(self) -> str:
        return f"{self.fecha}"

    def save(self, *args, **kwargs):
        if self.lote.fecha_vencimiento <= date.today():
            return
        super().save(*args, **kwargs)
        stock, created = Stock.objects.get_or_create(institucion=self.institucion, medicamento=self.lote.medicamento)
        stock.cantidad += self.lote.cantidad
        stock.save()
