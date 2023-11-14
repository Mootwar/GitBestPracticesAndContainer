def solve(recidence: str) -> str:
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
        return ("Not a valid option")


testData = input()
solve(testData)
