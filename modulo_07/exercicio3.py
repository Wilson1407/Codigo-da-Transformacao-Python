# jogo de advinhação com math e random.

import random
import math

def jogar():
    print("=== Jogo de Adivinhação ===")
    print("Tente adivinhar o número entre 1 e 100.")

    numero_secreto = random.randint(1, 100)
    tentativas_maximas = int(math.log2(100)) + 1
    tentativas = 0

    while True:
        try:
            entrada = input(f"\nSua tentativa ({tentativas + 1}/{tentativas_maximas}): ")
            palpite = int(entrada)
            tentativas += 1

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas!")
                break
            elif palpite < numero_secreto:
                print("Mais alto!")
            else:
                print("Mais baixo!")

        except ValueError:
            print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    jogar()