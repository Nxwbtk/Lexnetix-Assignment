from ninja import ModelSchema
from .models import School, HeadMaster, Teacher

class	SchoolOut(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_name']
	school_name : str = 'NULL'

class	School_one(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_id']
	school_id : str = 'NULL'
	school_name : str = 'NULL'
	school_phone : str = 'NULL'
	school_address : str = 'NULL'
	zipcode : str = 'NULL'
	school_email : str = 'NULL'
	school_website : str = 'NULL'

class	Headmaster_Out(ModelSchema):
	class	Config:
		model = HeadMaster
		model_fields = ['headmaster_name']
	headmaster_name : str = 'NULL'
	headmaster_school : SchoolOut = 'NULL'

class	TeacherOut(ModelSchema):
	class	Config:
		model = Teacher
		model_fields = ['teacher_name']
	teacher_name : str = 'NULL'
	teacher_id : str = 'NULL'
	teacher_phone : str = 'NULL'
	teacher_email : str = 'NULL'
	teacher_school : SchoolOut = 'NULL'

class	Teacher_list(ModelSchema):
	class	Config:
		model = Teacher
		model_fields = ['teacher_name']
	teacher_name : str = 'NULL'
