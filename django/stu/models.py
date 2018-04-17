from django.db import models


# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=128, unique=False)
	email = models.CharField(max_length=128, unique=True)
	photo = models

	def __str__(self):
		return self.name


class Company(models.Model):
	name = models.CharField(max_length=128, unique=True)
	about = models.CharField(max_length=512, unique=False)

	def __str__(self):
		return self.name


class Job(models.Model):
	pos = models.CharField(max_length=64, unique=False)
	company = models.ForeignKey('Company', on_delete=models.CASCADE)
	skills = models.CharField(max_length=264, unique=False)

	class Meta:
		unique_together = ('pos', 'company')

	def __str__(self):
		return "%s (%s)"%(self.pos,self.company)


class Application(models.Model):
	student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
	job_id = models.ForeignKey('Job', on_delete=models.CASCADE)
	status = models.CharField(max_length=12, unique=False)

	class Meta:
		unique_together = ('student_id', 'job_id')

	def __str__(self):
		return "#%d"%(self.pk)

