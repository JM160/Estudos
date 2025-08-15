def min_contracoes_palindromo(lista):
    esq = 0
    dir = len(lista) - 1
    operacoes = 0

    while esq < dir:
        if lista[esq] == lista[dir]:
            # Elementos iguais → só anda os ponteiros
            esq += 1
            dir -= 1
        elif lista[esq] < lista[dir]:
            # Soma dois da esquerda
            lista[esq + 1] += lista[esq]
            esq += 1
            operacoes += 1
        else:
            # Soma dois da direita
            lista[dir - 1] += lista[dir]
            dir -= 1
            operacoes += 1

    return operacoes


# Leitura de entrada
n = int(input())
lista = list(map(int, input().split()))

# Saída
print(min_contracoes_palindromo(lista))
