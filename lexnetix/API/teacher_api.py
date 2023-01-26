from ninja import Router, NinjaAPI, Form
from typing import List
from django.shortcuts import get_object_or_404
from lexnetix.schemas import (
	TeacherOut,
	TeacherIn,
	TeacherPatch,
)
from lexnetix.models import Member, Info, School

router = Router()
@router.get('schools/teacher/get', response=List[TeacherOut], tags=['Teacher'])
def	teacher_list(request):
	return [TeacherOut.from_orm(tc) for tc in Member.objects.filter(member_role=1)]

@router.post('schools/teacher/add', response=dict, tags=['Teacher'])
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

@router.put('schools/teacher/put/{int:update_id}', response=dict, tags=['Teacher'])
def	teacher_put(request, update_id : int, payload : TeacherIn):
	try:
		tc = get_object_or_404(Member, id=update_id)
		info = get_object_or_404(Info, id=payload.dict()['info_id'])
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		setattr(tc, 'member_info', info)
		setattr(tc, 'member_school', sc)
		tc.save()
		return { "Status": "Teacher updated successfully",
				"model": TeacherOut.from_orm(tc) }
	except:
		return { "Status": "Teacher updated Failed" }

@router.patch('schools/teacher/patch/{int:update_id}', response=dict, tags=['Teacher'])
def	teacher_patch(request, update_id : int, payload : TeacherPatch):
	try:
		tc = get_object_or_404(Member, id=update_id)
		data = payload.dict(exclude_unset=True, exclude_none=True)
		try :
			info = get_object_or_404(Info, id=data['info_id'])
			setattr(tc, 'member_info', info)
		except:
			pass
		try:
			sc = get_object_or_404(School, id=data['school_id'])
			setattr(tc, 'member_school', sc)
		except:
			pass
		tc.save()
		return { "Status": "Teacher updated successfully",
				"model": TeacherOut.from_orm(tc) }
	except:
		return { "Status": "Teacher updated Failed" }

@router.delete('schools/teacher/delete/{int:teacher_id}', response=dict, tags=['Teacher'])
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
