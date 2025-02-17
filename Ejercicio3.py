"""
Torres de hanoi
"""

def hanoi(n, origen, destino, aux):
    if n == 1:
        print(f"Disco {n} de {origen} a {destino}")
    else:
        hanoi(n-1, origen, aux, destino)
        print(f"Disco {n} de {origen} a {destino}")  
        hanoi(n-1, aux, destino, origen)

hanoi(3, "A", "B", "C")


