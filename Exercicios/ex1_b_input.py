#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#Retornar a soma de elementos de uma lista

def soma(lista):
	soma_item = 0
	#tamanho = len(lista)
	for item in lista:
		#soma_item = soma_item + int(item)
		soma_item += int(item)
	return soma_item

#lista = [x for x in input("Insira a lista: ").split()]

def get_lista():
	
	input_user = input("Insira a lista separada por espaços: ")
	lista = input_user.split()
	return lista

lista = get_lista()
total = soma(lista)
print(total)

