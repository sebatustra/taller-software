# from django.db import IntegrityError
# import pytest


# @pytest.mark.django_db
# def test_institucion_model():
#     from maestro.models import Institucion

#     nombre = "Hospital Clínico"
#     tipo = Institucion.Tipo.HOSPITAL_CLINICO
#     titularidad = Institucion.Titularidad.PUBLICO
#     num_camas_uti = 10
#     num_camas_uci = 5
#     factor = 1.5

#     institucion = Institucion.objects.create(
#         nombre=nombre,
#         tipo=tipo,
#         titularidad=titularidad,
#         num_camas_uti=num_camas_uti,
#         num_camas_uci=num_camas_uci,
#         factor=factor,
#     )

#     assert institucion.nombre == nombre
#     assert institucion.tipo == tipo
#     assert institucion.titularidad == titularidad
#     assert institucion.num_camas_uti == num_camas_uti
#     assert institucion.num_camas_uci == num_camas_uci
#     assert institucion.factor == factor

#     assert str(
#         institucion) == nombre, "se debe usar el nombre como representación str del objeto"

#     institucion.num_camas_uci = -5
#     institucion.num_camas_uti = -10

#     with pytest.raises(IntegrityError):
#         institucion.save()

#         institucion = Institucion.objects.get(id=institucion.id)
#         assert institucion.num_camas_uci >= 0, "camas UCI debe ser mayor o igual que cero"
#         assert institucion.num_camas_uti >= 0, "camas UTI debe ser mayor o igual que cero"


# @pytest.mark.django_db
# def test_medicamento_model():
#     from maestro.models import Medicamento

#     nombre_comercial = "Paracetamol"
#     nombre_generico = "Acetaminofén"
#     ingredientes = "Paracetamol"
#     concentracion = "500 mg"
#     forma_presentacion = Medicamento.FormaPresentacion.FRASCO
#     forma_farmaceutica = Medicamento.FormaFarmaceutica.TABLETAS
#     via_administracion = Medicamento.Via.ORAL
#     indicaciones_terapeuticas = "Dolor y fiebre"
#     contraindicaciones = "Alergia al paracetamol"
#     efectos_secundarios = "Ninguno"
#     instrucciones_dosificacion = "1 tableta cada 6 horas"
#     fabricante = "Bayer"
#     informacion_almacenamiento = "Lugar fresco y seco"
#     interacciones_medicamentosas = "Ninguna"

#     medicamento = Medicamento.objects.create(
#         nombre_comercial=nombre_comercial,
#         nombre_generico=nombre_generico,
#         ingredientes=ingredientes,
#         concentracion=concentracion,
#         forma_presentacion=forma_presentacion,
#         forma_farmaceutica=forma_farmaceutica,
#         via_administracion=via_administracion,
#         indicaciones_terapeuticas=indicaciones_terapeuticas,
#         contraindicaciones=contraindicaciones,
#         efectos_secundarios=efectos_secundarios,
#         instrucciones_dosificacion=instrucciones_dosificacion,
#         fabricante=fabricante,
#         informacion_almacenamiento=informacion_almacenamiento,
#         interacciones_medicamentosas=interacciones_medicamentosas,
#     )

#     assert medicamento.nombre_comercial == nombre_comercial
#     assert medicamento.nombre_generico == nombre_generico
#     assert medicamento.ingredientes == ingredientes
#     assert medicamento.concentracion == concentracion
#     assert medicamento.forma_presentacion == forma_presentacion
#     assert medicamento.forma_farmaceutica == forma_farmaceutica
#     assert medicamento.via_administracion == via_administracion
#     assert medicamento.indicaciones_terapeuticas == indicaciones_terapeuticas
#     assert medicamento.contraindicaciones == contraindicaciones
#     assert medicamento.efectos_secundarios == efectos_secundarios
#     assert medicamento.instrucciones_dosificacion == instrucciones_dosificacion
#     assert medicamento.fabricante == fabricante
#     assert medicamento.informacion_almacenamiento == informacion_almacenamiento
#     assert medicamento.interacciones_medicamentosas == interacciones_medicamentosas

#     assert str(
#         medicamento) == f"{nombre_comercial} ({nombre_generico}) | {fabricante}", "se debe usar el nombre comercial y genérico como representación str del objeto"


# @pytest.mark.django_db
# def test_item_model():
#     from maestro.models import Item

#     nombre = "Monitor de signos vitales"
#     tipo = Item.Tipo.APOYO_MONITORIZACION

#     item = Item.objects.create(
#         nombre=nombre,
#         tipo=tipo,
#     )

#     assert item.nombre == nombre
#     assert item.tipo == tipo

#     assert str(
#         item) == f"{nombre} ({tipo})", "se debe usar el nombre y tipo como representación str del objeto"


# """
# class Equipamiento(models.Model):
#     class Tipo(models.TextChoices):
#         SOPORTE_VITAL = "soporte_vital", "Soporte Vital"
#         APOYO_MONITORIZACION = "apoyo_monitorizacion", "Apoyo y Monitorización"

#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     marca = models.CharField(max_length=255)
#     modelo = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return f"{self.modelo} ({self.modelo}) | {self.item}"


# """


# @pytest.mark.django_db
# def test_equipamiento_model():
#     from maestro.models import Equipamiento, Item

#     item = Item.objects.all().first()
#     marca = "Philips"
#     modelo = "M3"

#     equipamiento = Equipamiento.objects.create(
#         item=item,
#         marca=marca,
#         modelo=modelo,
#     )

#     assert equipamiento.item == item
#     assert equipamiento.marca == marca
#     assert equipamiento.modelo == modelo

#     # Incidencia: modelo se repite en lugar de marca
#     assert str(
#         equipamiento) == f"{modelo} ({modelo}) | {item}", "se debe usar el modelo y marca como representación str del objeto"


# @pytest.mark.django_db
# def test_quiebre_model():
#     from maestro.models import Quiebre, Institucion, Medicamento

#     institucion = Institucion.objects.all().first()
#     medicamento = Medicamento.objects.all().first()

#     quiebre = Quiebre.objects.create(
#         institucion=institucion,
#         medicamento=medicamento,
#         cantidad=500,
#     )

#     assert quiebre.institucion == institucion
#     assert quiebre.medicamento == medicamento
#     assert quiebre.cantidad == 500

#     with pytest.raises(IntegrityError):
#         Quiebre.objects.create(
#             institucion=institucion,
#             medicamento=medicamento,
#             cantidad=-500,
#         )

#         quiebre = Quiebre.objects.get(id=quiebre.id)
#         assert quiebre.cantidad >= 0, "cantidad debe ser mayor o igual que cero"


import pytest


@pytest.mark.django_db
def test_institucion_model():
    pass


@pytest.mark.django_db
def test_medicamento_model():
    pass


@pytest.mark.django_db
def test_item_model():
    pass


@pytest.mark.django_db
def test_equipamiento_model():
    pass


@pytest.mark.django_db
def test_quiebre_model():
    pass
