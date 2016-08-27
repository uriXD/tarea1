#!/usr/bin/env python
tokens={'#':0,"main":2,"int":34,'{':90,"void":65}
caracteres_validos = "#{"
f = open("Lexico.c")
arreglo = []
palabra = ' '
while True:
	c = f.read(1)
	if not c:
		print "Se termino el archivo:"
		break
	if c == '\n':
		print "Espacio1: = "
		palabra = ''.join(arreglo)
		arreglo = []
		c = f.read(1)

	elif c == ' ':
		palabra = ''.join(arreglo)
		print 'Espacio2: = ' + palabra, '-'
		arreglo = []

	elif caracteres_validos.find(c) >= 0:
		print "Es caracter valido: ", tokens[c]

	#print "Caracter:", c
	arreglo.append(c)
f.close()

# 1) 