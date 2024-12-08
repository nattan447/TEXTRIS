from datetime import datetime
import pickle
from readchar import readkey, key
from  tela import Tela
import  os

class Partida :
    def __init__(self,nome_jogador):
        self.nome_jogador = nome_jogador
        self.pontuacao = 0
    


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

            print(" ")

            tecla = readkey()
            if(tecla==key.LEFT):
                tela.mover_esquerda()
            elif (tecla==key.RIGHT):
                tela.mover_direta()
            elif (tecla==key.DOWN):
                tela.mover_baixo()
            elif(tecla=="s"):
                ##sai da partida
                return
            elif(tecla=="g"): 
                ##salva e sai da partida    
                self.__salvar_partida()
                return
            tela.mostrar_tela()

    def __salvar_partida(self):
              """
              salva o objeto da partida atual em um arquivo com nome sendo : nome_jogador+dataAtual
              """

              if not os.path.exists("partidas"):
                    #crio a pasta paridas se nao existir
                  os.makedirs("partidas")

              data = datetime.now()
              nomeArquivo = self.nome_jogador+str(data.strftime('%d-%m-%Y-%H-%M-%S'))
              caminhoArquivo = os.path.join("partidas",nomeArquivo) #caminho do arquivo na pasta partidas

              with open(caminhoArquivo, "wb") as arquivo:
                  #crio o arquivo
                    pickle.dump(self, arquivo) 



