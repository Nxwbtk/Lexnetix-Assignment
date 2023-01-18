from django.db import models

# Create your models here.
class	School(models.Model):
	school_id = models.CharField(max_length=5)
	school_name = models.CharField(max_length=100)
	school_address = models.CharField(max_length=100)
	school_phone = models.CharField(max_length=10, null=True, blank=True)
	school_email = models.CharField(max_length=100, null=True, blank=True)
	school_website = models.CharField(max_length=100, null=True, blank=True)

class	HeadMaster(models.Model):
	headmaster_name = models.CharField(max_length=100)
	headmaster_school = models.OneToOneField(School, on_delete=models.CASCADE)

class	Teacher(models.Model):
	teacher_id = models.CharField(max_length=5, blank=True, null=True)
	teacher_name = models.CharField(max_length=100, blank=True)
	teacher_phone = models.CharField(max_length=10, blank=True, null=True)
	teacher_email = models.CharField(max_length=100, default='teacher@gmail.com', blank=True, null=True)
	teacher_school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True)

class	Stu(models.Model):
	stu_id = models.CharField(max_length=10)
	stu_fname = models.CharField(max_length=20)
	stu_lname = models.CharField(max_length=20)
	stu_phone = models.CharField(max_length=10)
	stu_email = models.CharField(max_length=100)
	stu_sc = models.ForeignKey(School, on_delete=models.CASCADE)
	stu_class = models.ForeignKey('Classes', on_delete=models.CASCADE, null=True)

class	Classes(models.Model):
	class_id = models.CharField(max_length=10)
	class_name = models.CharField(max_length=100)
	class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	class_sc = models.ForeignKey(School, on_delete=models.CASCADE)
