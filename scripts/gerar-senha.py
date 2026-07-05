import random
import sys

letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*+-_=?"

def gerar_senha(tamanho=16, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    pool = letras_minusculas
    obrigatorios = []

    if usar_maiusculas:
        pool += letras_maiusculas
        obrigatorios.append(random.choice(letras_maiusculas))
    if usar_numeros:
        pool += numeros
        obrigatorios.append(random.choice(numeros))
    if usar_simbolos:
        pool += simbolos
        obrigatorios.append(random.choice(simbolos))

    if tamanho < len(obrigatorios):
        tamanho = len(obrigatorios)

    restantes = tamanho - len(obrigatorios)
    senha = [random.choice(pool) for _ in range(restantes)]
    senha.extend(obrigatorios)
    random.shuffle(senha)
    return "".join(senha)

def verificar_forca(senha):
    score = 0

    if len(senha) >= 12:
        score += 1
    if len(senha) >= 16:
        score += 1
    if any(c in simbolos for c in senha):
        score += 1
    if any(c in numeros for c in senha):
        score += 1
    if any(c in letras_maiusculas for c in senha):
        score += 1

    if score <= 2:
        return "Fraca"
    elif score <= 3:
        return "Média"
    elif score <= 4:
        return "Forte"
    else:
        return "Muito Forte"

if __name__ == "__main__":
    try:
        if len(sys.argv) >= 2:
            tamanho = int(sys.argv[1])
        else:
            tamanho = 16

        senha = gerar_senha(tamanho)
        forca = verificar_forca(senha)

        print(f"Senha: {senha}")
        print(f"Tamanho: {len(senha)} caracteres")
        print(f"Força: {forca}")

        if forca in ("Fraca", "Média"):
            print("Dica: aumenta o tamanho ou usa símbolos e números.")

    except ValueError:
        print("Uso: python gerar-senha.py [tamanho]")
        print("Ex:  python gerar-senha.py 20")
        sys.exit(1)
