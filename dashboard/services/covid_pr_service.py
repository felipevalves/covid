import math
from tabula import read_pdf
from dashboard.models import Boletim

# ver como implementar classe abstrata
class CovidPrService:
    __CONST_MUNICIPIO = 'MUNICÍPIO'
    __CONST_CONFIRMADOS = 'CONFIRMADOS'
    __CONST_OBITOS = 'ÓBITOS'
    __CONST_DESCARTADOS = 'DESCARTADOS'
    __CONST_INVESTIGACAO = 'EM INVESTIGAÇÃO'

    __URL = 'http://www.saude.pr.gov.br/arquivos/File/CORONA_{}.pdf'

    def executar(self, data):
        my_url = self.__formatar_url(data)
        return self.__tratar_retorno(read_pdf(my_url, pages=1), data)

    def __formatar_url(self, data):
        return self.__URL.format(data.strftime('%d%m%Y'))

    def __tratar_retorno(self, df, data):
        boletins = []

        for tabela in df:
            for index, row in tabela.iterrows():
                print(row)
                if self.get_value_string(row, self.__CONST_MUNICIPIO) is None:
                    continue

                boletins.append(Boletim(estado='PR',
                                        municipio=self.get_value_string(row, self.__CONST_MUNICIPIO),
                                        confirmados=self.get_value_number(row, self.__CONST_CONFIRMADOS),
                                        obitos=self.get_value_number(row, self.__CONST_OBITOS),
                                        descartados=self.get_value_number(row, self.__CONST_DESCARTADOS),
                                        investigacao=self.get_value_number(row, self.__CONST_INVESTIGACAO),
                                        data_boletim=data))
        return boletins

    def get_value_string(self, row, campo):
        if campo not in row:
            return None

        if row[campo] == 'nan':
            return None
        return row[campo]

    def get_value_number(self, row, campo):
        if campo not in row:
            return None

        if math.isnan(row[campo]):
            return 0
        return row[campo]
