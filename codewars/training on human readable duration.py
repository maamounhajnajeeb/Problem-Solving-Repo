def format_duration(number : int):
    laLista = {"First":"", "Second":"", "Third":"", "Fourth":"", "Fifth":""}

    # helper functions
    def findyear(number:int):
        result = number // 31536000
        advance = number % 31536000
        return result, advance
    def findDay(number:int):
        result = number // 86400
        advance = number % 86400
        return result, advance
    def findHr(number:int):
        result = number // 3600
        advance = number % 3600
        return result, advance
    def findMin(number:int):
        result = number // 60
        advance = number % 60
        return result, advance

    # Study number func
    def studyNumber(lista : list):
        counter = 0
        while counter < len(lista):
            try:
                element = int(lista[counter][:2])
            except ValueError:
                element = int(lista[counter][:1])
            if element > 1:
                lista[counter] += "s"
            counter += 1
        return lista

    def findPhrase(lista : list):
        phrase = ""
        for word in lista:
            phrase += word
        return phrase

    def branchFunc(number):
        new = []
        if number == 0: return "now"
        elif number >= 31536000:
            result, advance = findyear(number)
            laLista['First'] = f"{result} year"
            branchFunc(advance)
        elif number >= 86400:
            result, advance = findDay(number)
            laLista['Second'] = f"{result} day"
            branchFunc(advance)
        elif number >= 3600:
            result, advance = findHr(number)
            laLista["Third"] = f"{result} hour"
            branchFunc(advance)
        elif number >= 60:
            result, advance = findMin(number)
            laLista["Fourth"] = f"{result} minute"
            branchFunc(advance)
        elif number < 60 and number > 0:
            laLista["Fifth"] = f"{number} second"
        # making list here
        new = [laLista[key] for key in laLista if laLista[key] != ""]
        # Studying the number
        new = studyNumber(new)
        # Studying and situation
        phrase = ""
        if len(new) == 1:
            phrase = new[0]
        elif len(new) == 2:
            new.insert(1, " and ")
            phrase = findPhrase(new)
        elif len(new) == 3:
            new.insert(1, ", ")
            new.insert(3, " and ")
            phrase = findPhrase(new)
        elif len(new) == 4:
            new.insert(1, ", ")
            new.insert(3, ", ")
            new.insert(5, " and ")
            phrase = findPhrase(new)
        elif len(new) == 5:
            new.insert(1, ", ")
            new.insert(3, ", ")
            new.insert(5, ", ")
            new.insert(7, " and ")
            phrase = findPhrase(new)
        return phrase

    number = branchFunc(number)
    return number

# Some Tests Cases

# print(format_duration(1))
# print(format_duration(59))
# print(format_duration(60))
# print(format_duration(61))
# print(format_duration(120))
# print(format_duration(121))
# print(format_duration(122))
# print(format_duration(3599))
# print(format_duration(3600))
# print(format_duration(3661))
# print(format_duration(3721))
# print(format_duration(7201))
# print(format_duration(7322))
# print(format_duration(2688000))
# print(format_duration(31536000*2))
