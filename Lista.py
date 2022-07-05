lista = [1, 3, 5 ,7]
lista_animal = ['cachorro','gato','elefante','papagaio']

#a lista sempre começa a partir da posição '0' então o 1 e o cachorro estão na posição '0'!
#Strings são exibidas a partir da ordem alfabetica a b c d e f.....

print(lista_animal[0])
print(lista[3])

#Também posso buscar um numero máximo e minimo dentro de um lista de números.

print(max(lista_animal))
print(min(lista))
print(lista_animal[0])

#Podemos utilizar a soma entre os números também.

print(sum(lista))


# para fazer o for passar pela lista toda utiliza-se o for valor in lista:
#todo processo é feito uma conta de numero a número.
soma = 0
for x in lista:
    print (x)
    soma += x
print(soma)    


entrada =(input('Digite o animal que quer encontrar na lista: '))
if entrada in lista_animal:
    print('Existe um {} na lista ' .format (entrada))
else:
    print('não existe o animal {} na lista' .format(entrada))    


# Tupla são listas imutavéis
tupla = (1,2,15,16)
print(len(tupla))
print(tupla)

#Faz uma conversão de uma lista para uma tupla.
tupla_anima = tuple (lista_animal)
print(lista_animal)
print(type(tupla_anima))
print(tupla_anima)

#Altera o valor apontado na lista
lista_animal[0] = 'lobo'
print(lista_animal)
lista[1] = 100
print(lista)

#Faz com que a lista sejá ordenada
lista_animal.sort()
print(lista_animal)
lista.sort()
print(lista)

#Faz com que a lista seja ordenada de trás pra frente
lista_animal.reverse()
lista.reverse()
print(lista_animal)
print(lista)