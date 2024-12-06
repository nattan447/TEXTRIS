
from readchar import readkey, key
from  tela import Tela

class Partida :
    def __init__(self,nome_jogador):
        self.nome_jogador = nome_jogador
        self.pontuacao = 0
        self.bloco_atual = None #bloco que esta em execucao na partida
    


    def __mostrar_infos(self):
        """mostra as keys disponiveis para o jogador e seua pontuacao"""
        
        print("Pontuação : " + str(self.pontuacao))
        print("Teclas do jogo: ")
        print("← move esquerda | → move direira | ↓")
        print("<Page Down> rotaciona esquerda | <Page Up> rotaciona direita")
        print("<s> sai da partida, <g> grava e sai da partida")


    def iniciar_partida(self,quantidadeL,quantidadeC):
        """ essa função inicia a  partida criando uma tela
            quantidadeL : quantidade de linhas da tela
            quantidadeC : quantidade colunas da tela
        """

        tela = Tela(quantidadeL,quantidadeC)
        
        tela.adicionar_bloco()
        
        tela.mostrar_tela()


        while True:

            self.__mostrar_infos()  
            tecla = readkey()
            if(tecla=="a"):
                print("apertou a ")
      




