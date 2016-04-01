from django.db import models
from django.utils import timezone

class Producto(models.Model):
	#author = models.ForeignKey('auth.User')
	nombre = models.CharField(max_length=200)
    #text = models.TextField()
	fechaRegistro = models.DateTimeField(
		default=timezone.now)
	fechaCompra = models.DateTimeField(
		blank=True, null=True)

	def compra(self):
		self.fechaCompra = timezone.now()
		self.save()

	def __str__(self):
		return self.nombre
