from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from demandas.models import Demanda
from demandas.permissions import UserIsOwnerDemanda
from demandas.serializers import DemandaSerializer


class DemandasListCreate(ListCreateAPIView):
    serializer_class = DemandaSerializer

    def get_queryset(self):
        return Demanda.objects.filter(anunciante=self.request.user)

    def perform_create(self, serializer):
        serializer.save(anunciante=self.request.user)


class DemandaCrud(RetrieveUpdateDestroyAPIView):
    serializer_class = DemandaSerializer
    queryset = Demanda.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerDemanda)


class DemandaFinalizar(APIView):
    serializer_class = DemandaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        demanda_id = kwargs['pk']
        demanda = Demanda.objects.get(id=demanda_id)
        if demanda.anunciante == self.request.user:
            demanda.status = True
            demanda.save()
            serializer = self.serializer_class(demanda, context={
                'request': request
            })
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)


