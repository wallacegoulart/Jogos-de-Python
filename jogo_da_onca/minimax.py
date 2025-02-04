from typing import Callable
from math import inf


def teste_termino(estado: list) -> bool:
    """
    Determina se um estado de jogo não possui filhos.
    """
    pass


def estados_sucessores(estado: list, turno_onca: bool) -> list:
    """
    Expande o estado atual, retornando uma lista de tuplas com 3 elementos,
    sendo o primeiro a casa de origem do movimento, o segundo a casa destino,
    e o terceiro, o estado sucessor resultante.
    """
    pass


def decisao_minimax(estado: list, funcao_utilidade: Callable,
                    limite=-1) -> tuple:
    """
    Retorna uma tupla contendo o par `(origem, destino)` que leva ao primeiro
    estado sucessor encontrado tido como mais promissor.
    """
    valor = valor_max(estado, funcao_utilidade, limite -1)
    for origem, destino, sucessor in estados_sucessores(estado):
        if funcao_utilidade(sucessor) == valor:
            return (origem, destino)


def valor_max(estado: list, funcao_utilidade: Callable, limite: int) -> int:
    """
    Retorna o valor máximo de utilidade que um estado de jogo pode
    encaminhar. O argumento `limite` determina a maior profundidade de busca
    permitida.
    """
    if teste_termino(estado) or not limite:
        return funcao_utilidade(estado)
    
    valor = - inf
    for sucessor in estados_sucessores(estado):
        valor = max(valor, valor_min(sucessor, funcao_utilidade, limite - 1))
    
    return valor


def valor_min(estado: list, funcao_utilidade: Callable, limite: int) -> int:
    """
    Retorna o valor mínimo de utilidade que um estado de jogo pode
    encaminhar. O argumento `limite` determina a maior profundidade de busca
    permitida.
    """
    if teste_termino(estado) or not limite:
        return funcao_utilidade(estado)
        
    valor = inf
    for sucessor in estados_sucessores(estado):
        valor = min(valor, valor_max(sucessor, funcao_utilidade, limite - 1))
    
    return valor