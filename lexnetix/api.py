from ninja import Router
from typing import List
from .schemas import SchoolOut, School_one
from .models import School
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
