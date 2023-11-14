from django.shortcuts import render

# Create your models here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
profesores = []

@csrf_exempt
def profesor_detail(request, pk=None):
    profesor = {}
    # try:
    #     if(pk is None and request.method == 'GET'):
    #         return JsonResponse(profesores, status=200, safe=False)
    #     profesor = next(profesor for profesor in profesores if profesor['id'] == pk)
    # except StopIteration:
    #     return JsonResponse({'error': 'Profesor no encontrado'}, status=404)

    if request.method == 'GET':
        #filtrar por id profesores
        if(pk is not None):
            filtered = [profesor for profesor in profesores if profesor['id'] == pk]
            if len(filtered) == 0:
                return JsonResponse({'error': 'Profesor no encontrado'}, status=404)
            else:
                return JsonResponse(filtered[0], status=200)
        return JsonResponse(profesores, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        if not data:
            return JsonResponse({'error': 'Datos faltantes'}, status=400)
        if 'numeroEmpleado' in data:
            if not isinstance(data['numeroEmpleado'], str):
                return JsonResponse({'error': 'El campo numeroEmpleado debe ser una cadena de caracteres'}, status=400)
            profesor['numeroEmpleado'] = data['numeroEmpleado']
        if 'nombres' in data:
            if not isinstance(data['nombres'], str):
                return JsonResponse({'error': 'El campo nombres debe ser una cadena de caracteres'}, status=400)
            profesor['nombres'] = data['nombres']
        if 'apellidos' in data:
            if not isinstance(data['apellidos'], str) or data['apellidos'] is None:
                return JsonResponse({'error': 'El campo apellidos debe ser una cadena de caracteres'}, status=400)
            profesor['apellidos'] = data['apellidos']
        if 'horasClase' in data:
            try:
                horasClase = int(data['horasClase'])
            except ValueError:
                return JsonResponse({'error': 'El campo horasClase debe ser un número entero'}, status=400)
            profesor['horasClase'] = horasClase
        return JsonResponse(profesor, status=200)

    elif request.method == 'DELETE':
        profesores.remove(profesor)
        return JsonResponse({'message': 'Profesor eliminado correctamente'}, status=201)

    elif request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        if not data:
            return JsonResponse({'error': 'Datos faltantes'}, status=400)
        if 'numeroEmpleado' not in data or 'nombres' not in data or 'apellidos' not in data or 'horasClase' not in data:
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
        if not isinstance(data['numeroEmpleado'], int):
            return JsonResponse({'error': 'El campo numeroEmpleado debe ser una cadena de caracteres'}, status=400)
        if not isinstance(data['nombres'], str):
            return JsonResponse({'error': 'El campo nombres debe ser una cadena de caracteres'}, status=400)
        if not isinstance(data['apellidos'], str) or data['apellidos'] is None:
            return JsonResponse({'error': 'El campo apellidos debe ser una cadena de caracteres'}, status=400)
        try:
            horasClase = int(data['horasClase'])
        except ValueError:
            return JsonResponse({'error': 'El campo horasClase debe ser un número entero'}, status=400)
        profesor = {
            'id': len(profesores) + 1,
            'numeroEmpleado': data['numeroEmpleado'],
            'nombres': data['nombres'],
            'apellidos': data['apellidos'],
            'horasClase': horasClase
        }
        profesores.append(profesor)
        return JsonResponse(profesor, status=201)