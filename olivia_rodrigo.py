import random

ARTIST = "Olivia Rodrigo"

SONGS = {
    "SOUR": [
        "brutal",
        "traitor",
        "drivers license",
        "deja vu",
        "good 4 u",
        "enough for you",
        "happier",
        "jealousy, jealousy",
        "favorite crime",
        "hope ur ok",
    ],
    "GUTS": [
        "all-american bitch",
        "bad idea right?",
        "vampire",
        "lacy",
        "ballad of a homeschooled girl",
        "making the bed",
        "logical",
        "get him back!",
        "love is embarrassing",
        "the grudge",
        "pretty isn't pretty",
        "teenage dream",
    ],
}


def show_albums():
    print("\nÁlbuns:")
    for album, songs in SONGS.items():
        print(f"\n{album} — {len(songs)} músicas")
        for number, song in enumerate(songs, 1):
            print(f"  {number:02d}. {song}")


def random_song():
    album = random.choice(list(SONGS))
    song = random.choice(SONGS[album])

    print("\n🎲 Sua música aleatória:")
    print(f"   {song}")
    print(f"   Álbum: {album}")


def create_setlist():
    amount = input("\nQuantas músicas no setlist? ")

    try:
        amount = int(amount)
    except ValueError:
        print("Digite um número válido.")
        return

    all_songs = [
        (album, song)
        for album, songs in SONGS.items()
        for song in songs
    ]

    amount = min(amount, len(all_songs))
    setlist = random.sample(all_songs, amount)

    print("\n🎤 SETLIST")
    print("-" * 35)

    for position, (album, song) in enumerate(setlist, 1):
        print(f"{position:02d}. {song} — {album}")


def search_song():
    query = input("\nDigite parte do nome da música: ").lower()

    results = []

    for album, songs in SONGS.items():
        for song in songs:
            if query in song.lower():
                results.append((song, album))

    if not results:
        print("Nenhuma música encontrada.")
        return

    print("\n🔎 Resultados:")
    for song, album in results:
        print(f"- {song} ({album})")


def main():
    print(f"🎵 Bem-vindo ao {ARTIST} Music Generator!")

    while True:
        print("\n" + "=" * 35)
        print("1. Ver músicas")
        print("2. Sortear uma música")
        print("3. Criar setlist")
        print("4. Procurar música")
        print("5. Sair")
        print("=" * 35)

        choice = input("Escolha: ").strip()

        if choice == "1":
            show_albums()
        elif choice == "2":
            random_song()
        elif choice == "3":
            create_setlist()
        elif choice == "4":
            search_song()
        elif choice == "5":
            print("Até a próxima 💜")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
