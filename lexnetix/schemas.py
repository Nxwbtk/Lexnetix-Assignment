from ninja import ModelSchema
from .models import School

class	SchoolOut(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_name', 'school_phone', 'school_address', 'school_email']
