from ninja import ModelSchema
from .models import School, HeadMaster, Contact_Staff

class	SchoolOut(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_name']
	school_name : str = 'NULL'

class	School_one(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_name']
	school_name : str = 'NULL'
	school_phone : str = 'NULL'
	school_address : str = 'NULL'
	zipcode : str = 'NULL'
	school_email : str = 'NULL'
	school_website : str = 'NULL'


class	Contact_Staff(ModelSchema):
	class	Config:
		model = Contact_Staff
		model_fields = ['staff_id']
	staff_id : str = 'NULL'
	staff_name : str = 'NULL'
	staff_phone : str = 'NULL'
	staff_email : str = 'NULL'
	staff_school : SchoolOut

class	Headmaster_Out(ModelSchema):
	class	Config:
		model = HeadMaster
		model_fields = ['headmaster_name']
	# headmaster_info : Contact_Staff
	headmaster_school : SchoolOut
