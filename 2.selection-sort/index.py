# a função busca_menor itera através da lista recebida pelo parâmetro
# a cada iteração da lista é verificado se número iterado é menor que o armazenado na variável *menor* declarada na terceira linha da função
# caso seja menor, o valor da variável é alterado, contendo até então o menor número possível
#
# essa iteração se repete até o último elemento da lista e por final retorna o índice do menor número encontrado na lista.

def busca_menor(lista):
    menor = lista[0]
    menor_indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    return menor_indice

# a função ordenacao_por_selecao declara uma lista vazia e itera através da lista recebida via parãmetro
# ara cada item na lista recebida, é executada a função busca_menor para buscar o menor número possível da lista recebida por ordenacao_por_selecao
# após isso é removido o menor número da lista recebida ao mesmo tempo que o adiciona na nova lista, repetindo o ciclo até a lista estar completamente ordenada

def ordenacao_por_selecao(lista):
    nova_lista = []
    for _ in range(len(lista)):
        menor = busca_menor(lista)      
        nova_lista.append(lista.pop(menor))
    return nova_lista

print(ordenacao_por_selecao([4, 5, 8, 3, 2,12, 3, 1])) 



def selection_sort(arr):
    n = len(arr)

    # Percorre toda a lista
    for i in range(n - 1):
        # Assume que o índice atual é o menor
        min_index = i

        # Procura o menor elemento no restante da lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Troca o elemento atual com o menor elemento encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso
lista = [64, 25, 12, 22, 11]
selection_sort(lista)
print("Lista ordenada:", lista)