# -*- coding: UTF-8 -*-

#Retornar o maior elemento de uma lista

def maior_elemento(lista):
	lista.sort(reverse=True)
	return lista[0]

lista = [0,8,9,7,19,9,1]

maior = maior_elemento(lista)
print(maior)

