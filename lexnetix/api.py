from ninja import Router
from typing import List
from .schemas import SchoolOut, School_one, Headmaster_Out
from .models import School, HeadMaster, Contact_Staff
import json

router = Router()

@router.get('schools/', response=List[SchoolOut])
def	School_list(request):
	sc = School.objects.all()
	return sc

@router.get('schools/{name}/', response=List[School_one])
def	School_one(request, name):
	sc = School.objects.filter(school_name=name)

	if list(sc) != []:
		return School.objects.filter(school_name=name)
	return [{}]

@router.get('schools/headmaster/{name}', response=List[Headmaster_Out])
def	Headmaster_list(request, name):
	hm = HeadMaster.objects.filter(headmaster_name=name)
	if list(hm) != []:
		return hm
	return [{}]
