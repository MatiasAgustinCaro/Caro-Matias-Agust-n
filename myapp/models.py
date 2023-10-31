from django.db import models

#Create your models here.

class Libro(models.Model):
    Id= models.AutoField(primary_key=True)
    Titulo= models.CharField(max_length=100, verbose_name='Titulo')
    Imagen= models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    Sipnosis=models.TextField(verbose_name="Sipnosis") 

    def __str__(self):
        fila= "Titulo: " + self.Titulo +  " - " + " Sipnopsis: " + self.Sipnosis 
        return fila
    
    def delete(self, using= None, keep_parents= False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()



