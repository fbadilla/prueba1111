from django.shortcuts import render
from django.http import HttpResponse
from .models import Estacion , Proyecto
import requests
from django.core.paginator import Paginator, EmptyPage

from bs4 import BeautifulSoup
import json

from django.http import HttpResponse

def obtener_informacion(request):
    url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

    proyecto_dict = {}

    for i in range(1, 30):
        payload = {'pagina_offset': i}
        response = requests.post(url, data=payload)

        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'class': 'tabla_datos'})

        for tr in table.tbody.find_all('tr'):
            tds = tr.find_all('td')
            proyecto_dict[tds[1].get_text()] = {
                'numero': tds[0].get_text(),
                'tipo': tds[2].get_text(),
                'region': tds[3].get_text(),
                'tipologia': tds[4].get_text(),
                'titular': tds[5].get_text(),
                'inversion': tds[6].get_text(),
                'fecha_presentacion': tds[7].get_text(),
                'estado': tds[8].get_text(),
            }
    for nombre, datos in proyecto_dict.items():
        proyecto = Proyecto(nombre=nombre, numero=datos['numero'], tipo=datos['tipo'],
                            region=datos['region'], tipologia=datos['tipologia'], titular=datos['titular'],
                            inversion=datos['inversion'], fecha_presentacion=datos['fecha_presentacion'],
                            estado=datos['estado'])
        proyecto.save()

    with open('proyectos.json', 'w') as f:
        json.dump(proyecto_dict, f)

    return HttpResponse('Información obtenida y guardada en proyectos.json')
    


def users(request):
    url = "http://api.citybik.es/v2/networks/bikesantiago"

# Hacer una petición GET a la API
    response = requests.get(url)

# Si la petición es exitosa (código 200), obtener el campo "stations" del objeto JSON
    if response.status_code == 200:
        data = response.json()
        stations = data["network"]["stations"]
        paginator = Paginator(stations, 10)
    try:
        page = request.GET.get('page', 1)
        users = paginator.page(page)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, "users.html", {'users': users})


def guardar_estaciones(request):
    # URL de la API
    url = "http://api.citybik.es/v2/networks/bikesantiago"

    # Hacer una petición GET a la API
    response = requests.get(url)

    # Si la petición es exitosa (código 200), obtener el campo "stations" del objeto JSON
    if response.status_code == 200:
        data = response.json()
        stations = data["network"]["stations"]

        # Crear objetos Estacion y guardarlos en la base de datos
        for station in stations:
            estacion = Estacion(name=station["name"], address=station["extra"]["address"], latitude=station["latitude"], longitude=station["longitude"], empty_slots=station["empty_slots"], free_bikes=station["free_bikes"])
            estacion.save()

        return render(request, "guardado_exitoso.html")
    else:
        return render(request, "error.html")
