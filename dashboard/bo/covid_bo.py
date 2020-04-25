from dashboard.models import Boletim

def consultar_covid_cidade(uf, cidade):
    return Boletim.objetos.filter(estado=uf).filter(municipio=cidade).order_by('data_boletim')

