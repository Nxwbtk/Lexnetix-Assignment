from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from lexnetix.schemas import (
	SchoolOut,
	SchoolIn,
	StudentOut
)
from lexnetix.models import School

router = Router()

@router.get('schools', response=List[SchoolOut], tags=['School'])
def	list_school(request):
	return [SchoolOut.from_orm(school) for school in School.objects.all()]

@router.get('schools/{str:id}', response={ 200 : SchoolOut, 404 : dict }, tags=['School'])
def	get_school(request, id : str):
	try:
		return 200, get_object_or_404(School, id=id)
	except:
		return 404, { 'details' : 'Not found' }

@router.post('school/add', response=dict, tags=['School'])
def	post_school(request, payload : SchoolIn = Form(...)):
	school = School.objects.create(**payload.dict())
	return {
		"details": "School posted successfully",
		"model": SchoolOut.from_orm(school)
	}

@router.put('school/put/{int:schoolid}', response=dict, tags=['School'])
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

@router.patch('school/patch/{int:sc_id}', response=dict, tags=['School'])
def	patch_school(request, sc_id : int, payload : SchoolIn):
	try:
		school = get_object_or_404(School, id=sc_id)
		data = payload.dict(exclude_unset=True, exclude_none=True)
		for key, value in data.items():
			setattr(school, key, value)
		school.save()
		return {
			"Status": "School updated successfully",
			"model": SchoolOut.from_orm(school)
		}
	except:
		return { "Error": "PATCH failed" }

@router.delete('school/{str:id}', response=dict, tags=['School'])
def	delete_school(request, id : str):
	try:
		school = get_object_or_404(School, id=id)
		school.delete()
		return { "details": "School deleted successfully" }
	except:
		return { "details": "School not found" }
