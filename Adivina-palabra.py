import random

PALABRAS = ["python", "docker", "juego", "terminal", "codigo"]

def jugar():
    palabra = random.choice(PALABRAS)
    letras_acertadas = set()
    intentos = 6

    print("🎮 Bienvenido al juego Adivina la Palabra (CLI) 🎮")
    while intentos > 0:
        progreso = "".join(c if c in letras_acertadas else "_" for c in palabra)
        print("\nPalabra:", " ".join(progreso))
        print(f"Intentos restantes: {intentos}")

        letra = input("Ingresa una letra: ").lower()
        if letra in palabra:
            letras_acertadas.add(letra)
            if all(c in letras_acertadas for c in palabra):
                print(f"\n🎉 ¡Ganaste! La palabra era: {palabra}")
                return
        else:
            intentos -= 1
            print("❌ Letra incorrecta.")

    print(f"\nPerdiste 😢. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar()
