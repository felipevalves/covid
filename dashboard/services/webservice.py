from abc import ABC
from abc import abstractmethod

class Webservice(ABC):

    @abstractmethod
    def executar(self, data):
        print('executar')