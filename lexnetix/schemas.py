from ninja import ModelSchema, Schema, Field
from .models import (
	School,
	HeadMaster,
	Member,
	Info,
	Classes
	)


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

class	InfoOne(ModelSchema):
	class	Config:
		model = Info
		model_fields = "__all__"

class	InfoOutPatch(ModelSchema):
	class	Config:
		model = Info
		model_fields = "__all__"
	info_id : str = None
	info_name : str = None
	info_phone : str = None
	info_email : str = None

class	ClassOut(ModelSchema):
	class	Config:
		model = Classes
		model_fields = ['class_name', 'class_sc']
	class_name : str = None
	class_sc : SchoolOne = None

class	ClassOne(ModelSchema):
	class	Config:
		model = Classes
		model_fields = "__all__"

class	TeacherOut(ModelSchema):
	class Config:
		model = Member
		model_fields = ['id', 'member_info']
	id : int
	member_info : InfoOut = None
	member_school : SchoolOne = None

class	NameMember(ModelSchema):
	class	Config:
		model = Info
		model_fields = ['info_name']
	info_name : str = None

class	StudentList(ModelSchema):
	class	Config:
		model = Member
		model_fields = ['id']
	id : int
	member_info : NameMember = None

class	StudentOut(ModelSchema):
	class	Config:
		model = Member
		model_fields = ['id', 'member_info']
	id : int
	member_info : InfoOut = None
	member_school : SchoolOne = None

class ClassOut(ModelSchema):
	class Config:
		model = Classes
		model_fields = "__all__"
	class_id : str = None
	class_name : str = None
	class_sc : SchoolOne = None


## POST
class	SchoolIn(Schema):
	school_name : str = None
	school_address : str = None
	school_phone : str = None
	school_email : str = None
	school_website : str = None

class	HeadmasterIn(Schema):
	headmaster_name : str
	school_id : str

class	HeadmasterUpdate(Schema):
	headmaster_name : str
	school_id : int

class	HeadmasterPatch(Schema):
	headmaster_name : str = None
	school_id : int = None

class	TeacherIn(Schema):
	info_id : int
	school_id : int

class	StudentIn(Schema):
	info_id : int
	school_id : int

class	InfoIn(Schema):
	info_id : str
	info_name : str
	info_phone : str
	info_email : str

class	InfoPatch(Schema):
	info_id : str = None
	info_name : str = None
	info_phone : str = None
	info_email : str = None

class	TeacherPatch(Schema):
	info_id : int = None
	school_id : int = None

class	StudentPatch(Schema):
	info_id : int = None
	school_id : int = None

class	ClassIn(Schema):
	class_id : str
	class_name : str
	school_id : int

class	ClassPatch(Schema):
	class_id : str = None
	class_name : str = None
	school_id : int = None

