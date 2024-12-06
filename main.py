from readchar import readkey, key
from jogo import Jogo

from tela import Tela

# Iblock = [["*"],
#           ["*"],
#           ["*"],
#           ["*"],]


# jogo = Jogo()

# jogo.iniciar_game()


tela = Tela(8,4)

tela.mostrar_tela()

tela.adicionar_bloco()
tela.mostrar_tela()





# print("Pressione teclas!")
# while True:
#     tecla = readkey()
#     if "a" < tecla < "z" or "A" < tecla < "Z":
#         print("Pressionou letra:", tecla)
#     elif tecla == key.DOWN:
#         print("Pressionou seta para baixo")
#     elif tecla == key.ENTER:
#         print("Pressionou ENTER")
#         print("Tchau!")
#         break
