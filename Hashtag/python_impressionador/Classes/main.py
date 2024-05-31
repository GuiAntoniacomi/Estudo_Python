from ContasBancos import ContaCorrente, CartaoCredito


conta_Guizo = ContaCorrente('Guizo',  '000.000.000-01', 1234, 98765)
cartao_Guizo = CartaoCredito('Guizo', conta_Guizo)
print(cartao_Guizo._senha)

print(conta_Guizo.__doc__)

