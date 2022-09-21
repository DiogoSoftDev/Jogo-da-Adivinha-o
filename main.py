from random import randint
from time import sleep

computador = randint(0, 5)
print("\033[34m-=-\033[m" * 15)
print("Vou pensar num numero entre 0 e 5, tente")
print("\033[34m-=-\033[m" * 15)
jogador = int(input("Que numero pensei?"))
print("\033[35mProcessando...\033[m")
sleep (2)
if jogador == computador:
    print("\033[32mParabéns, consegiui ganhar\033[m")
else:
    print("\033[32mPerdeu\033[m, pensei no número {} e não no {}".format(computador, jogador))