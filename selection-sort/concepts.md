# Ordenação por Seleção

A ordenação por seleção é um algoritmo de ordenação simples que funciona _interativamente_ selecionando o menor elemento de uma lista não ordenada e trocando-o com o primeiro não ordenado.

O Processo é repetido até que toda a lista esteja ordenada, abaixo temos um exemplo de implementação do algoritmo em python.

```python
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
# Lista ordenada: [11, 12, 22, 25, 64]
```

_Adendo: A Ordenação por seleção não é o algoritmo mais eficiente para grandes conjuntos de dados, pois tem uma complexidade de tempo de O(n²). No entanto, é fácil de entender e implementar, e funciona bem para conjuntos de dados pequenos._