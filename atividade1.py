import random

def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def guessing_game():
    words = ["casa", "facil", "caju", "jaca", "laranja"]
    secret_word = random.choice(words)
    shuffled_word = shuffle_word(secret_word)
    
    print("Bem-vindo ao jogo de adivinhar palavras!")
    print(f"A palavra embaralhada é: {shuffled_word}")
    
    remaining_attempts = 5
    guessed_correctly = False
    
    while remaining_attempts > 0 and not guessed_correctly:
        answer = input(f"Você tem {remaining_attempts} tentativa(s). Qual é a palavra? ")
        
        if answer.lower() == secret_word:
            print(f"Parabéns! Você acertou a palavra '{secret_word}'!")
            guessed_correctly = True
        else:
            remaining_attempts -= 1
            encouraging_words = [
                "Tente de novo!", 
            ]
            print(random.choice(encouraging_words))
    
    if not guessed_correctly:
        print(f"Poxa, suas tentativas acabaram. A palavra correta era '{secret_word}'.")
    print(f"Fim de jogo. Você usou {5 - remaining_attempts} tentativa(s).")


guessing_game()
