from ninja import ModelSchema
from .models import School

class	SchoolOut(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_name']

class	School_one(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_name']
	school_name : str = 'NULL'
	school_phone : str = 'NULL'
	school_address : str = 'NULL'
	school_email : str = 'NULL'
	school_website : str = 'NULL'
