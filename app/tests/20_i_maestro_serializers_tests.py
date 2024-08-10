import pytest


@pytest.mark.django_db
def test_institucion_serializer():
    pass


@pytest.mark.django_db
def test_medicamento_serializer():
    pass


@pytest.mark.django_db
def test_item_serializer():
    pass


@pytest.mark.django_db
def test_equipamiento_serializer():
    pass


@pytest.mark.django_db
def test_quiebre_serializer():
    pass


# from maestro.models import Institucion, Medicamento, Quiebre
# from maestro.serializers import QuiebreSerializer
# import pytest
# import json

# from maestro.models import Institucion, Item, Medicamento, Quiebre


# @pytest.mark.django_db
# def test_institucion_serializer():
#     from maestro.serializers import InstitucionSerializer

#     institucion = Institucion.objects.create(
#         nombre="Hospital de San Antonio", tipo="hospital", titularidad="publico", num_camas_uti=10, num_camas_uci=5, factor=1.0
#     )

#     data = {
#         "nombre": institucion.nombre,
#         "tipo": institucion.tipo,
#         "titularidad": institucion.titularidad,
#         "num_camas_uti": institucion.num_camas_uti,
#         "num_camas_uci": institucion.num_camas_uci,
#     }

#     serialized_data = InstitucionSerializer(data=data)
#     serialized_object = InstitucionSerializer(institucion)
#     serialized_data.is_valid()

#     assert json.dumps(serialized_object.data) == json.dumps(
#         data), "data serializada no tiene el orden correcto"
#     assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


# @pytest.mark.django_db
# def test_medicamento_serializer():
#     from maestro.serializers import MedicamentoSerializer

#     medicamento = Medicamento.objects.create(
#         nombre_comercial="Paracetamol", nombre_generico="Paracetamol", ingredientes="Paracetamol", concentracion="500mg", forma_presentacion="frasco", forma_farmaceutica="tabletas", via_administracion="oral", indicaciones_terapeuticas="Dolor", contraindicaciones="Ninguna", efectos_secundarios="Ninguno", instrucciones_dosificacion="1 tableta cada 8 horas", fabricante="Bayer", informacion_almacenamiento="Lugar fresco y seco", interacciones_medicamentosas="Ninguna"
#     )

#     data = {
#         "nombre_comercial": medicamento.nombre_comercial,
#         "nombre_generico": medicamento.nombre_generico,
#         "ingredientes": medicamento.ingredientes,
#         "concentracion": medicamento.concentracion,
#         "forma_presentacion": medicamento.forma_presentacion,
#         "forma_farmaceutica": medicamento.forma_farmaceutica,
#         "via_administracion": medicamento.via_administracion,
#         "indicaciones_terapeuticas": medicamento.indicaciones_terapeuticas,
#         "contraindicaciones": medicamento.contraindicaciones,
#         "efectos_secundarios": medicamento.efectos_secundarios,
#         "instrucciones_dosificacion": medicamento.instrucciones_dosificacion,
#         "fabricante": medicamento.fabricante,
#         "informacion_almacenamiento": medicamento.informacion_almacenamiento,
#         "interacciones_medicamentosas": medicamento.interacciones_medicamentosas,
#     }

#     serialized_data = MedicamentoSerializer(data=data)
#     serialized_object = MedicamentoSerializer(medicamento)
#     serialized_data.is_valid()

#     assert json.dumps(serialized_object.data) == json.dumps(
#         data), "data serializada no tiene el orden correcto"
#     assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


# @pytest.mark.django_db
# def test_item_serializer():
#     from maestro.serializers import ItemSerializer

#     item = Item.objects.create(
#         nombre="Monitor de signos vitales", tipo="apoyo_monitorizacion"
#     )

#     data = {
#         "nombre": item.nombre,
#         "tipo": item.tipo,
#     }

#     serialized_data = ItemSerializer(data=data)
#     serialized_object = ItemSerializer(item)
#     serialized_data.is_valid()

#     assert json.dumps(serialized_object.data) == json.dumps(
#         data), "data serializada no tiene el orden correcto"
#     assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


# @pytest.mark.django_db
# def test_equipamiento_serializer():
#     from maestro.serializers import EquipamientoSerializer

#     item = Item.objects.create(
#         nombre="Monitor de signos vitales", tipo="apoyo_monitorizacion"
#     )

#     equipamiento = item.equipamiento_set.create(
#         marca="Bosch", modelo="2021"
#     )

#     data = {
#         "item": item.id,
#         "marca": equipamiento.marca,
#         "modelo": equipamiento.modelo,
#     }

#     serialized_data = EquipamientoSerializer(data=data)
#     serialized_object = EquipamientoSerializer(equipamiento)
#     serialized_data.is_valid()

#     assert json.dumps(serialized_object.data) == json.dumps(
#         data), "data serializada no tiene el orden correcto"
#     assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


# @pytest.mark.django_db
# def test_quiebre_serializer():
#     institucion = Institucion.objects.create(
#         nombre="Hospital de Talca", tipo="hospital", titularidad="publico", num_camas_uti=10, num_camas_uci=5, factor=1.0
#     )

#     medicamento = Medicamento.objects.create(
#         nombre_comercial="Panadol", nombre_generico="Panadol", ingredientes="Panadol", concentracion="500mg", forma_presentacion="frasco", forma_farmaceutica="tabletas", via_administracion="oral", indicaciones_terapeuticas="Dolor", contraindicaciones="Ninguna", efectos_secundarios="Ninguno", instrucciones_dosificacion="1 tableta cada 8 horas", fabricante="Bayer", informacion_almacenamiento="Lugar fresco y seco", interacciones_medicamentosas="Ninguna"
#     )

#     # Verifica si ya existe un objeto Quiebre con la misma institucion y medicamento
#     quiebre, created = Quiebre.objects.get_or_create(
#         institucion=institucion, medicamento=medicamento, defaults={
#             'cantidad': 500}
#     )

#     data = {
#         "institucion": institucion.id,
#         "medicamento": medicamento.id,
#         "cantidad": quiebre.cantidad,
#     }

#     serialized_data = QuiebreSerializer(data=data)
#     serialized_object = QuiebreSerializer(quiebre)
#     is_valid = serialized_data.is_valid()

#     assert is_valid, f"Errores: {serialized_data.errors}"
#     assert json.dumps(serialized_object.data) == json.dumps(
#         data), "data serializada no tiene el orden correcto"