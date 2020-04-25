from collections import OrderedDict
from .covid_bo import consultar_covid_cidade
from ..fusioncharts import FusionCharts

data_source = OrderedDict()


def chart_column_2d():
    consultar_covid_fusion_chart('PR', 'CURITIBA')
    chart_config()
    return FusionCharts("line", "myFirstChart", "600", "400", "myFirstchart-container", "json", data_source)


def consultar_covid_fusion_chart(uf, cidade):
    data_source['data'] = []
    boletins = consultar_covid_cidade(uf, cidade)
    for b in boletins:
        data_source['data'].append({'label': b.data_boletim.strftime("%d/%m/%Y"), 'value': b.confirmados})


def chart_config():
    chart_config = OrderedDict()
    chart_config["caption"] = "CASOS CONFIRMADOS DE CODIV-19"
    chart_config["subCaption"] = "Curitiba"
    chart_config["xAxisName"] = "Data"
    chart_config["yAxisName"] = "Quantidade"
    # chart_config["numberSuffix"] = "K"
    chart_config["theme"] = "fusion"

    data_source['chart'] = chart_config
