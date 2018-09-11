#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#Retornar a soma dos elementos com valor negativo

from funcoes import get_lista

def cria_listas(lista):
	x = 0
	z = 0
	
	listas = []
	tamanho = len(lista)
	while (x <= (tamanho)):
		y = 0
		while (y <= (tamanho)):
			print("x,y:{},{}".format(x,y))
			#listas[z] = [lista[x],lista[y]]
			#print(listas[z])
			z += 1
			y += 1
		x += 1
	return listas 
	
lista = get_lista()
lista_de_duplas = cria_listas(lista)
print(lista_de_duplas)

