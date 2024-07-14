from abc import ABC, abstractmethod


class Gleb(ABC):

    @abstractmethod
    def hate(self): pass


class GlebWithCoffee(ABC):

    def hate(self):
        print('Глеб: У меня есть кофе и я всеx вас люблю! Го на улицу)')


class GlebWithoutCoffee(ABC):

    def hate(self):
        print('Глеб: Пффф, иди учи базу!')

