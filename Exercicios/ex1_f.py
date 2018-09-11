#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#Retornar a soma dos elementos com valor negativo

from funcoes import get_lista

def soma_negativa(lista):
	tamanho = len(lista)
	soma = 0
	for valor in lista:
		if ((valor) < "0"):
			soma += int(valor)
	return soma

lista = get_lista()
soma = soma_negativa(lista)
print("A soma dos números negativos é {}".format(soma))

