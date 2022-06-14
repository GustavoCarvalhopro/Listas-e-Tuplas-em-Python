conjunto ={1,2,3,4, 2 ,3}
conjunto.add(5)

print(type(conjunto))
print(conjunto)

conjunto.discard(1)
print(conjunto)

conjunto2 = {5,6,7,8,9,10}
print(conjunto2)

conjunto_uniao = conjunto.union(conjunto2)
print('União entre conjunto 1 e 2: {}' .format (conjunto_uniao))


conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))
