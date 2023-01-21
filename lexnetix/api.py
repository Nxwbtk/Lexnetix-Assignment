from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from .schemas import (
	SchoolOut,
	Headmaster_Out,
	TeacherOut,
# 	Teacher_list,
	SchoolIn,
# 	StudentOut,
# 	Student_list,
# 	ClassOut,
	HeadmasterIn,
	HeadmasterUpdate,
# 	TeacherIn
)
from .models import (
	School,
	HeadMaster,
	Member,
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

@router.patch('school/patch/{int:sc_id}', response=dict)
def	patch_school(request, sc_id : int, payload : SchoolIn):
	try:
		# print("Test")
		school = get_object_or_404(School, id=sc_id)
		for key, value in payload.dict().items():
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

##################
### Headmaster ###
##################

@router.get('schools/headmaster/', response=List[Headmaster_Out])
def	Headmaster_list(request):
	return [Headmaster_Out.from_orm(hm) for hm in HeadMaster.objects.all()]

@router.post('schools/headmaster/add', response=dict)
def	headmaster_post(request, payload : HeadmasterIn = Form(...)):
	try:
		for x in School.objects.all():
			if x.id == int((payload.dict())['school_id']):
				data = { 'headmaster_name' : (payload.dict())['headmaster_name'], 'headmaster_school' : x }
				mode = HeadMaster.objects.create(**data)
				return { "details": "Headmaster posted successfully",
					"model": Headmaster_Out.from_orm(mode) }
		return { "details": "Headmaster posted Failed" }
	except:
			return { "details": "Headmaster posted Failed" }

@router.put('schools/headmaster/put/{int:headmaster_id}', response=dict)
def	headmaster_put(request, headmaster_id : int, payload : HeadmasterUpdate):
	try:
		hm = get_object_or_404(HeadMaster, id=headmaster_id)
		setattr(hm, 'headmaster_name', payload.dict()['headmaster_name'])
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		setattr(hm, 'headmaster_school', sc)
		hm.save()
		return { "Status": "Headmaster updated successfully",
	  			"model": Headmaster_Out.from_orm(hm) }
	except:
		return { "Status": "Headmaster updated Failed" }

# @router.patch()

@router.delete('schools/headmaster/delete/{int:headmaster_id}', response=dict)
def	headmaster_delete(request, headmaster_id : int):
	try:
		hm = get_object_or_404(HeadMaster, id=headmaster_id)
		hm.delete()
		return { "Status": "Headmaster deleted successfully" }
	except:
		return { "Status": "Headmaster deleted Failed" }

###################
##### Teacher #####
###################

@router.get('schools/teacher/get', response=List[TeacherOut])
def	teacher_list(request):
	return [TeacherOut.from_orm(tc) for tc in Member.objects.filter(member_role=1)]

# @router.post('schools/teacher/add', response=dict)
# def	teacher_post(request, payload : ):
# 	pass

@router.delete('schools/teacher/delete/{int:teacher_id}', response=dict)
def	teacher_delete(request, teacher_id : int):
	try:
		tc = get_object_or_404(Member, id=teacher_id)
		tc.delete()
		return { "Status": "Teacher deleted successfully" }
	except:
		return { "Status": "Teacher deleted Failed" }

###################
##### Student #####
###################

# @router.get('schools/student/get', response=List[StudentOut])
