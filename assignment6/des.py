
def answer(recidence: str) -> str:
    list1 = [
        "Reykjavik",
        "Kopavogur",
        "Hafnarfjordur",
        "Reykjanesbaer",
        "Gardabaer",
        "Mosfellsbaer",
        "Arborg",
        "Akranes",
        "Seltjarnarnes"]
    list2 = ["Akureyri", "Fjardabyggd", "Mulathing"]
    city = recidence
    if (city in list1):
        return "Reykjavik"
    elif (city in list2):
        return "Akureyri"
    else:
        return "Invalid option."


def main() -> None:
    data = input()
    answer(data)


if __name__ == "__main__":
    main()
