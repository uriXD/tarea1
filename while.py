trikki = 'larga vida y prosperidad'
secuencia = ["uno", 2, trikki,[1,2,3,4,5]]
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
	print edad