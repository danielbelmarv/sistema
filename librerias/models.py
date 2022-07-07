from unittest.util import _MAX_LENGTH
from django.db import models





class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    precio = models.IntegerField()
    imagen= models.ImageField(upload_to='img/', verbose_name="Imagen" , null=True)
    description = models.TextField(verbose_name="Descripcion" ,null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Descripcion: " + self.description
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


class Persona (models.Model):
    id = models.AutoField(primary_key = True) 
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=40)
    password= models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    telefono = models.IntegerField

    def __str__(self):
        return '{0}, {1}'.format(self.apellido, self.nombre)
