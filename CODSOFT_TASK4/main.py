# Task 4 - Movie Recommendation System

movies = {
    "Horror": [
        "The Conjuring", "Annabelle", "Insidious", "The Nun",
        "It", "The Exorcist", "Hereditary", "Sinister",
        "A Quiet Place", "Scream"
    ],

    "Romance": [
        "Titanic", "The Notebook", "La La Land", "Me Before You",
        "The Fault in Our Stars", "Pride and Prejudice", "Before Sunrise",
        "Dear John", "Five Feet Apart", "10 Things I Hate About You"
    ],

    "Comedy": [
        "The Hangover", "Home Alone", "3 Idiots", "Rush Hour",
        "Dumb and Dumber", "Superbad", "Mean Girls", "The Mask",
        "Central Intelligence", "Game Night"
    ],

    "Action": [
        "Avengers", "John Wick", "Mission Impossible", "Fast and Furious",
        "Mad Max: Fury Road", "Die Hard", "Gladiator", "Top Gun: Maverick",
        "The Equalizer", "Extraction"
    ],

    "Thriller": [
        "A Quiet Place", "Gone Girl", "The Invisible Man", "Prisoners",
        "Se7en", "The Silence of the Lambs", "Split", "Get Out",
        "The Girl on the Train", "Nocturnal Animals"
    ],

    "Sci-Fi": [
        "Inception", "Interstellar", "The Matrix", "Avatar",
        "Blade Runner 2049", "Arrival", "Dune", "Gravity",
        "The Martian", "Edge of Tomorrow"
    ],

    "Fantasy": [
        "Harry Potter", "The Lord of the Rings", "The Hobbit",
        "Fantastic Beasts", "The Chronicles of Narnia", "Pan's Labyrinth",
        "Stardust", "Maleficent", "Alice in Wonderland", "The Green Knight"
    ],

    "Mystery": [
        "Knives Out", "Sherlock Holmes", "Murder on the Orient Express",
        "The Prestige", "The Da Vinci Code", "Zodiac", "The Others",
        "Identity", "Searching", "The Sixth Sense"
    ],

    "Adventure": [
        "Jurassic Park", "Jumanji", "Indiana Jones",
        "Pirates of the Caribbean", "The Mummy", "King Kong",
        "Uncharted", "National Treasure", "Life of Pi", "The Revenant"
    ],

    "Drama": [
        "Forrest Gump", "The Shawshank Redemption",
        "The Pursuit of Happyness", "Good Will Hunting",
        "The Green Mile", "A Beautiful Mind", "Whiplash",
        "The Social Network", "Little Women", "Manchester by the Sea"
    ],

    "Crime": [
        "The Godfather", "Goodfellas", "The Departed", "Scarface",
        "Pulp Fiction", "Heat", "Casino", "The Irishman",
        "American Gangster", "Once Upon a Time in America"
    ],

    "Animation": [
        "Toy Story", "Frozen", "The Lion King", "Finding Nemo",
        "Moana", "Coco", "Up", "Inside Out",
        "Zootopia", "How to Train Your Dragon"
    ],

    "Documentary": [
        "Our Planet", "Free Solo", "The Social Dilemma",
        "My Octopus Teacher", "13th", "Won't You Be My Neighbor?",
        "Icarus", "March of the Penguins", "Blackfish", "Man on Wire"
    ],

    "Historical": [
        "Gladiator", "Troy", "Lincoln", "Schindler's List",
        "The Last Samurai", "Braveheart", "Dunkirk",
        "12 Years a Slave", "The King's Speech", "Darkest Hour"
    ],

    "Musical": [
        "The Greatest Showman", "La La Land", "Mamma Mia!",
        "West Side Story", "Les Miserables", "Chicago",
        "Sing", "Sing 2", "Moulin Rouge!", "Rocketman"
    ],

    "Family": [
        "Paddington", "Matilda", "The Parent Trap",
        "Charlie and the Chocolate Factory", "Home Alone",
        "Mrs. Doubtfire", "The Incredibles", "Mary Poppins",
        "Wonder", "Night at the Museum"
    ],

    "War": [
        "Saving Private Ryan", "1917", "Dunkirk", "Fury",
        "Hacksaw Ridge", "Black Hawk Down", "Platoon",
        "Full Metal Jacket", "All Quiet on the Western Front",
        "Letters from Iwo Jima"
    ],

    "Superhero": [
        "Iron Man", "Spider-Man", "Black Panther", "Wonder Woman",
        "Thor", "Captain America: The Winter Soldier",
        "The Avengers", "Doctor Strange", "Guardians of the Galaxy",
        "Batman Begins"
    ],

    "Psychological": [
        "Shutter Island", "Black Swan", "Fight Club",
        "The Machinist", "Joker", "American Psycho",
        "Mulholland Drive", "Donnie Darko", "Memento", "Taxi Driver"
    ],

    "Sports": [
        "Rocky", "Creed", "Chak De! India", "Ford v Ferrari",
        "Moneyball", "Rush", "The Blind Side", "Remember the Titans",
        "Million Dollar Baby", "Dangal"
    ]
}


print("===== Movie Recommendation System =====")

print("\nAvailable Preferences:")

for genre in movies:
    print("-", genre)


preference = input("\nEnter your preferred genre: ").strip().title()


if preference in movies:

    print("\nRecommended Movies for you:")

    for movie in movies[preference]:
        print("-", movie)

else:

    print("\nSorry, that genre is not available.")
    print("Please choose a genre from the list.")
