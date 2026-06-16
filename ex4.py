import random

number = random.randint(1, 100)
counter = 0

while True:
    guess = int(input("Digite um numero: "))
    counter += 1

    if guess == number:
        print(f"Parabéns! Você acertou em {counter} tentativas.")
        break

    if guess < number:
        print("Muito baixo")

    if guess > number:
        print("Muito alto")
