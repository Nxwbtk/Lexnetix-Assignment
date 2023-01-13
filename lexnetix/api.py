from ninja import Router, NinjaAPI
from typing import List
from .schemas import (
	SchoolOut,
	School_one,
	Headmaster_Out,
	TeacherOut,
	Teacher_list,
	School_post,
	StudentOut,
	Student_list,
	ClassOut,
	Headmaster_post
)
from .models import (
	School,
	HeadMaster,
	Teacher,
	Stu,
	Classes
)
from django.core import serializers
import json

router = Router()
## GET

@router.get('schools/', response=List[SchoolOut])
def	School_list(request):
	sc = School.objects.all()
	return sc

@router.get('schools/{id}/', response=List[School_one])
def	School_one(request, id):
	sc = School.objects.filter(school_id=id)
	# print("hey")
	if list(sc) != []:
		return School.objects.filter(school_id=id)
	return [{}]

@router.get('schools/headmaster/{name}', response=List[Headmaster_Out])
def	Headmaster_list(request, name):
	hm = HeadMaster.objects.filter(headmaster_name=name)
	if list(hm) != []:
		return hm
	return [{}]

@router.get('schools/headmaster', response=List[Headmaster_Out])
def	Headmaster_list(request):
	hm = HeadMaster.objects.all()
	if list(hm) != []:
		return hm
	return [{}]

@router.get('schools/teacher/list/{id}', response=List[TeacherOut])
def	Teacher_one(request, id):
	tc = Teacher.objects.filter(teacher_id=id)
	if list(tc) != []:
		return Teacher.objects.filter(teacher_id=id)
	return [{}]

@router.get('schools/teacher/list', response=List[Teacher_list])
def	Teacher_one(request):
	tc = Teacher.objects.all()
	if list(tc) != []:
		return tc
	return [{}]

@router.get('school/{sc_id}/students', response=List[StudentOut])
def	StudentList(request, sc_id):
	dek = Stu.objects.all()
	# test = {}
	for x in dek:
		print(x.stu_sc.school_id)
		res = Stu.objects.filter(stu_sc__school_id=sc_id)
	if list(res) != []:
		return res
	return [{}]

@router.get('school/{sc}/students/{id}', response=List[Student_list])
def	StudentDetail(request, id, sc):
	sc_id = School.objects.all()
	for x in sc_id:
		if x.school_id == sc:
			dek = Stu.objects.filter(stu_id=id)
			if list(dek) != []:
				return dek
	return [{}]

@router.get('school/{sc_id}/classes', response=List[ClassOut])
def	ClassList(request, sc_id):
	dek = Classes.objects.all()
	for x in dek:
		res = Classes.objects.filter(class_sc__school_id=sc_id)
		if list(res) != []:
			return res
		return [{}]
## POST

@router.post('schools/add', response=List[School_post])
def	School_post(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	if School.objects.filter(school_id=body['school_id']).exists() == True:
		return School.objects.filter(school_id=body['school_id'])
	try:
		sc = School.objects.create(school_id=body['school_id'], school_name=body['school_name'], school_phone=body['school_phone'], school_address=body['school_address'], school_email=body['school_email'], school_website=body['school_website'])
		sc.save()
		data = School.objects.filter(school_id=body['school_id'])
		return data
	except:
		return [{}]

@router.post('school/headmaster/add', response=List[Headmaster_post])
def	Headmaster_post(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	if HeadMaster.objects.filter(headmaster_name=body['headmaster_name']).exists() == True:
		return HeadMaster.objects.filter(headmaster_name=body['headmaster_name'])
	try:
		hm = HeadMaster.objects.create(headmaster_name=body['headmaster_name'])
		print(hm)
		hm.save()
		data = HeadMaster.objects.filter(headmaster_name=body['headmaster_name'])
		return data
	except:
		return [{}]
# api = NinjaAPI()
# @router.post('school/headmaster/add')
# def create_data(request, item: Headmaster_post):
# 	# print(item.dict())
# 	test = HeadMaster.objects.create(item.dict())
# 	return [{}]

