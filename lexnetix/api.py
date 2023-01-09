from ninja import Router

router = Router()

@router.get('school/{int:id}')

def	school(request, id : int):
	data = {
		'Name': 'Nakhon Sawan',
		'id' : 1,
	}
	# print(type(id))
	if data['id'] == id:
		return data
	return {'error': 'Not found'}
