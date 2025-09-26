import random  # Módulo para geração de números e escolhas aleatórias
import string  # Módulo para acessar coleções de caracteres úteis (como letras)

def gerar_senha_minusculas():
    """
    Gera uma senha aleatória de letras minúsculas com o comprimento especificado pelo usuário.
    """
    # 1. Perguntar ao usuário o comprimento desejado
    while True:
        try:
            comprimento = int(input("Digite o comprimento desejado para a senha (ex: 8, 10, 12): "))
            if comprimento <= 0:
                print("O comprimento deve ser um número positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # A variável 'letras_minusculas' armazena a string 'abcdefghijklmnopqrstuvwxyz'
    letras_minusculas = string.ascii_lowercase

    # Inicializa a senha como uma string vazia
    senha_gerada = ""

    # 2. Usar um laço de repetição para selecionar e juntar caracteres
    # O laço irá rodar 'comprimento' vezes
    for _ in range(comprimento):
        # random.choice() seleciona um elemento aleatório de uma sequência (como nossa string de letras)
        caractere_aleatorio = random.choice(letras_minusculas)

        # Adiciona o caractere escolhido à senha
        senha_gerada += caractere_aleatorio

    # 3. Imprimir a senha gerada na tela
    print("\n--- Senha Gerada ---")
    print(f"Comprimento: {comprimento}")
    print(f"Senha: **{senha_gerada}**")
    print("--------------------")

# Chama a função para executar o programa
if __name__ == "__main__":
    gerar_senha_minusculas()