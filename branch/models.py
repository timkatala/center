from django.db import models
from django.contrib.auth.models import AbstractUser


class Branch(models.Model):
	name = models.CharField(max_length=50, blank=False, unique=True)

	class Meta:
		verbose_name  =  'Filial'
		verbose_name_plural = 'Filiallar'

	def __str__(self):
		return self.name


class User(AbstractUser):
	branch = models.ForeignKey(Branch,related_name='users', on_delete=models.CASCADE)
	kassir = models.BooleanField(default=False, blank=True)
	head = models.BooleanField(default=False, blank=True)
	branch_head = models.BooleanField(default=False, blank=True)

	class Meta:
		verbose_name  =  'Foydalanuvchi'
		verbose_name_plural  =  'Foydalanuvchilar'
	def __str__(self):
		return self.username


