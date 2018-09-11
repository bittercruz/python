#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#Retornar a soma dos elementos com valor negativo

from funcoes import get_lista

def qtde_vizinhos(lista):
	i = 0
	vizinhos = 0
	tamanho = len(lista)
	for valor in lista:
		if i<(tamanho-1):
			if (valor == lista[i+1]):
				vizinhos += 1
		i += 1
	return vizinhos

lista = get_lista()
vizinhos = qtde_vizinhos(lista)
print("A quantidade de vizinhos iguais é {}".format(vizinhos))

