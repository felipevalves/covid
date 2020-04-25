from django.db import models

# Create your models here.
class Boletim(models.Model):

    estado = models.CharField(
        default='PR',
        max_length=2,
        null=False,
        blank=False)

    municipio = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    confirmados = models.IntegerField(
        default=0
    )
    obitos = models.IntegerField(
        default=0
    )
    descartados = models.IntegerField(
        default=0
    )
    investigacao = models.IntegerField(
        default=0
    )
    data_boletim = models.DateField()

    objetos = models.Manager()

    def __str__(self):
        return '{} {}/{}'.format(self.data_boletim.strftime("%d/%m/%Y"), self.municipio, self.estado)


