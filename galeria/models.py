from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




class Fotografia(models.Model):

    OPCOES = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA','Galaxia'),
        ('PLANETA', 'Planeta')
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES,default='')
    descricao = models.TextField(null=False, blank=False)
    publicada = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d',blank=True)
    data_foto = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )
    
    def __str__(self):
        return self.nome
