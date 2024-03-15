n = int(input('Quantos numeros da sequeência de Fibonacci você deseja gerar?'))
       
fibo_seq = [0, 1]

while len(fibo_seq) < n:
    pn = fibo_seq[-1] + fibo_seq[-2]
    fibo_seq.append(pn)

fibonacci_string = " → ".join(map(str, fibo_seq[:n]))

print("Sequência de Fibonacci com os primeiros", n, "números:")
print(fibonacci_string)
print('FIM')