def listamuunnos():
    for jako in lista:
        if jako % 2 == 0:
            lista.remove(jako)
    return lista

lista = [1,2,3,6]
print(lista)
print(listamuunnos())