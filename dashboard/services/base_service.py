from dashboard.services.covid_pr_service import CovidPrService
from dashboard.models import Boletim

from datetime import date, datetime, timedelta

from dashboard.services.covid_sp_service import CovidSpService
from dashboard.services.webservice import Webservice


class BaseService:
    __covid_pr = CovidPrService()

    def __init__(self) -> None:
        super().__init__()
        Webservice.register(CovidPrService)
        Webservice.register(CovidSpService)

    def importar_dados_covid(self, uf):
        #
        start = date(2020, 3, 28)
        end = date(2020, 4, 16)
        day = timedelta(days=1)

        data = start
        while data < end:
            print(data)
            boletins = self.__covid_pr.executar(data)
            # criar um factory para instanciar o ws conforme uf
            Boletim.objetos.filter(data_boletim=data).filter(estado=uf).delete()

            for b in boletins:
                b.save()

            data += day

        # data = datetime(2020, 3, 29)
        # boletins = self.__covid_pr.executar(data)
        #     # criar um factory para instanciar o ws conforme uf
        # Boletim.objetos.filter(data_boletim=data).filter(estado=uf).delete()
        #
        # for b in boletins:
        #     b.save()




# s = BaseService()
# s.importar_dados_covid()