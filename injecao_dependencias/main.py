from src.pessoa import Pessoa
from src.acoes.falar import IniciarFala
from src.acoes.correr import FazerCorrida
from src.acoes.jogar import IniciarFutebol
from src.acoes.comer import IniciarComer

pessoa1 = Pessoa(IniciarFala())
pessoa1.realizarAcao()

pessoa2 = Pessoa(FazerCorrida())
pessoa2.realizarAcao()