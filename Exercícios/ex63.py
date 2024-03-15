n = int(input('Quantos numeros da sequeência de Fibonacci você deseja gerar?'))
       
fibo_seq = [0, 1]

while len(fibo_seq) < n:
    pn = fibo_seq[-1] + fibo_seq[-2]
    fibo_seq.append(pn)

fibonacci_string = " → ".join(map(str, fibo_seq[:n]))

print("Sequência de Fibonacci com os primeiros", n, "números:")
print(fibonacci_string)
print('FIM')

# Correção Guanabara
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('-'*30)
print(f'{t1} → {t2}', end=" ")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} → ', end=" ")
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')