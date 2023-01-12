from django.db import models

# Create your models here.
class	School(models.Model):
	school_id = models.CharField(max_length=5, primary_key=True)
	school_name = models.CharField(max_length=100)
	school_phone = models.CharField(max_length=10)
	school_address = models.CharField(max_length=100)
	school_email = models.CharField(max_length=100)
	school_website = models.CharField(max_length=100)

class	HeadMaster(models.Model):
	headmaster_name = models.CharField(max_length=100)
	headmaster_school = models.OneToOneField(School, on_delete=models.CASCADE)

class	Teacher(models.Model):
	teacher_id = models.CharField(max_length=5, primary_key=True)
	teacher_name = models.CharField(max_length=100)
	teacher_phone = models.CharField(max_length=10)
	teacher_email = models.CharField(max_length=100, default='teacher@gmail.com')
	teacher_school = models.ForeignKey(School, on_delete=models.CASCADE)

class	Stu(models.Model):
	stu_id = models.CharField(max_length=10)
	stu_fname = models.CharField(max_length=20)
	stu_lname = models.CharField(max_length=20)
	stu_phone = models.CharField(max_length=10)
	stu_email = models.CharField(max_length=100)
	stu_sc = models.ForeignKey(School, on_delete=models.CASCADE)
