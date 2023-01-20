from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from .schemas import (
	SchoolOut,
# 	Headmaster_Out,
# 	TeacherOut,
# 	Teacher_list,
	SchoolIn,
# 	StudentOut,
# 	Student_list,
# 	ClassOut,
# 	HeadmasterIn,
# 	TeacherIn
)
from .models import (
	School,
# 	HeadMaster,
# 	Teacher,
# 	Stu,
# 	Classes
)
# from django.core import serializers
# import json

router = Router()

#################
#### School #####
#################

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

@router.put('school/put/{int:schoolid}', response=dict)
def	put_school(request, schoolid : int, payload : SchoolIn):
	try:
		school = get_object_or_404(School, id=schoolid)
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
			"Status": "School updated successfully",
			"model": SchoolOut.from_orm(school)
		}
	except:
		return { "Error": "PATCH failed" }

@router.delete('school/{str:id}', response=dict)
def	delete_school(request, id : str):
	try:
		school = get_object_or_404(School, id=id)
		school.delete()
		return { "details": "School deleted successfully" }
	except:
		return { "details": "School not found" }

# ##################
# ### Headmaster ###
# ##################

# @router.get('schools/headmaster/', response=List[Headmaster_Out])
# def	Headmaster_list(request):
# 	return [Headmaster_Out.from_orm(hm) for hm in HeadMaster.objects.all()]

# @router.post('schools/headmaster/add', response=dict)
# def	headmaster_post(request, payload : HeadmasterIn = Form(...)):
# 	try:
# 		for x in School.objects.all():
# 			if x.id == int((payload.dict())['school_id']):
# 				data = { 'headmaster_name' : (payload.dict())['headmaster_name'], 'headmaster_school' : x }
# 				mode = HeadMaster.objects.create(**data)
# 				return { "details": "Headmaster posted successfully",
# 					"model": Headmaster_Out.from_orm(mode) }
# 	except:
# 			return { "details": "Headmaster posted Failed" }

# ###################
# ##### Teacher #####
# ###################

# @router.get('schools/teacher/list', response=List[TeacherOut])
# def	teacher_list(request):
# 	return [TeacherOut.from_orm(tc) for tc in Teacher.objects.all()]

# @router.post('schools/teacher/add', response=dict)
# def	teacher_post(request, payload : TeacherIn = Form(...)):
# 	try:
# 		for x in School.objects.all():
# 			if x.id == int((payload.dict())['school_id']):
# 				data = { 'teacher_name' : (payload.dict())['teacher_name'], 'teacher_id' : (payload.dict())['teacher_id'], 'teacher_phone' : (payload.dict())['teacher_phone'], 'teacher_email' : (payload.dict())['teacher_email'], 'teacher_school' : x }
# 				mode = Teacher.objects.create(**data)
# 				return { "details": "Teacher posted successfully",
# 					"model": TeacherOut.from_orm(mode) }
# 	except:
# 			return { "details": "Teacher posted Failed" }
