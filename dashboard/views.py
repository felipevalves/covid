from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Boletim
from dashboard.services.base_service import BaseService
from dashboard.bo import covid_bo, chart_bo


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'dashboard/index.html'


class BoletimListView(ListView):
    template_name = 'dashboard/lista.html'
    model = Boletim
    context_object_name = 'boletins'


def importar_dados_covid(request):
    if request.method == 'POST':
        print(covid_bo.consultar_covid_cidade('PR', 'CURITIBA'))

        service = BaseService()
        # service.importar_dados_covid('PR')
        print('chamar classe de importar dados covid')

    return render(request, 'dashboard/importar_dados.html')


def chart_column_2d(request):
    chart = chart_bo.chart_column_2d()
    return render(request, 'dashboard/chart.html', {'output': chart.render()})
