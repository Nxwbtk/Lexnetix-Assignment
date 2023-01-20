from django.contrib import admin
from .models import (
	School,
	HeadMaster,
    Info,
    Member,
	Classes
)

# Register your models here.
admin.site.register(School)
admin.site.register(HeadMaster)
admin.site.register(Info)
admin.site.register(Member)
admin.site.register(Classes)
