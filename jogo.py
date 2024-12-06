from partida import Partida

class Jogo:
    def iniciar_game(self):
        
        self.partidas = []
        
        """
        essa função inicia o jogo
        
        """
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

    
    
    def __iniciarPartida(self):
        """
        essa função inicia uma partida
        """
        nome = input("Digite o nome do jogador : ")
        partida = Partida(nome)
        quantidadeL = input("digite o numero de linhas da tela do jogo : ")
        quantidadeC = input("digite o número de colunas da tela do jogo : ")
        partida.iniciar_partida(int(quantidadeL),int(quantidadeC))

        self.partidas.append(partida) #dps que a partida acabar colocamos no array de partidas para uso futuro
        
        # if len(self.partidas)>0:
        #     self.partidas.sort(key=partida.pontuacao,reverse=True) #ordeno as lista de partidas em ordem descrescente por pontuacao
    
    
    def  __caregarPartida(self):
        print("carrehar partida")
    
    def __showtop10players(self):
        """
        mostra o top 10 players que obtiveram maiores pontuaçaõ
        """
        for i in range(10):
            print(self.partidas[i].nome)
        
    
    
