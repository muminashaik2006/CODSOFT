def literary_book_recommendation():

    books = {

        "1980s": {
            "novel": [
                ("Veyi Padagalu", 4.9),("Asamardhuni Jeeva Yatra", 4.8),("Chivaraku Migiledi", 4.7),("Alpajeevi", 4.6),("Matti Manushulu", 4.5)
            ],

            "poetry": [
                ("Maha Prasthanam", 4.9),("Khadga Srushti", 4.8),("Siprali", 4.7),("Mutyala Saralu", 4.6),("Agni Dhaara", 4.5)
            ],

            "comedy": [
                ("Barrister Parvateesam", 4.9),("Ganapathi", 4.7),("Budugu", 4.8),("Iddaru Ammayilu", 4.5),("Navvula Lokam", 4.4)
            ],

            "mythology": [
                ("Andhra Mahabharatam", 4.9),("Bhagavatam", 4.8),("Ramayanam", 4.8),("Srikrishna Rayabaram", 4.7),("Harivamsam", 4.6)
            ]
        },

        "1990s": {
            "novel": [
                ("Antarmukham", 4.8),("Tulasi Dalam", 4.9),("Aakasamlo Sagam", 4.7),("Jeevana Tarangalu", 4.8),("Mouna Poratam", 4.6)
            ],

            "romance": [
                ("Prema Lekhalu", 4.8),("Maidanam", 4.7),("Kalala Kougili", 4.6),("Prema Nagar", 4.5),("Priyuralu Pilichindi", 4.4)
            ],

            "stories": [
                ("Amaravati Kathalu", 4.9),("Galivana", 4.8),("Mithunam", 4.8),("Smruthi Rekhalu", 4.6),("Kathala Sampooti", 4.5)
            ],

            "biography": [
                ("Buddhuni Jeevitam", 4.7),("Veeresalingam Charitra", 4.8),("Ambedkar Jeevitam", 4.9),("Gandhi Jeevita Gatha", 4.8),("APJ Abdul Kalam Jeevitam", 4.9)
            ]
        },

        "2000s": {
            "novel": [
                ("In The Mood For Love", 4.7),("Soul Circus", 4.8),("Long March", 4.7),("Sira", 4.8),("Cheekati Rojulu", 4.6)
            ],

            "romance": [
                ("Naa Ishtam", 4.5),("Prema Oka Maikam", 4.7),("Malli Premistava", 4.6),("Kalala Teeram", 4.5),("Prema Yatra", 4.4)
            ],

            "self-help": [
                ("Vijayaniki Aidu Metlu", 4.8),("Gelupu Pilupu", 4.7),("Atma Vishwasam", 4.8),("Jeevita Satyalu", 4.6),("Success Margam", 4.5)
            ],

            "technology": [
                ("Computer Basics Telugu", 4.6),("Internet Guide", 4.5),("Programming Parichayam", 4.7),("Technology Today", 4.5),("Digital World", 4.4)
            ]
        },

        "2020s": {
            "novel": [
                ("Yodha", 4.8),("Asatyaniki Aavala", 4.7),("Manovalam", 4.8),("Agnipatham", 4.6),("Jeevana Rekhalu", 4.5)
            ],

            "self-help": [
                ("Mind Power", 4.8),("Success Formula", 4.7),("Positive Thinking", 4.8),("Goal Setting", 4.6),("Lead Yourself", 4.5)
            ],

            "motivation": [
                ("Gelupu Nee Sontham", 4.9),("Dream Big", 4.8),("Never Give Up", 4.8),("Rise Again", 4.7),("Inspiration", 4.6)
            ],

            "technology": [
                ("Artificial Intelligence", 4.9),("Machine Learning Basics", 4.8),("Python Programming", 4.9),("Data Science Guide", 4.8),("Cyber Security", 4.7)
            ]
        }
    }

    print("=" * 60)
    print("      TELUGU AND ENGLISH BOOK RECOMMENDATION SYSTEM")
    print("=" * 60)

    while True:

        print("\nAvailable Decades:")
        for decade in books:
            print("-", decade)

        decade = input("\nEnter preferred decade: ").strip()

        if decade not in books:
            print("\nSorry! Books are not available for this decade.")
            continue

        print("\nAvailable Genres:")
        for genre in books[decade]:
            print("-", genre.title())

        genre = input("\nEnter preferred genre: ").lower().strip()

        if genre not in books[decade]:
            print("\nSorry! This genre is not available in the selected decade.")
            continue

        print(f"\nRecommended {genre.title()} Books from {decade}:\n")

        for book, rating in books[decade][genre]:
            print(f"📚 {book}  | ⭐ Rating: {rating}/5")

        choice = input(
            "\nWould you like more recommendations? (yes/no): "
        ).lower().strip()

        if choice != "yes":
            print("\nThank you for using the Telugu and English Book Recommendation System!")
            break

literary_book_recommendation()
