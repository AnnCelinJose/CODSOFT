movie_db = {
    "action": [
        "Avengers: Endgame",
        "John Wick",
        "Mad Max: Fury Road",
        "Mission Impossible",
        "The Dark Knight",
        "Gladiator"
    ],

    "comedy": [
        "Home Alone",
        "The Hangover",
        "Mr. Bean's Holiday",
        "Jumanji",
        "The Mask",
        "Free Guy"
    ],

    "horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle",
        "The Nun",
        "IT",
        "A Quiet Place"
    ],

    "science fiction": [
        "Interstellar",
        "Inception",
        "Avatar",
        "Dune",
        "The Matrix",
        "Blade Runner 2049"
    ],

    "romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Me Before You",
        "Pride and Prejudice",
        "A Walk to Remember"
    ],

    "animation": [
        "Toy Story",
        "Frozen",
        "Moana",
        "Kung Fu Panda",
        "Finding Nemo",
        "Coco"
    ],

    "thriller": [
        "Shutter Island",
        "Gone Girl",
        "Prisoners",
        "Se7en",
        "The Silence of the Lambs",
        "Zodiac"
    ],

    "fantasy": [
        "Harry Potter",
        "The Lord of the Rings",
        "The Hobbit",
        "Narnia",
        "Fantastic Beasts",
        "Percy Jackson"
    ]
}

print("=" * 45)
print("      SMARTFLIX RECOMMENDATION SYSTEM")
print("=" * 45)

while True:
    print("\nAvailable Genres:")
    for genre in movie_db:
        print("-", genre.title())

    choice = input("\nEnter a genre (or type 'exit'): ").lower()

    if choice == "exit":
        print("\nThank you for using SmartFlix!")
        break

    if choice in movie_db:
        print("\nRecommended Movies:\n")

        for i, movie in enumerate(movie_db[choice], start=1):
            print(f"{i}. {movie}")

    else:
        print("\nGenre not found. Please choose from the list.")