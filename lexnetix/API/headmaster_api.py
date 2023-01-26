from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from lexnetix.schemas import (
    Headmaster_Out,
    HeadmasterIn,
	HeadmasterUpdate,
    HeadmasterPatch,
)
from lexnetix.models import HeadMaster, School


router = Router()
@router.get('schools/headmaster/', response=List[Headmaster_Out], tags=['Headmaster'])
def	Headmaster_list(request):
	return [Headmaster_Out.from_orm(hm) for hm in HeadMaster.objects.all()]

@router.post('schools/headmaster/add', response=dict, tags=['Headmaster'])
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

@router.put('schools/headmaster/put/{int:headmaster_id}', response=dict, tags=['Headmaster'])
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

@router.patch('schools/headmaster/patch/{int:headmaster_id}', response=dict, tags=['Headmaster'])
def	headmaster_patch(request, headmaster_id : int, payload : HeadmasterPatch):
	try:
		hm = get_object_or_404(HeadMaster, id=headmaster_id)
		data = payload.dict(exclude_unset=True, exclude_none=True)
		try:
			sc = get_object_or_404(School, id=data['school_id'])
			setattr(hm, 'headmaster_school', sc)
		except:
			pass
		for key, value in data.items():
			setattr(hm, key, value)
		hm.save()
		return { "Status": "Headmaster updated successfully",
	  			"model": Headmaster_Out.from_orm(hm) }
	except:
		return { "Status": "Headmaster updated Failed" }

@router.delete('schools/headmaster/delete/{int:headmaster_id}', response=dict, tags=['Headmaster'])
def	headmaster_delete(request, headmaster_id : int):
	try:
		hm = get_object_or_404(HeadMaster, id=headmaster_id)
		hm.delete()
		return { "Status": "Headmaster deleted successfully" }
	except:
		return { "Status": "Headmaster deleted Failed" }
