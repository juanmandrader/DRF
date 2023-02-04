from rest_framework.response import Response
from rest_framework.views import APIView
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
