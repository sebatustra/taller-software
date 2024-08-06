from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import (
    Lote,
    Consumo,
    Stock,
    Movimiento
)
from .serializers import (
    LoteSerializer,
    ConsumoSerializer,
    StockSerializer,
    MovimientoSerializer
)
from rest_framework.decorators import api_view
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


# class MovimientoMedicamentoView:
#     def get():
#         pass


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
