from django.db import models
# from .models import Contact_Staff

# Create your models here.
class	School(models.Model):
	school_name = models.CharField(max_length=100)
	school_phone = models.CharField(max_length=10)
	school_address = models.CharField(max_length=100)
	school_email = models.CharField(max_length=100)
	school_website = models.CharField(max_length=100)


# class	Teacher(models.Model):
# 	Teacher_name = models.CharField(max_length=100)
# 	Teacher_phone = models.CharField(max_length=10)
# 	Teacher_email = models.CharField(max_length=100)

class	Contact_Staff(models.Model):
	staff_id = models.CharField(max_length=5, primary_key=True)
	staff_name = models.CharField(max_length=100)
	staff_phone = models.CharField(max_length=10)
	staff_email = models.CharField(max_length=100)
	staff_school = models.ForeignKey(School, on_delete=models.CASCADE)

class	HeadMaster(models.Model):
	headmaster_name = models.CharField(max_length=100)
	# headmaster_info = Contact_Staff()
	headmaster_school = models.OneToOneField(School, on_delete=models.CASCADE)
