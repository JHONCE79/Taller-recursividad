"""
Palindromo
"""

def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return palindromo(palabra[1:-1])
    
print(palindromo("steven"))

 