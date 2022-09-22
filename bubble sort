""" UTILIZANDO A LINGUAGEM PYTHON """

# Definindo uma função.
def bubleSort(lista):
    # Criando uma variável para controlar o laço de repetição, while.
    finalizada = False
    
    # Caso finalizada seja igual a false entre no laço de repetição.
    while not finalizada:
        # Iniciando com a variável de controle em True.
        finalizada = True
        
        # Laço de repetição para organização do vetor.
        for i in range(len(lista)-1):
            # Verificação do valores do vetor.
            if lista[i+1] < lista[i]:
                
                # Armazenando o valor a ser trocado.
                valorAnterior = lista[i]
                # Duplicando valor.
                lista[i] = lista[i+1]
                # Colocando o valor salvo no valor posterior. Assim com esses passos havendo uma troca.
                lista[i+1] = valorAnterior
                # Indicando para o algoritmo que nesse laço houve uma auteração no vetor, logo, talvez, o vetor ainda precise de mais uma passagem.
                finalizada = False
    
    # Retorno da função, a lista já organizada.
    return lista

# Vetor qualquer.
vetor = [10,9,8,7,6,5,4,3,2,1]
# Impressão.
print(bubleSort(vetor))
