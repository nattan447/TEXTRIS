import os
from bloco import Bloco




class Tela:
    def __init__(self,quantidadeL,quantidadeC):
        self.__quantidadeL = quantidadeL
        #aqui eu crio uma matrix quantidadeL x quantidadeC, com uma linha e coluna a mais para servir de paredes 
        self.__quantidadeC = quantidadeC
        self.__matrixT = [[" " for c in range(quantidadeC+1) ] for l in range(quantidadeL+1)]

    @staticmethod
    def __limparTela():
        os.system('cls||clear')    
    
    def mostrar_tela(self):
        self.__limparTela()
        for i in range(1,self.__quantidadeC):
            #preencho a primeira linha e a ultima com paredes
            self.__matrixT[0][i]=self.__matrixT[self.__quantidadeL][i] ="_" 
            
        for i in range(1,self.__quantidadeL):
            #preencho a primeira coluna e a ultima com paredes
            self.__matrixT[i][0] = self.__matrixT[i][self.__quantidadeC] = "|"

        for l in self.__matrixT:
            print(" ")
            for c in l:
               print(c,end="")
        print("")


    def adicionar_bloco(self):
        #nosssas linha do jogo comeca no indice 1
        bloco = Bloco([1,2,3,4,5,6,7])
        self.__limparTela()
        bloco.gerarBloco(self.__matrixT)
        
            
    






