def modificar(lista):
    
    lista = list(set(lista))
    
    lista.sort(reverse=True)
    
    
    lista = [num for num in lista if num % 2 == 0]
    
    suma = sum(lista)
    
    lista.insert(0, suma)
    
    return lista


lista = [4, 7, 2, 9, 10, 21, 12, 7, 4]
print(modificar(lista))