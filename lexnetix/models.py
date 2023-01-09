from django.db import models

# Create your models here.
class	School(models.Model):
	school_name = models.CharField(max_length=100)
	school_phone = models.CharField(max_length=10)
	school_address = models.CharField(max_length=100)
	school_email = models.CharField(max_length=100)
	school_website = models.CharField(max_length=100)

# class	HeadMaster(models.Model):
# 	headmaster_name = models.CharField(max_length=100)
# 	headmaster_phone = models.CharField(max_length=10)
# 	headmaster_email = models.CharField(max_length=100)
# 	headmaster_school = models.ForeignKey(School, on_delete=models.CASCADE)

# class	Teacher(models.Model):
# 	Teacher_name = models.CharField(max_length=100)
# 	Teacher_phone = models.CharField(max_length=10)
# 	Teacher_email = models.CharField(max_length=100)

