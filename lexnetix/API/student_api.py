from ninja import Router, NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404
from lexnetix.schemas import (
	StudentOut,
	StudentList,
	StudentIn,
	StudentPatch
)
from lexnetix.models import Member, Info, School


router = Router()

@router.get('schools/student/get', response=List[StudentList], tags=['Student'])
def	Student_List(request):
	return [StudentList.from_orm(st) for st in Member.objects.filter(member_role=2)]

@router.get('schools/{int:sc_id}/student/get/', response=List[StudentList], tags=['Student'])
def	Student_in_sc(request, sc_id : int):
	sl = Member.objects.filter(member_role=2, member_school_id=sc_id)
	return [StudentList.from_orm(st) for st in sl]

@router.post('schools/student/add', response={200:dict, 404:dict}, tags=['Student'])
def	Student_post(request, payload : StudentIn):
	try:
		info = get_object_or_404(Info, id=payload.dict()['info_id'])
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		data = { 'member_info' : info, 'member_school' : sc, 'member_role' : 2 }
		mode = Member.objects.create(**data)
		return 200,{ "details": "Student posted successfully",
				"model": StudentOut.from_orm(mode) }
	except:
		return 404,{ "details": "Student posted Failed" }

@router.put('schools/student/put/{int:update_id}', response={200:dict, 404:dict}, tags=['Student'])
def	Student_put(request, update_id : int, payload : StudentIn):
	try:
		st = get_object_or_404(Member, id=update_id)
		info = get_object_or_404(Info, id=payload.dict()['info_id'])
		sc = get_object_or_404(School, id=payload.dict()['school_id'])
		setattr(st, 'member_info', info)
		setattr(st, 'member_school', sc)
		st.save()
		return 200,{ "Status": "Student updated successfully",
				"model": StudentOut.from_orm(st) }
	except:
		return 404,{ "Status": "Student updated Failed" }

@router.patch('schools/student/patch/{int:update_id}', response={200:dict, 404:dict}, tags=['Student'])
def	student_patch(request, update_id : int, payload : StudentPatch):
	try:
		stu = get_object_or_404(Member, id=update_id)
		data = payload.dict(exclude_unset=True, exclude_none=True)
		try :
			info = get_object_or_404(Info, id=data['info_id'])
			setattr(stu, 'member_info', info)
		except:
			pass
		try:
			sc = get_object_or_404(School, id=data['school_id'])
			setattr(stu, 'member_school', sc)
		except:
			pass
		stu.save()
		return 200,{ "Status": "Teacher updated successfully",
				"model": StudentOut.from_orm(stu) }
	except:
		return 404,{ "Status": "Teacher updated Failed" }

@router.delete('schools/student/delete/{int:student_id}', response={200:dict, 404:dict}, tags=['Student'])
def	student_delete(request, student_id : int):
	try:
		st = get_object_or_404(Member, id=student_id)
		st.delete()
		return 200,{ "Status": "Student deleted successfully" }
	except:
		return 404,{ "Status": "Student deleted Failed" }
