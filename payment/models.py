from django.db import models
from django.utils import timezone
import datetime
from django.utils.html import format_html
from branch.models import *
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

YEAR_CHOICES = [(f'{m} {y}',f'{m} {y}') for y in range(2020, 2026) for m in MONTHS]

class Teacher(models.Model):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=50, blank=True, verbose_name="Ismi")
	subject = models.CharField(max_length=100, blank=True, verbose_name="Fan")
	official = models.IntegerField(default=0, verbose_name="rasmiy oylik")

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name="O'qituvchi"
		verbose_name_plural="O'qituvchilar"

class Salary(models.Model):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)

	teacher = models.ForeignKey(Teacher, related_name='salaries',on_delete=models.CASCADE)
	period = models.CharField(choices=YEAR_CHOICES,
	     	default=f'{MONTHS[datetime.datetime.now().month-1]} {datetime.datetime.now().year}', max_length=20)
	date = models.DateTimeField(auto_now_add=True, verbose_name="to'langan san'a")
	paid = models.IntegerField(default=0, verbose_name="Hisoblandi")
	official = models.IntegerField(default=0, verbose_name="rasmiy oylik")

	class Meta:
		verbose_name="Oylik"
		verbose_name_plural="Oyliklar"
		unique_together = ('teacher','period')

	def __str__(self):
		return f'{self.teacher}ning oyligi'
# class Lesson(models.Model):
# 	teacher = models.ForeignKey(Teacher, verbose_name="o'qituvchi",on_delete=models.CASCADE)
# 	schedule = models.CharField(max_length=100)

# 	def __str__(self):
# 		return self.schedule


class Student(models.Model):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
	charachteristics = models.TextField(max_length=30, blank=True, verbose_name="Ta'rif")
	name = models.CharField(max_length=50, blank=True, verbose_name="FISH")
	phone_number = models.CharField(max_length=20, blank=True,default='-', verbose_name="Tel. nomeri")
	fathers_phone = models.CharField(max_length=20, blank=True,default='-', verbose_name="Otasing tel.")
	mothers_phone = models.CharField(max_length=20, blank=True,default='-', verbose_name="Onasing tel.")

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name="Talaba"
		verbose_name_plural="Talabalar"
	# @property
	# def model_two_other_field(self):
	# 	return ', '.join([m2.percent for m2 in self.payments.all()])


class Contract(models.Model):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)

	TIMES = [(f'{t}.00', f'{t}.00') for t in range(6, 24)]
	teacher = models.ForeignKey(Teacher, related_name='contracts', verbose_name="o'qituvchisi",on_delete=models.CASCADE)
	student = models.ForeignKey(Student, related_name='contracts', verbose_name="o'quvchisi",on_delete=models.CASCADE)
	percent = models.IntegerField(default=50)
	price = models.IntegerField(default=0)
	parity = models.CharField(max_length=5, verbose_name='Kun', choices=(
																		('Toq', 'Toq'),
																		('Juft','Juft'), ), default=1
																						)
	group_time = models.CharField(max_length=5, choices=TIMES, default=1)
	date_joined = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)
	
	class Meta:
		unique_together = ('teacher', 'student',)
		verbose_name="Shartnoma"
		verbose_name_plural="Shartnomalar"
	def __str__(self):
		return f'{self.teacher.name}-{self.student.name}'

class Payment(models.Model):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
	kassir = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	MONTH_CHOICE = [(m,m) for m in range(1,13)]
	contract = models.ForeignKey(Contract, related_name='payments',on_delete=models.CASCADE)
	period = models.CharField(choices=YEAR_CHOICES,
	     	default=f'{MONTHS[datetime.datetime.now().month-1]} {datetime.datetime.now().year}', max_length=20, verbose_name="To'lov oyi")
	teacher = models.ForeignKey(Teacher, blank=True, related_name='payments', verbose_name="o'qituvchisi",on_delete=models.CASCADE)
	student = models.ForeignKey(Student, blank=True, related_name='payments', verbose_name="o'quvchisi",on_delete=models.CASCADE)	
	date = models.DateTimeField(auto_now_add=True, verbose_name="san'a")
	has_to_pay = models.IntegerField(default=0, verbose_name="To'lanishi kerak")
	percent = models.IntegerField(default=50, verbose_name='foiz')
	paid = models.IntegerField(default=0, verbose_name="To'landi")

	class Meta:
		unique_together=('teacher', 'student' , 'period')
		verbose_name="To'lov"
		verbose_name_plural="To'lovlar"
	def save(self, *args, **kwargs):
		#self.contract = Contract.objects.get_or_create(teacher=self.teacher, student=self.student)
		if self.contract:
			#self.percent = self.contract.percent
			self.teacher = self.contract.teacher
			self.student = self.contract.student
			if not self.has_to_pay:
				self.has_to_pay = self.contract.price
		super().save(*args,**kwargs)




