from partida import Partida
from tela import Tela
from readchar import readkey, key
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
            
            resposta = input("Digite a opção desejada :")
            
            if resposta=="i":
                self.__iniciarPartida()
            elif resposta =="c":
                self.__caregarPartida()
            elif resposta=="p":
                self.__showtop10players()
            elif resposta=="s":
                return
            else:
                print("operação invalida")
            Tela.limparTela()


    
    
    def __iniciarPartida(self):
        """
        essa função inicia uma partida
        """
        nome = input("Digite o nome do jogador : ")
        partida = Partida(nome)
        quantidadeL = input("digite o numero de linhas da tela do jogo : ")
        quantidadeC = input("digite o número de colunas da tela do jogo : ")
        partida.iniciar_partida(int(quantidadeL),int(quantidadeC))
        print("cabou a graça")
        self.partidas.append(partida) #dps que a partida acabar colocamos no array de partidas para uso futuro
        
        # if len(self.partidas)>0:
        #     self.partidas.sort(key=partida.pontuacao,reverse=True) #ordeno as lista de partidas em ordem descrescente por pontuacao
    
    
    def  __caregarPartida(self):
        print("carrehar partida")
    
    def __showtop10players(self):
        """
        mostra o top 10 players que obtiveram maiores pontuaçaõ
        """
        Tela.limparTela()
        for i in range(len(self.partidas)):
            print("jogadaor : " + self.partidas[i].nome_jogador)
            
            if(i==9): break

        while True:
            print("aperte s para sair")
            tecla = readkey()
            if(tecla == "s"):return
                    
                
    
    
