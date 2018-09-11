#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#Retornar a soma dos elementos com valor negativo

from funcoes import get_lista

def eh_igual(lista1, lista2):
	if (lista1 == lista2):
		return True
	else:
		return False
	

lista_1 = get_lista()
lista_2 = get_lista()

if eh_igual(lista_1, lista_2):
	print("Listas iguais")
else:	
	print("Listas diferentes")

