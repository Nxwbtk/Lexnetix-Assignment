from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from lexnetix.schemas import (
	InfoOne,
	InfoIn,
	InfoPatch,
	InfoOutPatch,

)
from lexnetix.models import Info

router = Router()
@router.get('schools/get_info/', response=List[InfoOne], tags=['Info'])
def	teacher_info_list(request):
	return [InfoOne.from_orm(info) for info in Info.objects.all()]

@router.post('schools/st_tc/add_info', response=dict, tags=['Info'])
def	teacher_info_post(request, payload : InfoIn):
	try:
		info = Info.objects.create(**payload.dict())
		return { "details": "Info posted successfully",
				"model": InfoOne.from_orm(info) }
	except:
		return { "details": "Teacher info posted Failed" }

@router.put('schools/put_info/{int:info_id}', response=dict, tags=['Info'])
def	teacher_info_put(request, info_id : int, payload : InfoIn):
	try:
		info = get_object_or_404(Info, id=info_id)
		for key, value in payload.dict().items():
			setattr(info, key, value)
		info.save()
		return { "Status": "Info updated successfully",
				"model": InfoOne.from_orm(info) }
	except:
		return { "Status": "Teacher info updated Failed" }

@router.patch('schools/patch_info/{int:info_id}', response=dict, tags=['Info'])
def	InfoPatch(request, info_id : int, payload : InfoPatch):
	try:
		info = get_object_or_404(Info, id=info_id)
		data = payload.dict(exclude_unset=True, exclude_none=True)
		for key, value in data.items():
			setattr(info, key, value)
		info.save()
		return { "Status": "Info updated successfully",
				"model": InfoOutPatch.from_orm(info) }
	except:
		return { "Status": "Teacher info updated Failed" }

@router.delete('schools/delete_info/{int:info_id}', response=dict, tags=['Info'])
def	teacher_info_delete(request, info_id : int):
	try:
		info = get_object_or_404(Info, id=info_id)
		info.delete()
		return { "Status": "Teacher info deleted successfully" }
	except:
		return { "Status": "Teacher info deleted Failed" }
