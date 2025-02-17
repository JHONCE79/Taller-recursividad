"""
Anagramas
"""

def anagrama(text):
    if text == "":
        return []
    else:
        primero = text[0]
        restante = text[1:]
        combinations = []
        for i in anagrama(restante):
            combinations.append(i)
        return combinations
                   

print(anagrama("abc"))