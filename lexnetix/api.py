from ninja import Router
from typing import List
from .schemas import SchoolOut
from .models import School
import json

router = Router()

@router.get('school/', response=List[SchoolOut])

def	School_list(request):
	qs = School.objects.all()
	return qs
