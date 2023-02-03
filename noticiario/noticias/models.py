from django.db import models

# Create your models here.

class Noticias(models.Model):
    titulo = models.CharField(max_length=100)
    imagen1 = models.ImageField(upload_to='media', null=True)
    imagen2 = models.ImageField(upload_to='media', null=True)
    imagen3 = models.ImageField(upload_to='media', null=True)
    imagen4 = models.ImageField(upload_to='media', null=True)
    imagen5 = models.ImageField(upload_to='media', null=True)
    descripcion = models.CharField(max_length=500)
    fechaPublicacion = models.DateTimeField('Fecha de publicacion')
    
    def __str__(self):
        return f"{self.titulo}"