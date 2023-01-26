from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from lexnetix.schemas import (
	ClassOut,
	ClassIn,
	ClassPatch,
	ClassOne

)
from lexnetix.models import Classes, School


router = Router()
@router.get('schools/class/get', response=List[ClassOut], tags=['Class'])
def	Class_List(request):
	return [ClassOut.from_orm(cl) for cl in Classes.objects.all()]

@router.get('schools/{int:sc_id}/class/get/', response=List[ClassOut], tags=['Class'])
def	Class_in_sc(request, sc_id : int):
	cl = Classes.objects.filter(class_sc_id=sc_id)
	return [ClassOut.from_orm(subject) for subject in cl]

@router.post('schools/class/add', response=dict, tags=['Class'])
def	Class_post(request, payload : ClassIn):
	try:
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		data = { 'class_id' : payload.dict()['class_id'], 'class_name' : payload.dict()['class_name'], 'class_sc' : sc }
		mode = Classes.objects.create(**data)
		print(mode.class_sc)
		return { "Status": "Class posted successfully",
				"model": ClassOut.from_orm(mode) }
	except:
		return { "Status": "Class posted Failed" }

@router.put('schools/class/put/{int:update_id}', response=dict, tags=['Class'])
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

@router.patch('schools/class/patch/{int:update_id}', response=dict, tags=['Class'])
def	Class_patch(request, update_id : int, payload : ClassPatch):
	try:
		subject = get_object_or_404(Classes, id=update_id)
		data = payload.dict(exclude_unset=True, exclude_none=True)
		for key, value in data.items():
			setattr(subject, key, value)
		try:
			sc = get_object_or_404(School, id=data['school_id'])
			setattr(subject, 'class_sc', sc)
		except:
			pass
		subject.save()
		return { "Status": "Class updated successfully",
				"model": ClassOut.from_orm(subject) }
	except:
		return { "Status": "Class updated Failed" }

@router.delete('schools/class/delete/{int:class_id}', response=dict, tags=['Class'])
def	Class_delete(request, class_id : int):
	try:
		cl = get_object_or_404(Classes, id=class_id)
		cl.delete()
		return { "Status": "Class deleted successfully" }
	except:
		return { "Status": "Class deleted Failed" }

