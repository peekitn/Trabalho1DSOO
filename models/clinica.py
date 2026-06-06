from typing import List

class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cidade(self) -> str:
        return self.__cidade
