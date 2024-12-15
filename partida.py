from datetime import datetime
import pickle
from readchar import readkey, key
from  tela import Tela
import  os


##
# \brief Esta classe implementa a Paritda do nosso jogo
class Partida :
    ##
    # \brief Construtor. inicia o nome do jogador , pontuação e a tela da partida como vazio
    def __init__(self,nome_jogador,pontuacao):
        self.nome_jogador = nome_jogador
        self.pontuacao = pontuacao
        self.__telaPartida = None


    ##
    # \brief inicia uma Partida que foi salva antes
    def init_part_carregada(self):
         """
            carrega uma partida salva anteriormente
         """
         self.__controlar_partida()
    ##
    # \brief Inicia a iterface quando o usuario perde a partida        
    def __perdeu_partida(self):
         """
         interface de quando o usuario perde parida
         """
         print("você perdeu o jogo :(")
         print("pontuação : " + str(self.pontuacao))
         print("pressione 's' para voltar ao menu principal")
         while True:
              tecla = readkey()
              if tecla=='s':
                   return    

    ##
    # \brief Mostra as informacoes da partida atual
    def __mostrar_infos(self):
        """mostra as keys disponiveis para o jogador e seua pontuacao"""
        
        print("Pontuação : " + str(self.pontuacao))
        print("Teclas do jogo: ")
        print("← move esquerda | → move direira | ↓")
        print("<Page Down> rotaciona esquerda | <Page Up> rotaciona direita")
        print("<s> sai da partida, <g> grava e sai da partida")

    ##
    # \brief Permite ao jogador controlar o estado da parida
    def __controlar_partida(self):
        '''essa funcao disponibiliza o usuario a controlar como sua partida ira prosseguir'''
        self.__telaPartida.mostrar_tela()
        while True:
            self.__mostrar_infos()

            print(" ")
            tecla = readkey()
            if tecla==key.LEFT:
                self.__telaPartida.mover_esquerda()
            elif tecla==key.RIGHT:
                self.__telaPartida.mover_direta()
            elif tecla==key.DOWN:
                moveu = self.__telaPartida.mover_baixo() 
                
                if moveu == False :
                     linhasremovidas = self.__telaPartida.remover_linhas()
                     if linhasremovidas>0:
                          self.pontuacao += 100*linhasremovidas
                     adicionou = self.__telaPartida.adicionar_bloco()
                     if adicionou== False:
                          self.__perdeu_partida() 
                          return #nao adicionou o bloco => jogador perdeu                
                else:
                     self.pontuacao+=2

                     
            elif tecla==key.PAGE_UP:
                 self.__telaPartida.rotacionar_direita()
            elif tecla==key.PAGE_DOWN:
            
                 self.__telaPartida.rotacionar_esquerda()
            
            elif(tecla=="s"):
                ##sai da partida
                return
            elif(tecla=="g"): 
                ##salva e sai da partida    
                self.__salvar_partida()
                return
            self.__telaPartida.mostrar_tela()
         
    ##
    # \brief Inicia a partida
    # \param  inteiros com quantidade de linhas da tela e quantidade colunas da tela,respectivamente
    def iniciar_partida(self,quantidadeL,quantidadeC):
        """ essa função inicia a  partida criando uma tela
            quantidadeL : quantidade de linhas da tela
            quantidadeC : quantidade colunas da tela
        """
        if quantidadeC<=2 and quantidadeL<=2:
             self.__perdeu_partida()
             return
            
        self.__telaPartida = Tela(quantidadeL,quantidadeC)
        
        self.__telaPartida.adicionar_bloco()
    
        self.__controlar_partida()

    ##
    # \brief Salva a partida atual em um arquivo
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



