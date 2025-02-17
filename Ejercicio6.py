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
            nuevo = text[:i] + primero + text[i:]
            combinations.append(nuevo)
        return combinations
                   

print(anagrama("abc"))