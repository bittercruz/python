#!/usr/bin/python3

# -*- coding: UTF-8 -*-

def get_lista():
	
	input_user = input("Insira a lista separada por espaços: ")
	lista = input_user.split()
	return lista

def soma(lista):
	soma_item = 0
	for item in lista:
		soma_item += int(item)
	return soma_item