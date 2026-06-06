from typing import List

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional = profissional

    @property
    def custo(self) -> float:
        return self.__custo
        
    @property
    def descricao(self) -> str:
        return self.__descricao

