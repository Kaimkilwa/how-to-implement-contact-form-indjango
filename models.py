from django.db import models

# Create your models here.
class ContactModel(models.Model):
	name = models.CharField(max_length = 70, blank= True, null = True)
	email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	comments = models.TextField()

	class Meta:
		verbose_name_plural ="Contact"

	def  __str__(self):
		return self.name
