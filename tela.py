import os

from bloco import *


class Tela:
    def __init__(self,quantidadeL,quantidadeC):
        self.__quantidadeL = quantidadeL
        #aqui eu crio uma matrix quantidadeL x quantidadeC, com uma duas linhas e duas colunas a mais para servir de paredes 
        self.__quantidadeC = quantidadeC
        self.__matrixT = [[" " for c in range(quantidadeC+2) ] for l in range(quantidadeL+2)]
        
        self.bloco_atual = None #bloco que esta em execucao na tela


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
        
        self.bloco_atual = BlocoI(self.__matrixT) #crio o bloco de formato I
    
        self.__limparTela()

        self.bloco_atual.gerarBloco()


    def taganhadofilho(self):
        
        """checka se alguma linha da matrix esta completa se estiver removemos as pecas dela
            return : boolean(removeu a linha)
        """
        contador = 0 #ira contar quantas colunas em uma linha estao preenchidas
        linhaRemover = -1 #referencia a linha que ira ser removida

        for l in range(1,self.__quantidadeL+1):
            contador = 0
            
            for c in range(1,self.__quantidadeC+1):
                if self.__matrixT[l][c]!=" ":
                    contador+=1
            
            if(contador==self.__quantidadeC):
                linhaRemover = l
        
        if(linhaRemover!=-1):
            for c in range(1,self.__quantidadeC+1):
                self.__matrixT[linhaRemover][c] = " "
            return True
        return False





    def mover_esquerda(self):
        """move bloco atual para a esquerda da tela"""
        self.bloco_atual.ir_esquerda()

    def mover_direta(self):
        """move bloco atual para a direita da tela"""
        self.bloco_atual.ir_direita()
    
    def mover_baixo(self):
        """move bloco atual para baixo da tela"""
        self.bloco_atual.ir_baixo()    

    def rotacionar_esquerda(self):
        """rotaciona o bloco atual para a esquerda"""
        self.bloco_atual.rotacionar_esquerda()

    def rotacionar_direita(self):
        """rotaciona bloco para a direita"""
        self.bloco_atual.rotacionar_direita()    
    
    def mostrar_pontuacao(self,pontuacao):
        print("Pontuação:  "+ str(pontuacao))

    






