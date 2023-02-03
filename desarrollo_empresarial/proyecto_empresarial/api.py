from rest_framework.response import Response
from rest_framework.views import APIView
from proyecto_empresarial.models import EtapaProyecto
from proyecto_empresarial.serializers import EtapaProyectoSerializer

class EtapaProyectoAPIView(APIView):

    def get(slef, request):
        etapa = EtapaProyecto.objects.all()
        etapa_serializer = EtapaProyectoSerializer(etapa, many = True)
        return Response(etapa_serializer.data)
