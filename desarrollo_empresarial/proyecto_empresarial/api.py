from rest_framework import status
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from proyecto_empresarial.models import EtapaProyecto
from proyecto_empresarial.serializers import EtapaProyectoSerializer

@api_view(['GET','POST'])
def etapa_proyecto_api_view(request):

    if request.method == 'GET':
        etapas = EtapaProyecto.objects.all()
        etapas_serializer = EtapaProyectoSerializer(etapas, many = True)
        return Response(etapas_serializer.data)
    elif request.method == 'POST':
        etapa_serializer = EtapaProyectoSerializer(data = request.data)
        if etapa_serializer.is_valid():
            etapa_serializer.save()
            return Response(etapa_serializer.data)
        return Response(etapa_serializer.errors)


@api_view(['GET','PUT','DELETE'])
def etapa_proyecto_detail_api_view(request, pk=None):
    # Queryset
    etapa = EtapaProyecto.objects.filter(id=pk).first()

    # validation
    if etapa:

        # retrieve    
        if request.method == 'GET':
            etapa_serializer = EtapaProyectoSerializer(etapa)
            return Response(etapa_serializer.data, status = status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            etapa_serializer = EtapaProyectoSerializer(etapa, data = request.data)
            if etapa_serializer.is_valid():
                etapa_serializer.save()
                return Response(etapa_serializer.data,  status = status.HTTP_200_OK)
            return Response(etapa_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            etapa.delete()
            return Response({"message" : "Etapa eliminada correctamente!"}, status = status.HTTP_200_OK)
    
    return Response({"message" : "No se ha encontrado una etapa con estos datos"},
                        status = status.HTTP_400_BAD_REQUEST)