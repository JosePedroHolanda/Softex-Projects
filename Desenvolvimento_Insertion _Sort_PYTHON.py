def insertion_sort(lista):
  print(len(lista))
  for i in range(1, len(lista)):
    pos_atual = lista[i]
    pos_anterior = i -1

    while pos_anterior >= 0 and pos_atual < lista[pos_anterior]:
      lista[pos_anterior + 1] = lista[pos_anterior]
      pos_anterior =- 1

    lista[pos_anterior + 1] = pos_atual

vetor=[41,39,31,13,37,15,33,3,29,7,17,35,9,21,25,5,11,51,23,27,19]
insertion_sort(vetor)
print(vetor)
