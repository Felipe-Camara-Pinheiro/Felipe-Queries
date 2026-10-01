import secrets
import string


def generate_password(length, use_symbols=True):
    characters = string.ascii_letters + string.digits

    if use_symbols:
        characters += "!@#$%&*?"

    return "".join(secrets.choice(characters) for _ in range(length))


def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%&*?" for char in password):
        score += 1

    if score <= 2:
        return "🔴 Fraca"
    if score <= 4:
        return "🟡 Média"
    return "🟢 Forte"


def main():
    print("╔══════════════════════════════╗")
    print("║      🔐 NEON PASSWORD       ║")
    print("╚══════════════════════════════╝")

    while True:
        try:
            length = int(input("\nTamanho da senha (8-64): "))
        except ValueError:
            print("Digite um número.")
            continue

        if not 8 <= length <= 64:
            print("Escolha um tamanho entre 8 e 64.")
            continue

        symbols = input("Usar símbolos? [S/n]: ").strip().lower()
        use_symbols = symbols != "n"

        password = generate_password(length, use_symbols)

        print("\nSua senha:")
        print(f"  {password}")
        print(f"\nForça: {password_strength(password)}")

        again = input("\nGerar outra? [S/n]: ").strip().lower()

        if again == "n":
            print("Até mais! 👋")
            break


if __name__ == "__main__":
    main()
