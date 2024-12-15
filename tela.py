import os
from blocos.blocoi import BlocoI
from blocos.blocoj import BlocoJ
from blocos.blocoo import BlocoO
from blocos.blocos import BlocoS
from blocos.blocoz import BlocoZ
from blocos.blocot import BlocoT
from blocos.blocol import BlocoL
import random


##
# \brief Esta classe implementa a tela da nossa partida
class Tela:
    ##
    # \brief contrutor
    # \param qualidadeL : quantidade de linhas da tela
    # \param quantidadeC : quantidade colunas da tela
    def __init__(self,quantidadeL,quantidadeC):
        self.__quantidadeL = quantidadeL
        #aqui eu crio uma matrix quantidadeL x quantidadeC, com uma duas linhas e duas colunas a mais para servir de paredes 
        self.__quantidadeC = quantidadeC
        self.__matrixT = [[" " for c in range(quantidadeC+2) ] for l in range(quantidadeL+2)]
        
        self.bloco_atual = None #bloco que esta em execucao na tela

        for i in range(1,quantidadeC+1):
            #preencho a primeira linha e a ultima com paredes
            self.__matrixT[0][i]=self.__matrixT[self.__quantidadeL+1][i] ="—" 
            
        for i in range(1,quantidadeL+1):
            #preencho a primeira coluna e a ultima com paredes
            self.__matrixT[i][0] = self.__matrixT[i][self.__quantidadeC+1] = "|"

    ##
    # \brief limpa a tela 
    @staticmethod
    def limparTela():
        os.system('cls||clear')    
    

    ##
    # \brief mostra a tela da paritda 
    def mostrar_tela(self):
        """ essa função mostra atela da partida"""
        self.limparTela()
        for l in self.__matrixT:
            print(" ")
            for c in l:
               print(c,end="")
        print("")

    ##
    # \brief adiciona o bloco na tela
    # \return :  false se o bloco nao foi adicionado, true se foi
    def adicionar_bloco(self):
        #nosssas linha do jogo comeca no indice 1
        chance = random.uniform(0.01,1.0)
        #bloco aleatorio
        if chance<=0.14:
            self.bloco_atual = BlocoI(self.__matrixT) #crio o bloco de formato I
        elif 0.14<chance<=0.28:
            self.bloco_atual = BlocoJ(self.__matrixT) #crio o bloco de formato J
        elif 0.28<chance<=0.42:
            self.bloco_atual = BlocoL(self.__matrixT) #crio o bloco de formato L
        elif 0.42<chance<=0.56:
            self.bloco_atual = BlocoO(self.__matrixT) #crio o bloco de formato L
        elif 0.56<chance<=0.70:
            self.bloco_atual = BlocoS(self.__matrixT)
        elif 0.70<chance<=0.84:
            self.bloco_atual = BlocoT(self.__matrixT)
        else :
            self.bloco_atual = BlocoZ(self.__matrixT)
        # self.bloco_atual = BlocoI(self.__matrixT)
    
        self.limparTela()
            #se nao gerou o bloco quer dizer que nao foi adicionado
        if  not self.bloco_atual.gerarBloco(): 
            return False
        return True
        
    def remover_linhas(self):
        """
        remove todas linhas que estao completas e retorna a quantidade de linhas removidas
        return : int
        """
        quantd = 0
        for i in range(0,len(self.__matrixT)-2):
              if self.__removerLinha() :
                  quantd+=1
        return quantd

    def __removerLinha(self):
        
        """checa se alguma linha da matrix esta completa se estiver removemos as pecas dela
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
                    
                for l in range(1,linhaRemover+1): #desco todos elementos da coluna 'c' que estao acima de linha que esta completo, para baixo
                    bau = self.__matrixT[l][c]
                    self.__matrixT[l][c] = j
                    j = bau

                until = linhaRemover+1
                
                #verifico se existe espaco para o pedaco do bloco 'cair', se existir, ele cai
                while until<=self.__quantidadeL and self.__matrixT[until][c]==" ":
                    until+=1
                while until is not linhaRemover+1:
                    for l in range(until-1,1,-1):
                        sobe = self.__matrixT[l][c]
                        if self.__matrixT[l-1][c] !=" ":
                            self.__matrixT[l][c] = self.__matrixT[l-1][c]
                            self.__matrixT[l-1][c] = sobe
                    until+= -1 
            return True
        return False

    def mover_esquerda(self):
        """move bloco atual para a esquerda da tela"""
        self.bloco_atual.ir_esquerda()

    def mover_direta(self):
        """move bloco atual para a direita da tela"""
        self.bloco_atual.ir_direita()
    

    def mover_baixo(self):
        """move bloco atual para baixo da tela retorna true se consguiu mover para baixo , senao retorna false
        
            return : boolean
        """
        moveu = self.bloco_atual.ir_baixo()
        if not moveu:                    
            return False
        return True
                    
            

    def rotacionar_esquerda(self):
        """rotaciona o bloco atual da tela para a esquerda"""
        self.bloco_atual.rotacionar_esquerda()

    def rotacionar_direita(self):
        """rotaciona bloco autal da tela para a direita"""
        self.bloco_atual.rotacionar_direita()    
    
    def mostrar_pontuacao(self,pontuacao):
        print("Pontuação:  "+ str(pontuacao))

    






