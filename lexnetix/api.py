from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from .schemas import (
	SchoolOut,
	Headmaster_Out,
	InfoOut,
	InfoOne,
	TeacherOut,
# 	Teacher_list,
	SchoolIn,
	StudentOut,
	StudentList,
	ClassOut,
	HeadmasterIn,
	HeadmasterUpdate,
	TeacherIn,
	StudentIn,
	InfoIn,
	ClassIn
)
from .models import (
	School,
	HeadMaster,
	Member,
	Info,
	Classes
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

#patch not done
@router.patch('school/patch/{int:sc_id}', response=dict)
def	patch_school(request, sc_id : int, payload : SchoolIn):
	try:
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

# waiting for patch method
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
###### Info #######
###################

@router.get('schools/get_info/', response=List[InfoOne])
def	teacher_info_list(request):
	return [InfoOne.from_orm(info) for info in Info.objects.all()]

@router.post('schools/st_tc/add_info', response=dict)
def	teacher_info_post(request, payload : InfoIn):
	try:
		info = Info.objects.create(**payload.dict())
		return { "details": "Teacher info posted successfully",
				"model": InfoOne.from_orm(info) }
	except:
		return { "details": "Teacher info posted Failed" }

@router.put('schools/put_info/{int:info_id}', response=dict)
def	teacher_info_put(request, info_id : int, payload : InfoIn):
	try:
		info = get_object_or_404(Info, id=info_id)
		for key, value in payload.dict().items():
			setattr(info, key, value)
		info.save()
		return { "Status": "Teacher info updated successfully",
				"model": InfoOne.from_orm(info) }
	except:
		return { "Status": "Teacher info updated Failed" }

# waiting for patch method

@router.delete('schools/delete_info/{int:info_id}', response=dict)
def	teacher_info_delete(request, info_id : int):
	try:
		info = get_object_or_404(Info, id=info_id)
		info.delete()
		return { "Status": "Teacher info deleted successfully" }
	except:
		return { "Status": "Teacher info deleted Failed" }

###################
##### Teacher #####
###################

@router.get('schools/teacher/get', response=List[TeacherOut])
def	teacher_list(request):
	return [TeacherOut.from_orm(tc) for tc in Member.objects.filter(member_role=1)]

@router.post('schools/teacher/add', response=dict)
def	teacher_post(request, payload : TeacherIn):
	try:
		info = get_object_or_404(Info, id=payload.dict()['info_id'])
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		data = { 'member_info' : info, 'member_school' : sc, 'member_role' : 1 }
		mode = Member.objects.create(**data)
		return { "details": "Teacher posted successfully",
				"model": TeacherOut.from_orm(mode) }
	except:
		return { "details": "Teacher posted Failed" }

@router.put('schools/teacher/put/{int:update_id}', response=dict)
def	teacher_put(request, update_id : int, payload : TeacherIn):
	try:
		tc = get_object_or_404(Member, id=update_id)
		info = get_object_or_404(Info, id=payload.dict()['info_id'])
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		print(sc)
		setattr(tc, 'member_info', info)
		setattr(tc, 'member_school', sc)
		tc.save()
		return { "Status": "Teacher updated successfully",
				"model": TeacherOut.from_orm(tc) }
	except:
		return { "Status": "Teacher updated Failed" }

# waiting for patch method

@router.delete('schools/teacher/delete/{int:teacher_id}', response=dict)
def	teacher_delete(request, teacher_id : int):
	try:
		tc = get_object_or_404(Member, id=teacher_id)
		info_id = tc.member_info.id
		ifo = get_object_or_404(Info, id=info_id)
		ifo.delete()
		tc.delete()
		return { "Status": "Teacher deleted successfully" }
	except:
		return { "Status": "Teacher deleted Failed" }

###################
##### Student #####
###################

@router.get('schools/student/get', response=List[StudentList])
def	Student_List(request):
	return [StudentList.from_orm(st) for st in Member.objects.filter(member_role=2)]

@router.get('schools/{int:sc_id}/student/get/', response=List[StudentList])
def	Student_in_sc(request, sc_id : int):
	sl = Member.objects.filter(member_role=2, member_school_id=sc_id)
	return [StudentList.from_orm(st) for st in sl]

@router.post('schools/student/add', response=dict)
def	Student_post(request, payload : StudentIn):
	try:
		info = get_object_or_404(Info, id=payload.dict()['info_id'])
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		data = { 'member_info' : info, 'member_school' : sc, 'member_role' : 2 }
		mode = Member.objects.create(**data)
		return { "details": "Student posted successfully",
				"model": StudentOut.from_orm(mode) }
	except:
		return { "details": "Student posted Failed" }

@router.put('schools/student/put/{int:update_id}', response=dict)
def	Student_put(request, update_id : int, payload : StudentIn):
	try:
		st = get_object_or_404(Member, id=update_id)
		info = get_object_or_404(Info, id=payload.dict()['info_id'])
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		setattr(st, 'member_info', info)
		setattr(st, 'member_school', sc)
		st.save()
		return { "Status": "Student updated successfully",
				"model": StudentOut.from_orm(st) }
	except:
		return { "Status": "Student updated Failed" }

# waiting for patch method

@router.delete('schools/student/delete/{int:student_id}', response=dict)
def	student_delete(request, student_id : int):
	try:
		st = get_object_or_404(Member, id=student_id)
		st.delete()
		return { "Status": "Student deleted successfully" }
	except:
		return { "Status": "Student deleted Failed" }

###################
###### Class ######
###################

@router.get('schools/class/get', response=List[ClassOut])
def	Class_List(request):
	return [ClassOut.from_orm(cl) for cl in Classes.objects.all()]

@router.get('schools/{int:sc_id}/class/get/', response=List[ClassOut])
def	Class_in_sc(request, sc_id : int):
	cl = Classes.objects.filter(class_sc_id=sc_id)
	return [ClassOut.from_orm(subject) for subject in cl]

@router.post('schools/class/add', response=dict)
def	Class_post(request, payload : ClassIn):
	try:
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		data = { 'class_id' : payload.dict()['class_id'], 'class_name' : payload.dict()['class_name'], 'class_sc' : sc }
		mode = Classes.objects.create(**data)
		return { "Status": "Class posted successfully",
				"model": ClassOut.from_orm(mode) }
	except:
		return { "Status": "Class posted Failed" }

@router.put('schools/class/put/{int:update_id}', response=dict)
def	Class_put(request, update_id : int, payload : ClassIn):
	try:
		subject = get_object_or_404(Classes, id=update_id)
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		setattr(subject, 'class_id', payload.dict()['class_id'])
		setattr(subject, 'class_name', payload.dict()['class_name'])
		setattr(subject, 'class_sc', sc)
		subject.save()
		return { "Status": "Class updated successfully",
				"model": ClassOut.from_orm(subject) }
	except:
		return { "Status": "Class updated Failed" }

# waiting for patch method

@router.delete('schools/class/delete/{int:class_id}', response=dict)
def	Class_delete(request, class_id : int):
	try:
		cl = get_object_or_404(Classes, id=class_id)
		cl.delete()
		return { "Status": "Class deleted successfully" }
	except:
		return { "Status": "Class deleted Failed" }
