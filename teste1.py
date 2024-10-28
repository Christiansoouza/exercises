lista = [1,'teste',2,'oi','ola',1,2,4]

lista_teste = [i for i,item in enumerate(lista) if isinstance(item, str)]

print(lista_teste)
