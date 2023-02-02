from django.db import models

class ModeloBase(models.Model):
    nombre = models.CharField(max_length=60, db_index=True)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True
