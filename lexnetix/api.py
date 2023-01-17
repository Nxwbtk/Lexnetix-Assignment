from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from .schemas import (
	SchoolOut,
	Headmaster_Out,
	TeacherOut,
	Teacher_list,
	SchoolIn,
	StudentOut,
	Student_list,
	ClassOut,
	HeadmasterIn
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

@router.get('schools', response=List[SchoolOut])
def	list_school(request):
	return [SchoolOut.from_orm(school) for school in School.objects.all()]

@router.get('schools/{str:id}', response={ 200 : SchoolOut, 404 : dict })
def	get_school(request, id : str):
	try:
		return 200, get_object_or_404(School, id=id)
	except:
		return 404, { 'details' : 'Not found' }

@router.post('school/add', response=dict)
def	post_school(request, payload : SchoolIn = Form(...)):
	school = School.objects.create(**payload.dict())
	return {
		"details": "School posted successfully",
		"model": SchoolOut.from_orm(school)
	}

@router.put('school/{str:id}', response=dict)
def	put_school(request, id : str, payload : SchoolIn = Form(...)):
	try:
		school = get_object_or_404(School, id=id)
		for key, value in payload.dict().items():
			setattr(school, key, value)
		school.save()
		return {
			"details": "School updated successfully",
			"model": SchoolOut.from_orm(school)
		}
	except:
		return { "details": "School not found" }

@router.patch('school/{str:id}', response=dict)
def	patch_school(request, id : str, payload : SchoolIn = Form(...)):
	try:
		school = get_object_or_404(School, id=id)
		for key, value in payload.dict(exclude_none=True).items():
			setattr(school, key, value)
		school.save()
		return {
			"details": "School updated successfully",
			"model": SchoolOut.from_orm(school)
		}
	except:
		return { "details": "School not found" }

@router.delete('school/{str:id}', response=dict)
def	delete_school(request, id : str):
	try:
		school = get_object_or_404(School, id=id)
		school.delete()
		return { "details": "School deleted successfully" }
	except:
		return { "details": "School not found" }

@router.get('schools/headmaster/', response=List[Headmaster_Out])
def	Headmaster_list(request):
	return [Headmaster_Out.from_orm(hm) for hm in HeadMaster.objects.all()]

@router.post('schools/headmaster/add', response={ 200 : dict, 404 : dict })
def	headmaster_post(request, payload : HeadmasterIn = Form(...)):
	# test = get_object_or_404(School, school_id=payload.school_id)
	try:
		print(" :(( ")
		HeadMaster.objects.create(**payload.dict())
		return 200, { 'details' : 'Headmaster posted successfully' }
	except:
		return 404, { 'details' : 'not found' }


# @router.get('schools/headmaster/{name}', response=List[Headmaster_Out])
# def	Headmaster_list(request, name):
# 	hm = HeadMaster.objects.filter(headmaster_name=name)
# 	if list(hm) != []:
# 		return hm
# 	return [{}]

# @router.get('schools/headmaster', response=List[Headmaster_Out])
# def	Headmaster_list(request):
# 	hm = HeadMaster.objects.all()
# 	if list(hm) != []:
# 		return hm
# 	return [{}]

# @router.get('schools/teacher/list/{id}', response=List[TeacherOut])
# def	Teacher_one(request, id):
# 	tc = Teacher.objects.filter(teacher_id=id)
# 	if list(tc) != []:
# 		return Teacher.objects.filter(teacher_id=id)
# 	return [{}]

# @router.get('schools/teacher/list', response=List[Teacher_list])
# def	Teacher_one(request):
# 	tc = Teacher.objects.all()
# 	if list(tc) != []:
# 		return tc
# 	return [{}]

# @router.get('school/{sc_id}/students', response=List[StudentOut])
# def	StudentList(request, sc_id):
# 	dek = Stu.objects.all()
# 	# test = {}
# 	for x in dek:
# 		print(x.stu_sc.school_id)
# 		res = Stu.objects.filter(stu_sc__school_id=sc_id)
# 	if list(res) != []:
# 		return res
# 	return [{}]

# @router.get('school/{sc}/students/{id}', response=List[Student_list])
# def	StudentDetail(request, id, sc):
# 	sc_id = School.objects.all()
# 	for x in sc_id:
# 		if x.school_id == sc:
# 			dek = Stu.objects.filter(stu_id=id)
# 			if list(dek) != []:
# 				return dek
# 	return [{}]

# @router.get('school/{sc_id}/classes', response=List[ClassOut])
# def	ClassList(request, sc_id):
# 	dek = Classes.objects.all()
# 	for x in dek:
# 		res = Classes.objects.filter(class_sc__school_id=sc_id)
# 		if list(res) != []:
# 			return res
# 		return [{}]
# ## POST

# @router.post('schools/add', response=List[School_post])
# def	School_post(request):
# 	body_unicode = request.body.decode('utf-8')
# 	body = json.loads(body_unicode)
# 	if School.objects.filter(school_id=body['school_id']).exists() == True:
# 		return School.objects.filter(school_id=body['school_id'])
# 	try:
# 		sc = School.objects.create(school_id=body['school_id'], school_name=body['school_name'], school_phone=body['school_phone'], school_address=body['school_address'], school_email=body['school_email'], school_website=body['school_website'])
# 		sc.save()
# 		data = School.objects.filter(school_id=body['school_id'])
# 		return data
# 	except:
# 		return [{}]

# @router.post('school/headmaster/add', response={ 200 : Headmaster_Out , 404 : dict})
# def	Headmaster_post(request, payload : Headmaster_post):
# 	try:
# 		sc_valid = get_object_or_404(School ,school_id=payload.headmaster_school)
# 		if list(sc_valid) != []:
# 			print(sc_valid)
# 			# hm = HeadMaster.objects.create(headmaster_name=body['headmaster_name'], headmaster_school=sc_valid)
# 			# print(sc_valid)
# 			# hm.save()
# 			# return HeadMaster.objects.all()
# 		return 200, Headmaster_Out
# 	except:
# 		return 404, { "error" : "not found" }

	# try :
	# 	print(type(body['headmaster_school']))
	# 	hm = HeadMaster.objects.create(headmaster_name=body['headmaster_name'], headmaster_school=body['headmaster_school'])
	# 	print("test")
	# 	hm.save()
	# 	data = HeadMaster.objects.filter(headmaster_name=body['headmaster_name'])
	# 	return data
	# except:
	# 	return [{}]
	# if HeadMaster.objects.filter(headmaster_name=body['headmaster_name']).exists() == True:
	# 	return HeadMaster.objects.filter(headmaster_name=body['headmaster_name'])
	# try:
	# 	hm = HeadMaster.objects.create(headmaster_name=body['headmaster_name'])
	# 	print(hm)
	# 	hm.save()
	# 	data = HeadMaster.objects.filter(headmaster_name=body['headmaster_name'])
	# 	return data
	# except:
	# 	return [{}]
# api = NinjaAPI()
# @router.post('school/headmaster/add')
# def create_data(request, item: Headmaster_post):
# 	# print(item.dict())
# 	test = HeadMaster.objects.create(item.dict())
# 	return [{}]

