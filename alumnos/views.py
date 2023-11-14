from django.shortcuts import render

# Create your views here.
from .models import Alumno
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from alumnos.models import Alumno
import json
alumnos = []
@csrf_exempt
def alumno_detail(request, pk=None, *args, **kwargs):
    alumno = None
    # try:
    #     if(pk is None):
    #         return JsonResponse({'alumnos': alumnos}, status=200, safe=False)
    #     alumno = next(alumno for alumno in alumnos if alumno['id'] == pk)
    # except StopIteration:
    #     return JsonResponse({'error': 'Alumno no encontrado'}, status=404)

    if request.method == 'GET':
        #filtrar por id profesores
        if(pk is not None):
            filtered = [alumno for alumno in alumnos if alumno['id'] == pk]
            if filtered is None or len(filtered) == 0:
                return JsonResponse({'error': 'Profesor no encontrado'}, status=404)
            else:
                return JsonResponse(filtered[0], status=200)
        return JsonResponse(alumno, status=201)


    elif request.method == 'PUT':
        data = json.loads(request.body)
        if not data:
            return JsonResponse({'error': 'Datos faltantes'}, status=500)
        if 'nombres' in data:
            if not isinstance(data['nombres'], str):
                return JsonResponse({'error': 'El campo nombres debe ser una cadena de caracteres'}, status=500)
            alumno['nombres'] = data['nombres']
        if 'apellidos' in data:
            if not isinstance(data['apellidos'], str):
                return JsonResponse({'error': 'El campo apellidos debe ser una cadena de caracteres'}, status=500)
            alumno['apellidos'] = data['apellidos']
        if 'matricula' in data:
            if not isinstance(data['matricula'], str):
                return JsonResponse({'error': 'El campo matricula debe ser una cadena de caracteres'}, status=500)
            alumno['matricula'] = data['matricula']
        if 'promedio' in data:
            try:
                promedio = float(data['promedio'])
            except ValueError:
                return JsonResponse({'error': 'El campo promedio debe ser un número decimal'}, status=500)
            alumno['promedio'] = promedio
        return JsonResponse(alumno, status=201)

    elif request.method == 'DELETE':
        alumno = [alumno for alumno in alumnos if alumno['id'] == pk]
        if alumno is None or len(alumno) == 0:
            return JsonResponse({'error': 'Alumno no encontrado'}, status=404)
        
        alumnos.remove(alumno[0])
        return JsonResponse({'message': 'Alumno eliminado correctamente'}, status=200)

    elif request.method == 'POST':
        data = json.loads(request.body)
        if not data:
            return JsonResponse({'error': 'Datos faltantes'}, status=500)
        if 'nombres' not in data or 'apellidos' not in data or 'matricula' not in data or 'promedio' not in data:
            return JsonResponse({'error': 'Datos incompletos'}, status=500)
        if not isinstance(data['nombres'], str):
            return JsonResponse({'error': 'El campo nombres debe ser una cadena de caracteres'}, status=500)
        if not isinstance(data['apellidos'], str) or data['apellidos'] is None:
            return JsonResponse({'error': 'El campo apellidos debe ser una cadena de caracteres'}, status=500)
        if not isinstance(data['matricula'], str):
            return JsonResponse({'error': 'El campo matricula debe ser una cadena de caracteres'}, status=500)
        try:
            promedio = int(data['promedio'])
        except ValueError:
            return JsonResponse({'error': 'El campo promedio debe ser un número decimal'}, status=500)
        alumno = {
            'id': data['id'],
            'nombres': data['nombres'],
            'apellidos': data['apellidos'],
            'matricula': data['matricula'],
            'promedio': promedio
        }
        alumnos.append(alumno)
        return JsonResponse(alumno, status=201)