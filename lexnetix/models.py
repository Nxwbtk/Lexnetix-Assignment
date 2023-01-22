from django.db import models

# Create your models here.
class	School(models.Model):
	school_name = models.CharField(max_length=100)
	school_address = models.CharField(max_length=100, null=True, blank=True)
	school_phone = models.CharField(max_length=10, null=True, blank=True)
	school_email = models.CharField(max_length=100, null=True, blank=True)
	school_website = models.CharField(max_length=100, null=True, blank=True)

class	HeadMaster(models.Model):
	headmaster_name = models.CharField(max_length=100)
	headmaster_school = models.OneToOneField(School, on_delete=models.CASCADE)

class	Info(models.Model):
	info_id = models.CharField(max_length=5, blank=True, null=True)
	info_name = models.CharField(max_length=100)
	info_phone = models.CharField(max_length=10, blank=True, null=True)
	info_email = models.CharField(max_length=100, blank=True, null=True)

class	Classes(models.Model):
	class_id = models.CharField(max_length=10)
	class_name = models.CharField(max_length=100)
	class_sc = models.ForeignKey(School, on_delete=models.CASCADE)

class	Member(models.Model):
	member_info = models.OneToOneField(Info, on_delete=models.CASCADE)
	member_school = models.ForeignKey(School, on_delete=models.CASCADE)
	member_role = models.IntegerField(default=0)

