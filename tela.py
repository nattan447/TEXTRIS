import os
from blocoi import BlocoI
from blocoj import BlocoJ
from blocol import BlocoL
from blocoo import BlocoO
import random
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
    def limparTela():
        os.system('cls||clear')    
    
    def mostrar_tela(self):
        """ essa função mostra a matriz da tela"""

        self.limparTela()


        for l in self.__matrixT:
            print(" ")
            for c in l:
               print(c,end="")
        print("")


    def adicionar_bloco(self):
        """essa função a adiciona uma bloco na matrix"""
        
        #nosssas linha do jogo comeca no indice 1
        chance = random.uniform(0.01,1.0)
        #bloco aleatorio
        if chance<=0.25:
            self.bloco_atual = BlocoI(self.__matrixT) #crio o bloco de formato I
        elif 0.25<chance<=0.5:
            self.bloco_atual = BlocoJ(self.__matrixT) #crio o bloco de formato J
        elif 0.5<chance<=0.75:
            self.bloco_atual = BlocoL(self.__matrixT) #crio o bloco de formato L
        elif 0.75<chance:
            self.bloco_atual = BlocoO(self.__matrixT) #crio o bloco de formato L

    
        self.limparTela()

        self.bloco_atual.gerarBloco()


    def __taganhanDoFilho(self):
        
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
                break

            #primeira linha completa -> apenas esvazie ela
        if(linhaRemover==1):
            for c in range(1,self.__quantidadeC+1):
                self.__matrixT[linhaRemover][c] = " "            
            return True
        elif(linhaRemover>1):
            #linha maior q 1 preenchida - > coloque o que esta em cima para baixo
            linhadesce = linhaRemover -1

            for c in range(1,self.__quantidadeC+1):
                j = " "
                for l in range(1,linhaRemover+1):
                    bau = self.__matrixT[l][c]
                    self.__matrixT[l][c] = j
                    j = bau

    
            return True
        return False

    def mover_esquerda(self):
        """move bloco atual para a esquerda da tela"""
        self.bloco_atual.ir_esquerda()

    def mover_direta(self):
        """move bloco atual para a direita da tela"""
        self.bloco_atual.ir_direita()
    
    def mover_baixo(self):
        """move bloco atual para baixo da tela retorna verdadeiro se consguiu mover para baixo
        
            return : -2 se o jogador perdeu , >=1 se o jogador apagou linhas , -1 se nao tem como ir para baixo
        """
        moveu = self.bloco_atual.ir_baixo()
        if moveu==False:
            midLinha = int ((len(self.__matrixT[0])-1)/2)
            if self.__matrixT[1][midLinha]!=" ":
                return -2#verifica se o user perdeu a partida
            quntLinhas = 0
            for i in range(0,len(self.__matrixT)-2):
                w = self.__taganhanDoFilho()
                if w ==True:
                    quntLinhas+=1
            self.adicionar_bloco()
            if quntLinhas>0:
                return quntLinhas
        return -1
            

    def rotacionar_esquerda(self):
        """rotaciona o bloco atual para a esquerda"""
        self.bloco_atual.rotacionar_esquerda()

    def rotacionar_direita(self):
        """rotaciona bloco para a direita"""
        self.bloco_atual.rotacionar_direita()    
    
    def mostrar_pontuacao(self,pontuacao):
        print("Pontuação:  "+ str(pontuacao))

    






