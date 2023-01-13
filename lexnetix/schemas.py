from ninja import ModelSchema, Schema
from .models import (
	School,
	HeadMaster,
	Teacher,
	Stu,
	Classes
	)
from ninja.orm import create_schema
# from  import serializers

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

class	StudentOut(ModelSchema):
	class	Config:
		model = Stu
		model_fields = ['stu_fname', 'stu_lname']
	stu_fname : str = 'NULL'
	stu_lname : str = 'NULL'

class	ClassOut(ModelSchema):
	class	Config:
		model = Classes
		model_fields = ['class_id']
	class_id : str = 'NULL'
	class_name : str = 'NULL'
	class_teacher : Teacher_list = 'NULL'

class	Student_list(ModelSchema):
	class	Config:
		model = Stu
		model_fields = ['stu_id']
	stu_fname : str = 'NULL'
	stu_lname : str = 'NULL'
	stu_id : str = 'NULL'
	stu_phone : str = 'NULL'
	stu_email : str = 'NULL'
	stu_sc : SchoolOut = 'NULL'
	stu_class : ClassOut  = 'NULL'


## POST
class	School_post(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_id', 'school_name', 'school_phone', 'school_address', 'school_email', 'school_website']
	school_id : str = 'NULL'
	school_name : str = 'NULL'
	school_phone : str = 'NULL'
	school_address : str = 'NULL'
	school_email : str = 'NULL'
	school_website : str = 'NULL'

class	School_id_in(ModelSchema):
	class	Config:
		model = School
		model_fields = School_post.Config.model_fields

Headmaster_post = create_schema(HeadMaster, fields=['headmaster_name', 'headmaster_school'])

# class	Headmaster_post(Schema):
# 	headmaster_name : str
# 	# headmaster_school : School_one
