from django.db import models
from datetime import datetime




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
    
    def __str__(self):
        return f" Fotografia [nome={self.nome}]"
