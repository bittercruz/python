#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#Retornar o num de ocorrências do primeiro elemento da lista 

from funcoes import get_lista

def num_ocorrencias(lista):
	tamanho = len(lista)
	ocorrencia = 0
	for item in lista:
		if item == lista[0]:
			ocorrencia += 1
	return ocorrencia

lista = get_lista()
ocorrencias = num_ocorrencias(lista)
print("O número de ocorrências é {}".format(ocorrencias))


