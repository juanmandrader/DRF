from django.db import models
from desarrollo_empresarial.models import ModeloBase
from geolocalizacion.models import Pais, Departamento, Municipio, DivisionTerritorial, Barrio
from personal.models import Profesion, Ocupacion, NivelEstudio

class EtapaProyecto(ModeloBase):
    pass


class ActividadEconomica(ModeloBase):
    pass


class TamanoEmpresa(ModeloBase):
    pass


class TipoSociedad(ModeloBase):
    pass


class ProyectoEmpresarial(models.Model):
    nombre = models.CharField(max_length=60, db_index=True)
    descripcion = models.TextField()
    etapa = models.ForeignKey(EtapaProyecto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    actividad_economica = models.ForeignKey(ActividadEconomica, on_delete=models.CASCADE)
    cantidad_empleados = models.IntegerField()
    facturacion_mensual_aprox = models.IntegerField()
    productos = models.CharField(max_length=1000)
    servicios = models.CharField(max_length=1000)
    tipo_mercado = models.CharField(max_length=5)
    numero_integrantes = models.SmallIntegerField()
    persona_contacto = models.ForeignKey("Integrante", on_delete=models.CASCADE, null=True)


class Integrante(models.Model):
    nombre_completo = models.CharField(max_length=80, db_index=True)
    cargo = models.CharField(max_length=30)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.CASCADE)
    nivel_estudio_id = models.ForeignKey(NivelEstudio, on_delete=models.CASCADE)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=2)
    es_lider = models.BooleanField()
    proyecto_empresarial = models.ForeignKey(ProyectoEmpresarial, on_delete=models.CASCADE)


class Empresa(models.Model):
    nit = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=30)
    fecha_formalizacion = models.CharField(max_length=30)
    tamano_empresa = models.ForeignKey(TamanoEmpresa, on_delete=models.CASCADE)
    tipo_sociedad_id = models.ForeignKey(TipoSociedad, on_delete=models.CASCADE)
    cubrimiento = models.CharField(max_length=1)
    proyecto_empresarial_id = models.ForeignKey(ProyectoEmpresarial, on_delete=models.CASCADE)


class ModeloNegocio(models.Model):
    quien_ayudara = models.CharField(max_length=1000)
    como_hace = models.CharField(max_length=1000)
    que_haces = models.CharField(max_length=1000)
    como_interactuas = models.CharField(max_length=1000)
    a_quien_ayudas = models.CharField(max_length=1000)
    como_alcanzarlos = models.CharField(max_length=1000)
    cual_sera_costo = models.CharField(max_length=1000)
    cuanto_ganaras = models.CharField(max_length=1000)
    proyecto_empresarial_id = models.ForeignKey(ProyectoEmpresarial, on_delete=models.CASCADE)


class InformacionContactoEmpresa(models.Model):
    celular = models.CharField(max_length=15)
    celular2 = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=60)
    instagram = models.CharField(max_length=60)
    facebook = models.CharField(max_length=60)
    pais_id = models.ForeignKey(Pais, on_delete=models.CASCADE)
    departamento_id =models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio_id = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    division_territorial_id = models.ForeignKey(DivisionTerritorial, on_delete=models.CASCADE)
    barrio_id = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    otro_barrio = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    proyecto_empresarial_id = models.ForeignKey(ProyectoEmpresarial, on_delete=models.CASCADE)
