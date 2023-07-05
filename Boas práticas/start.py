""" something """
from typing import Type, Union
from .atleta import Atleta

def agregation(element_1: Union[str, int], element_2: Union[str, int]):
    """ Create an agregation with two elements
    :param - element_1: string with first element
           - element_2: string with second element
    : return - string with elements agregated
    """

    return element_1 + element_2

string = agregation('ola','mundo')
print(string)

def receber_atleta(atleta: Type[Atleta]):
    print(atleta)

