
from  tela import Tela
class Partida :
    def __init__(self,nome_jogador):
        self.nome_jogador = nome_jogador
        self.pontuacao = 0
    
    def iniciar_partida(self,quantidadeL,quantidadeC):
        """ essa função inicia a  partida criando uma tela
            quantidadeL : quantidade de linhas da tela
            quantidadeC : quantidade colunas da tela
        """

        
        tela = Tela(quantidadeL,quantidadeC)
        tela.adicionar_bloco()
        tela.mostrar_tela()
