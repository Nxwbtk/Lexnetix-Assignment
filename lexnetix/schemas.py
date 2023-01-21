from ninja import ModelSchema, Schema, Field
from .models import (
	School,
	HeadMaster,
	Member,
	Info,
	Classes
	)
# from ninja.orm import create_schema


class	SchoolOut(ModelSchema):
	class	Config:
		model = School
		model_fields = "__all__"

class	SchoolOne(ModelSchema):
	class	Config:
		model = School
		model_fields = ['school_name']

class	Headmaster_Out(ModelSchema):
	class	Config:
		model = HeadMaster
		model_fields = "__all__"
	headmaster_name : str = 'NULL'
	headmaster_school : SchoolOut = 'NULL'

class	InfoOut(ModelSchema):
	class	Config:
		model = Info
		model_fields = ['info_name', 'info_phone', 'info_email']

class	ClassOut(ModelSchema):
	class	Config:
		model = Classes
		model_fields = ['class_name']
	class_name : str = None

class	TeacherOut(ModelSchema):
	# teacher_info : InfoOut = Field("member_info", alias="")
	class Config:
		model = Member
		model_fields = ['id', 'member_info']
	id : int
	member_info : InfoOut = None
	classes : ClassOut = None
	member_school : SchoolOne = None
# class	TeacherOut(ModelSchema):
# 	class	Config:
# 		model = Teacher
# 		model_fields = ['teacher_name']
# 	teacher_name : str = None
# 	teacher_id : str = None
# 	teacher_phone : str = None
# 	teacher_email : str = None
# 	teacher_school : SchoolOut = None

# class	Teacher_list(ModelSchema):
# 	class	Config:
# 		model = Teacher
# 		model_fields = ['teacher_name']
# 	teacher_name : str = 'NULL'

# class	StudentOut(ModelSchema):
# 	class	Config:
# 		model = Stu
# 		model_fields = ['stu_fname', 'stu_lname']
# 	stu_fname : str = 'NULL'
# 	stu_lname : str = 'NULL'

# class	ClassOut(ModelSchema):
# 	class	Config:
# 		model = Classes
# 		model_fields = ['class_id']
# 	class_id : str = 'NULL'
# 	class_name : str = 'NULL'
# 	class_teacher : Teacher_list = 'NULL'

# class	Student_list(ModelSchema):
# 	class	Config:
# 		model = Stu
# 		model_fields = ['stu_id']
# 	stu_fname : str = 'NULL'
# 	stu_lname : str = 'NULL'
# 	stu_id : str = 'NULL'
# 	stu_phone : str = 'NULL'
# 	stu_email : str = 'NULL'
# 	stu_sc : SchoolOut = 'NULL'
# 	stu_class : ClassOut  = 'NULL'


## POST
class	SchoolIn(Schema):
	school_name : str
	school_address : str
	school_phone : str = None
	school_email : str = None
	school_website : str = None

class	HeadmasterIn(Schema):
	headmaster_name : str
	school_id : str

class	HeadmasterUpdate(Schema):
	headmaster_name : str
	school_id : int

# class	TeacherIn(Schema):
# 	teacher_id : str = None
# 	teacher_name : str
# 	teacher_phone : str = None
# 	teacher_email : str = None
# 	school_id : str


# # class	School_id_in(ModelSchema):
# # 	class	Config:
# # 		model = School
# # 		model_fields = School_post.Config.model_fields

# # Headmaster_post = create_schema(HeadMaster, fields=['headmaster_name', 'headmaster_school'])

