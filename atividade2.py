import random

def shuffle_word(word):
    return ''.join(random.sample(word, len(word)))

def get_theme_words(theme_choice):
    themes = {
        1: ["londres", "paris", "berlim", "curitiba", "tokyo"],
        2: ["vermelho", "azul", "amarelo", "verde", "preto"],
        3: ["barcelona", "real", "chelsea", "palmeiras", "gremio"],
        4: ["brasil", "alemanha", "franca", "argentina", "mexico"],
        5: ["cadeira", "mesa", "laptop", "telefone", "caneca"]
    }
    return themes.get(theme_choice, themes[5])  # Tema padrão: Objetos

def choose_difficulty():
    difficulties = {1: 10, 2: 7, 3: 5}
    while True:
        try:
            level = int(input("\nEscolha o nível de dificuldade (1: Iniciante, 2: Intermediário, 3: Avançado): "))
            return difficulties.get(level, 5)
        except ValueError:
            print("Entrada inválida! Tente novamente.")

def get_theme_choice():
    while True:
        try:
            print("Escolha um tema:\n1: Cidades\n2: Cores\n3: Times\n4: Países\n5: Objetos")
            choice = int(input("Digite o número correspondente ao tema: "))
            if choice in range(1, 6):
                return choice
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 5.")

def game_loop(secret_word, shuffled_word, attempts):
    encouragement_phrases = [
        "Não desista!", "Você está quase lá!", 
        "Vai dar certo, continue tentando!", "Mantenha a calma e tente de novo!", 
        "Boa tentativa, mas ainda não foi dessa vez!"
    ]

    while attempts > 0:
        print(f"\nA palavra embaralhada é: {shuffled_word}")
        guess = input(f"Você tem {attempts} tentativa(s). Qual é a palavra? ").lower()

        if guess == secret_word:
            print(f"Parabéns! Você acertou a palavra '{secret_word}'!")
            return True
        else:
            print(random.choice(encouragement_phrases))
            attempts -= 1
    
    print(f"Poxa, suas tentativas acabaram. A palavra correta era '{secret_word}'.")
    return False

def main():
    print("Bem-vindo ao jogo de adivinhar palavras!")
    
    theme_choice = get_theme_choice()  # Escolher tema
    words = get_theme_words(theme_choice)  # Obter palavras com base no tema escolhido
    secret_word = random.choice(words)  # Palavra secreta
    shuffled_word = shuffle_word(secret_word)  # Embaralhar palavra secreta

    attempts = choose_difficulty()  # Definir nível de dificuldade
    game_loop(secret_word, shuffled_word, attempts)  # Rodar o jogo

    print("\nFim de jogo. Obrigado por jogar!")

# Iniciar o jogo
main()
