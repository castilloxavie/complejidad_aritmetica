import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elementos in lista:
        if elementos == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    tamanho_lista =  int(input("DE que tamaño sera la lista: "))
    objetivo = int(input("Que numero quieres encontrar: "))

    lista = [random.randint(0,100) for i in range(tamanho_lista)]

    encontrado = busqueda_lineal(lista, objetivo) 
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')