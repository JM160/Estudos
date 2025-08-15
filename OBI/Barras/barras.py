N = int(input())
X = list(map(int, input().split()))
H = max(X)

for i in range(H):
    linha = []
    for x in X:
        if x >= H - i:
            linha.append('1')
        else:
            linha.append('0')
    print(' '.join(linha))