from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here...
class Ingreso(models.Model):
    TAG = (
        ('Fijo','Fijo'),
        ('Extra','Extra'),
    )
    catego = (
        ('Trabajo','Trabajo'),
        ('Familia','Familia'),  
        ('Otro','Otro'),

    )
    nombre_ingreso = models.CharField(max_length=100,null=True)
    valor = models.IntegerField(null=True)
    categoria = models.CharField(max_length=100,null=True,choices=catego)
    tag = models.CharField(max_length=100,null=True,choices=TAG)
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    usuario = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_ingreso
class Gasto(models.Model):
    TAG = (
        ('Fijo','Fijo'),
        ('Extra','Extra'),
    )
    catego = (
        ('Trabajo','Trabajo'),
        ('Mercado','Mercado'),
        ('Servicios','Servicios'),
        ('Entretenimiento','Entretenimiento'),
        ('Ropa','Ropa'),
        ('Tarjeta de crédito','Tarjeta de crédito'),
        ('Transporte','Transporte'),
        ('Educación','Educación'),
        ('Regalos','Regalos'),
        ('Arriendo','Arriendo'),
        ('Otro','Otro'),

    )
    nombre_Gasto = models.CharField(max_length=100,null=True)
    valor = models.IntegerField(null=True)
    categoria = models.CharField(max_length=100,null=True,choices=catego)
    tag = models.CharField(max_length=100,null=True,choices=TAG)
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    usuario = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_Gasto
