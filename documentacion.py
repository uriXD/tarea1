
#: c01:if.py
#codigo 1
response = "yes"
if response == "yes":
  print "affirmative"
  val = 1
print "continuing..."
#<hr>
output = '''
affirmative
continuing...
'''

# 1) tabulacion, al momento de mover la tabulacion del "val = 1"
# nos marca el siguiente error:

#  File "if.py", line 5
#    val = 1
#    ^

# 2) el valor del output puede ser cambiado con " "

# 3) al quitar una '  en output, este nos marca un error

# 4) si la condicion del if esta entre (), no importa, la condicion al final se realiza

# 5) al mover la tabulacion del primer print en el if, nos marca error

# 6) el valor "yes" del response, puede cambiarse directamente aun valor booleano, pero
# este debe de ser True, osea con mayuscula al principio, si no no lo reconocera.

#################

#codigo 2

trikki = "larga vida y prosperidad"
secuencia = ["uno", 2, trikki]
for elemento in secuencia:
	print elemento

def saluda(ed):
	print "Felicidades, tu edad es de " + str(ed)

edad = 0
while edad <= 18:
	if edad == 18:
		saluda(edad)
		break
	else: 
		edad = edad + 1
	print str(edad)

#1) pues la tabulacion, y modificamos la tabulacion en el if o else o donde sea, lo mas probable es que nos marque un error

#2) si quitamos el str de la funcion saluda, nos marcara error, debido a que el print no , puede imprimir una cadena, y ala vez
#una concatenacion de un entero, este se tiene que transformar en cadena primero para concatenar.

#3)se puede cambiar las " ", por  ' ' en el trikki

#4) el ultimo print, puede ser cambiado y dejar solo el nombre de la variable edad, print edad, ya que el print por si
# solo puede regresar enteros flotantes etc.

#5) como python es un lenguaje ROTO, nos permite aguardar una lista dentro de otra lista ejemplo:
#  secuencia = ["uno", 2, trikki,[1,2,3,4,5]]

#6) quitar el break, cicla el programa, y este no puede ser remplazad por return

#######################
#codigo 3
#: c01:sum.py
def sum(arg1, arg2):
  return arg1 + arg2

print sum(42, 47)
print sum('spam ', "eggs")
#<hr>
output = '''
89
spam eggs
'''

#1) los datos al igual que muchos lenguajes, se pueden pedir, atravez de raw_input()

#2) declarar funciones, en python, es mas sencillo ya que no tenemos que declarar el tipo
# de variables que este resivira.

#3) como se ve en el segundo print, se puede mandar cadenas con " ", ' '

#4) en el primer print, no solo se pueden mandar enteros, sino tambien enteros y flotantes
# y el return los regresa la suma.

#5) los 2 print se pueden concatenar, con un srt, ejemplo: print str( sum(40,49.5) ) + sum('spam ', "eggs")


#codigo 4
print "That isn't a horse"
print 'You are not a "Viking"'
print """You're just pounding two
coconut halves together."""
print '''"Oh no!" He exclaimed.
"It's the blemange!"'''
print r'c:\python\lib\utils'

#1) mientras este entre comillas los print no tendran problemas .

#codigo 5
def myFunction(response):
  val = 0
  if response == "yes":
    print "affirmative"
    val = 1
  print "continuing..."
  return val

print myFunction("no")
print myFunction("yes")

# codigo 6

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

#1) al mover las tabulaciones de los if, el programa truena

#2) el almacenamiento de los tokens es como otros lenguajes, pero igual
# sin espesificar el tipo.

#3) python puede abrir un archivo externo como otros lenguajes, pero este 
# no necesitamos indicar un tipo de variable , para la variable que guerde el contenido del archivo.

#4) el if se maneja igual pero un poco diferente que otros lenguajes, por ejemplo el if no, y elif

#5 podemos usar funciones especiales para agilizar o agregar datos a la lista, join, find, append.
 