# Recursão

Toda função recursiva necessariamente precisa possuir dois casos indispensáveis:

- caso base
- caso recursivo

O **Caso Recursivo** é quando a função chama a si mesma, já o **Caso Base** é quando a função não chama a si mesma novamente, evitando um loop infinito.

```python
def regressive(i):
    # caso base
    if i < 0:
        return

    #caso recursivo
    print(i)
    regressive(i - 1)
```
