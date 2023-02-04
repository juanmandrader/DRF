from django.urls import path
from proyecto_empresarial.api import etapa_proyecto_api_view

urlpatterns=[
    path('etapa_proyecto/', etapa_proyecto_api_view, name="etapa_proyecto_api")
]