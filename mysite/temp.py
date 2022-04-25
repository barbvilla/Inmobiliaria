import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from m7_python.models import Inmuebles, Region

def get_list_inmuebles(name, descripcion):
    lista_inmuebles = Inmuebles.objects.filter(nombre_inmueble__contains=name).filter(descripcion__contains=descripcion)

    archi1=open("datos.txt", "w")
    for l in lista_inmuebles.values():
        archi1.write(str(l))
        archi1.write("\n")
    archi1.close()

    return lista_inmuebles

#resultado = get_list_inmuebles("Providencia", "Cocina")

def get_list_inmuebles_por_comuna(comuna):
    select = f"""
    SELECT A.id, A.nombre_inmueble, A.descripcion
    FROM public.m7_python_inmuebles as A
    INNER JOIN public.m7_python_comuna as B
    ON A.id_region_id = B.id
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE C.comuna LIKE '%%{str(comuna)}%%'
    """
    results = Inmuebles.objects.raw(select)

    archi1=open("datos.txt", "w")
    for p in results:
        archi1.write(p.nombre_inmueble+','+p.descripcion)
        archi1.write("\n")
    archi1.close()

get_list_inmuebles_por_comuna("Bernardo")


def get_list_inmuebles_region(id):
    region = str(Region.objects.filter(id=id).value()[0]["region"])

    lista_inmuebles = Inmuebles.objects.filters(id_region_id=id)

    archi1=open("datos.txt", "w")
    for l in lista_inmuebles.values():
        archi1.write(str(1,["nombre_inmueble"]))
        archi1.write(',')
        archi1.write(region)
        archi1.write("\n")
    archi1.close()

#get_list_inmuebles_region(16)

def get_list_inmueble_por_region(region):
    select = f"""
    SELECT A.id,
    A.nombre_inmueble,
    A.descripcion
    FROM public.m7_python_inmuebles as A 
    INNER JOIN public.m7_python_region as B
    ON A.id_region_id = B.id
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE B.Region like '%%{str(region)}%%'
    """
    results = Inmuebles.objects.raw(select)

    archi1=open("datos.txt","w")
    for p in results:
        archi1.write(p.nombre_inmueble+','+p.descripcion)
        archi1.write("\n")
    archi1.close()

get_list_inmueble_por_region("Metrop")
