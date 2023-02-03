from django.urls import path
from proyecto_empresarial.api import EtapaProyectoAPIView

urlpatterns=[
    path('etapa_proyecto/', EtapaProyectoAPIView.as_view(), name="etapa_proyecto_api")
]