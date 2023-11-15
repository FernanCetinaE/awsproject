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
    alumno = {}
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
        return JsonResponse(alumnos, status=200, safe=False)


    elif request.method == 'PUT':
        data = json.loads(request.body)
        
        if not data:
            return JsonResponse({'error': 'Datos faltantes'}, status=400)
        if 'nombres' in data:
            if not isinstance(data['nombres'], str):
                return JsonResponse({'error': 'El campo nombres debe ser una cadena de caracteres'}, status=400)
            alumno['nombres'] = data['nombres']
        if 'apellidos' in data:
            if not isinstance(data['apellidos'], str):
                return JsonResponse({'error': 'El campo apellidos debe ser una cadena de caracteres'}, status=400)
            alumno['apellidos'] = data['apellidos']
        if 'matricula' in data:
            if not isinstance(data['matricula'], str):
                return JsonResponse({'error': 'El campo matricula debe ser una cadena de caracteres'}, status=400)
            alumno['matricula'] = data['matricula']
        if 'promedio' in data:
            try:
                promedio = float(data['promedio'])
            except ValueError:
                return JsonResponse({'error': 'El campo promedio debe ser un número decimal'}, status=400)
            alumno['promedio'] = promedio
        for i, obj in enumerate(alumnos):
            if obj['id'] == data['id']:
                # Update the object with new data
                alumnos[i].update(alumno)
        return JsonResponse(alumno, status=200, safe=False)

    elif request.method == 'DELETE':
        filtered = [alumno for alumno in alumnos if alumno['id'] == pk]
        if pk is None:
            return JsonResponse({'error': 'Alumno no encontrado'}, status=405)
        if len(filtered) == 0:
            return JsonResponse({'error': 'Alumno no encontrado'}, status=404)
        
        alumnos.remove(filtered[0])
        return JsonResponse({'message': 'Alumno eliminado correctamente'}, status=200)

    elif request.method == 'POST':
        data = json.loads(request.body)
        if not data:
            return JsonResponse({'error': 'Datos faltantes'}, status=400)
        if 'nombres' not in data or 'apellidos' not in data or 'matricula' not in data or 'promedio' not in data:
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
        if not isinstance(data['nombres'], str):
            return JsonResponse({'error': 'El campo nombres debe ser una cadena de caracteres'}, status=400)
        if not isinstance(data['apellidos'], str) or data['apellidos'] is None:
            return JsonResponse({'error': 'El campo apellidos debe ser una cadena de caracteres'}, status=400)
        if not isinstance(data['matricula'], str):
            return JsonResponse({'error': 'El campo matricula debe ser una cadena de caracteres'}, status=400)
        try:
            promedio = int(data['promedio'])
        except ValueError:
            return JsonResponse({'error': 'El campo promedio debe ser un número decimal'}, status=400)
        alumno = {
            'id': data['id'],
            'nombres': data['nombres'],
            'apellidos': data['apellidos'],
            'matricula': data['matricula'],
            'promedio': promedio
        }
        alumnos.append(alumno)
        return JsonResponse(alumno, status=201)