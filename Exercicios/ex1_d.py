#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#Retornar a média dos elementos da lista

from funcoes import get_lista, soma

def media(lista):
	tamanho = len(lista)
	soma_total = int(soma(lista))
	media = float(soma_total/tamanho)
	return media

lista = get_lista()
print("A média é {0:5.2f}".format(media(lista)))

