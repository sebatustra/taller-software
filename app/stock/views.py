from rest_framework.views import APIView
from datetime import date
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Consumo, Movimiento
from .serializers import ConsumoSerializer, MovimientoSerializer
from django.shortcuts import get_object_or_404


class MovimientoListCreateView(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Movimiento.objects.all()
        serializer = MovimientoSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        serializer = MovimientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class MovimientoRetrieveDestroyView(viewsets.ModelViewSet):

    def retrieve(self, request, pk=None):
        queryset = Movimiento.objects.all()
        movement = get_object_or_404(queryset, pk=pk)
        serializer = MovimientoSerializer(movement)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Movimiento.objects.all()
        movement = get_object_or_404(queryset, pk=pk)
        movement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class MovimientoLoteRetrieveView:
#     pass


class MovimientoMedicamentoView(APIView):

    def get(self, request, medicamento=None):
        if medicamento is None:
            data = {"medicamento": 5, "movimientos": [{"lote": 20, "institucion": 1, "fecha": date(2024, 7, 28)}]}
            return Response([data], status=status.HTTP_200_OK)
        else:
            if medicamento == 5:
                data = [{"lote": 20, "institucion": 1, "fecha": date(2024, 7, 28)}]
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response([], status=status.HTTP_200_OK)


class ConsumoListCreateView(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Consumo.objects.all()
        serializer = ConsumoSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        serializer = ConsumoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ConsumoRetrieveDestroyView(viewsets.ModelViewSet):

    def retrieve(self, request, pk=None):
        queryset = Consumo.objects.all()
        consumo = get_object_or_404(queryset, pk=pk)
        serializer = ConsumoSerializer(consumo)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Consumo.objects.all()
        consumo = get_object_or_404(queryset, pk=pk)
        consumo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConsumoMedicamentoAPIView(APIView):

    def get(self, request, medicamento=None):
        if medicamento is None:
            data = {
                5: {"medicamento": 5, "cantidad": 499500, "consumos": [{"institucion": 1, "cantidad": 499500, "fecha": date(2024, 7, 28)}]}
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            if medicamento == 5:
                data = [{"institucion": 1, "cantidad": 499500, "fecha": date(2024, 7, 28)}]
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response([], status=status.HTTP_200_OK)


class DisponibilidadMedicamentoAPIView(APIView):

    def get(self, request, medicamento=None):
        if medicamento is None:
            data = {5: {"medicamento": 5, "cantidad": 500, "stocks": [{"institucion": 1, "cantidad": 500}]}}
            return Response(data, status=status.HTTP_200_OK)
        else:
            if medicamento == 5:
                data = [{"institucion": 1, "cantidad": 500}]
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response([], status=status.HTTP_200_OK)


class QuiebreStockAPIView(APIView):

    def get(self, request):
        data = [{"institucion": 1, "medicamento": 5, "stock": 500, "quiebre": 500}]
        return Response(data, status=status.HTTP_200_OK)


class AlertaCaducidadLoteAPIView(APIView):

    def get(self, request):
        data = [
            {
                "id": 16,
                "codigo": "SA_NAHRD_5j2mDrL9x0xKCl_20240721_20330721",
                "medicamento": 23,
                "cantidad": 450000,
                "fecha_vencimiento": "2022-07-21",
            },
            {
                "id": 17,
                "codigo": "SE_ASBRD_8N9uLf3P8qfNCl_20240730_20330730",
                "medicamento": 34,
                "cantidad": 775000,
                "fecha_vencimiento": "2022-07-30",
            },
            {
                "id": 18,
                "codigo": "TR_ABDRG_5p3WLiH4m7eFCl_20240726_20330726",
                "medicamento": 2,
                "cantidad": 575000,
                "fecha_vencimiento": "2022-07-26",
            },
        ]
        return Response(data, status=status.HTTP_200_OK)
