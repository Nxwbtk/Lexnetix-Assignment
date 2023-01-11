from ninja import Router
from typing import List
from .schemas import SchoolOut, School_one, Headmaster_Out, TeacherOut, Teacher_list
from .models import School, HeadMaster, Teacher
import json

router = Router()

@router.get('schools/', response=List[SchoolOut])
def	School_list(request):
	sc = School.objects.all()
	return sc

@router.get('schools/{id}/', response=List[School_one])
def	School_one(request, id):
	sc = School.objects.filter(school_id=id)

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

@router.get('schools/teacher/{id}', response=List[TeacherOut])
def	Teacher_one(request, id):
	tc = Teacher.objects.filter(teacher_id=id)
	if list(tc) != []:
		return Teacher.objects.filter(teacher_id=id)
	return [{}]

@router.get('schools/teacher', response=List[Teacher_list])
def	Teacher_one(request):
	tc = Teacher.objects.all()
	if list(tc) != []:
		return tc
	return [{}]
