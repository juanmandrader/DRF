from django.db import models
from desarrollo_empresarial.models import ModeloBase


class Pais(ModeloBase):
    pass


class Departamento(ModeloBase):
    pais = models.ForeignKey(
        Pais, on_delete=models.PROTECT, related_name="departamentos"
    )


class Municipio(ModeloBase):
    departamento = models.ForeignKey(
        Departamento, on_delete=models.PROTECT, related_name="municipios"
    )


class DivisionTerritorial(ModeloBase):
   municipio = models.ForeignKey(
        Municipio, on_delete=models.PROTECT, related_name="divisiones_territoriales"
    )


class Barrio(ModeloBase):
    division_territorial = models.ForeignKey(
        DivisionTerritorial, on_delete=models.PROTECT, related_name="barrios", unique=True
    )
