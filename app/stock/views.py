from rest_framework import viewsets
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

class MovimientoListCreateView(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Movimiento.objects.all()
        serializer = MovimientoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MovimientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# class MovimientoRetrieveDestroyView:
#     pass


# class MovimientoLoteRetrieveView:
#     pass


# class MovimientoMedicamentoView:
#     def get():
#         pass


# class ConsumoListCreateView:
#     pass


# class ConsumoRetrieveDestroyView:
#     pass
