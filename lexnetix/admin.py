from django.contrib import admin
from .models import (
	School,
	HeadMaster,
	Teacher,
	Stu
)

# Register your models here.
admin.site.register(School)
admin.site.register(HeadMaster)
admin.site.register(Teacher)
admin.site.register(Stu)
