from django.db import models
from django.utils import timezone
import datetime
from django.utils.html import format_html

# MONTHS = (
# 	('Yanvar', 'Yanvar'),
# 	('Fevral', 'Fevral'),
# 	('Mart','Mart'),
# 	('Aprel','Aprel'),
# 	('May', 'May'),
# 	('Iyun', 'Iyun'),
# 	('Iyul', 'Iyul'),
# 	('Avgust','Avgust'),
# 	('Sentyabr','Sentyabr'),
# 	('Oktyabr','Oktyabr'),
# 	('Noyabr','Noyabr'),
# 	('Dekabr','Dekabr'),
# 	)
MONTHS = ['Yanvar',
	'Fevral',
	'Mart',
	'Aprel',
	'May', 
	'Iyun',
	'Iyul',
	'Avgust',
	'Sentyabr',
	'Oktyabr',
	'Noyabr',
	'Dekabr',
	]
YEARS = (
	(2020, 2020),
	(2021,2021),
	(2022,2022),
	(2023,2023),
	(2024, 2024),
	(2025, 2025),
	)


class Teacher(models.Model):
	name = models.CharField(max_length=50, blank=True, verbose_name="Ismi")
	subject = models.CharField(max_length=100, blank=True, verbose_name="Fan")

	def __str__(self):
		return self.name 


class Lesson(models.Model):
	teacher = models.ForeignKey(Teacher, verbose_name="o'qituvchi",on_delete=models.CASCADE)
	schedule = models.CharField(max_length=100)

	def __str__(self):
		return self.schedule


class Student(models.Model):
	teacher = models.ManyToManyField(Teacher, related_name='students', verbose_name="o'qituvchisi")
	charachteristics = models.TextField(max_length=30, blank=True, verbose_name="Ta'rif")
	name = models.CharField(max_length=50, blank=True, verbose_name="FISH")
	phone_number = models.CharField(max_length=20, blank=True,default='-', verbose_name="Tel. nomeri")
	fathers_phone = models.CharField(max_length=20, blank=True,default='-', verbose_name="Otasing tel.")
	mothers_phone = models.CharField(max_length=20, blank=True,default='-', verbose_name="Onasing tel.")

	def __str__(self):
		return self.name 

	# @property
	# def model_two_other_field(self):
	# 	return ', '.join([m2.percent for m2 in self.payments.all()])


class Contract(models.Model):
	teacher = models.ForeignKey(Teacher, related_name='contracts', verbose_name="o'qituvchisi",on_delete=models.CASCADE)
	student = models.ForeignKey(Student, related_name='contracts', verbose_name="o'quvchisi",on_delete=models.CASCADE)
	percent = models.IntegerField(default=50)
	price = models.IntegerField(default=0)
	group = models.CharField(max_length=100, choices=[], blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)
	
	class Meta:
		unique_together = ('teacher', 'student',)
	def __str__(self):
		return f'{self.teacher.name}-{self.student.name}'

class Payment(models.Model):
	YEAR_CHOICES = [(f'{m} {y}',f'{m} {y}') for y in range(2020, 2026) for m in MONTHS]
	MONTH_CHOICE = [(m,m) for m in range(1,13)]
	contract = models.ForeignKey(Contract, related_name='payments',on_delete=models.CASCADE)
	period = models.CharField(choices=YEAR_CHOICES,
	     	default=f'{MONTHS[datetime.datetime.now().month-1]} {datetime.datetime.now().year}', max_length=20)
	teacher = models.ForeignKey(Teacher, blank=True, related_name='payments', verbose_name="o'qituvchisi",on_delete=models.CASCADE)
	student = models.ForeignKey(Student, blank=True, related_name='payments', verbose_name="o'quvchisi",on_delete=models.CASCADE)	
	date = models.DateTimeField(auto_now_add=True, verbose_name="san'a")
	has_to_pay = models.IntegerField(default=0)
	percent = models.IntegerField(default=50, verbose_name='foiz')
	paid = models.IntegerField(default=0)

	class Meta:
		unique_together=('teacher', 'student' , 'period')
	def save(self, *args, **kwargs):
		#self.contract = Contract.objects.get_or_create(teacher=self.teacher, student=self.student)
		if self.contract:
			#self.percent = self.contract.percent
			self.teacher = self.contract.teacher
			self.student = self.contract.student
			if not self.has_to_pay:
				self.has_to_pay = self.contract.price
		super().save(*args,**kwargs)




