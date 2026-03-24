from entitites.Ranking import *
from AutoComplete import AutoComplete

def main():
    dictionary = [
        "car", "cat", "cart", "cartoon", "canada", "candy",
        "car", "canada", "canada", "car", "canada", "canopy", "captain"
    ]

    service = AutoComplete(Alphabetical(), 5)
    service.add_words(dictionary)

    prefix = "car"
    sugg = service.get_suggestions(prefix)

    print(f"Suggestions: {sugg}")

if __name__ == '__main__':
    main()