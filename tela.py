import os
from bloco import Bloco


class Tela:
    def __init__(self,quantidadeL,quantidadeC):
        self.__quantidadeL = quantidadeL
        #aqui eu crio uma matrix quantidadeL x quantidadeC, com uma duas linhas e duas colunas a mais para servir de paredes 
        self.__quantidadeC = quantidadeC
        self.__matrixT = [[" " for c in range(quantidadeC+2) ] for l in range(quantidadeL+2)]
        
        for i in range(1,quantidadeC+1):
            #preencho a primeira linha e a ultima com paredes
            self.__matrixT[0][i]=self.__matrixT[self.__quantidadeL+1][i] ="_" 
            
        for i in range(1,quantidadeL+1):
            #preencho a primeira coluna e a ultima com paredes
            self.__matrixT[i][0] = self.__matrixT[i][self.__quantidadeC+1] = "|"

    
    @staticmethod
    def __limparTela():
        os.system('cls||clear')    
    
    def mostrar_tela(self):
        """ essa função mostra a matriz da tela"""

        self.__limparTela()


        for l in self.__matrixT:
            print(" ")
            for c in l:
               print(c,end="")
        print("")


    def adicionar_bloco(self):
        """essa função a adiciona uma bloco na matrix"""
        #nosssas linha do jogo comeca no indice 1
        bloco = Bloco([1,2,3,4,5,6,7])
        self.__limparTela()
        bloco.gerarBloco(self.__matrixT)


    def mover_esquerda(self):
        #move bloco para esquerda
        print("to mendove")
    def mostrar_pontuacao(self,pontuacao):
        print("Pontuação:  "+ str(pontuacao))

    






