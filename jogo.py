import pickle
from partida import Partida
from tela import Tela
from readchar import readkey, key
import os
import shutil
        

class Jogo:
    
    def iniciar_game(self):
        self.partidas = []
        """
        essa função inicia o jogo
        """
        while True:
            print("*** Jogo Textris - um tetris em modo texto ***")
            print("Opções  do jogo jogo:")
            print("- <i> para iniciar uma nova partida")
            print("- <c> para carregar  uma nova partida gravada e continua-la")
            print("- <p> para ver as 10 melhores pontuações")
            print("- <s> para sair do jogo")
            print("Digite a opção desejada :")
            resposta = readkey()
            Tela.limparTela()

            if resposta=="i":
                self.__iniciarPartida()
            elif resposta =="c":
                self.__carregarPartida()
            elif resposta=="p":
                self.__showtop10players()
            elif resposta=="s":
                shutil.rmtree("partidas",ignore_errors=True) #remove a pasta partidas
                return
            else:
                print("operação invalida")
            Tela.limparTela()

    def __iniciarPartida(self):
        """
        essa função inicia uma partida
        """
        nome = input("Digite o nome do jogador : ")
        partida = Partida(nome,0)
        quantidadeL = input("digite o numero de linhas da tela do jogo : ")
        quantidadeC = input("digite o número de colunas da tela do jogo : ")
        partida.iniciar_partida(int(quantidadeL),int(quantidadeC))
        print("cabou a graça")
    
        self.partidas.append(partida) #dps que a partida acabar colocamos no array de partidas para uso futuro
        if len(self.partidas)>1:
            self.partidas.sort(key=lambda partida:partida.pontuacao,reverse=True) #ordeno as lista de partidas em ordem descrescente por pontuacao
    
    
    def  __carregarPartida(self):
        """
        essa funcao carrega uma partida salva previamente
        """
        Tela.limparTela()

        if not os.path.exists("partidas"):
            print("não existe nenhuma partida salva. Presione a tecla 's' para voltar ao menu principal")
            while True:
                tecla = readkey()
                if tecla == 's':
                    return
            
    
        #abre a pasta partidas
        pastaPartidas = os.listdir("partidas")

        for i  in  range(len(pastaPartidas)):
            print(str(i)+" - "+pastaPartidas[i])
        
        print("escolha o número da partida a ser carregada ou presione s para voltar :")

        while True:
            tecla = readkey()
            if tecla=="s":
                return
            try:
                #checka se o arquivo da partida escolhido realmente existe nas pastas
                if 0<=int(tecla)<len(pastaPartidas):
                    # abre o arquivo e carrega como objeto
                    caminho = os.path.join("partidas",pastaPartidas[int(tecla)])
                    
                    with open(caminho, "rb") as arquivo:
                        
                        partida_carregada = pickle.load(arquivo)
                        
                        partida_carregada.init_part_carregada()
                        #saiu da partida
                        #otimizar essa parte do codigo
                        for i in range(0,len(self.partidas)):
                            if self.partidas[i].nome_jogador==partida_carregada.nome_jogador:
                                self.partidas[i] = partida_carregada
                                break
                        if len(self.partidas)>1:
                            self.partidas.sort(key=lambda partida:partida.pontuacao,reverse=True) #ordeno as lista de partidas em ordem descrescente por pontuacao

                        return
                
                else :return
            except:
                pass #operacao invalida
               
    
    def __showtop10players(self):
        """
        mostra o top 10 players que obtiveram as maiores pontuacoes
        """
        Tela.limparTela()
        for i in range(len(self.partidas)):
            print(str(i+1)+" - " + self.partidas[i].nome_jogador + " - " + str(self.partidas[i].pontuacao)+"pts")        
            if i==9: break
        
        print("aperte s para sair")
        while True:
            tecla = readkey()
            if tecla == "s":return
                    
                
    
    
