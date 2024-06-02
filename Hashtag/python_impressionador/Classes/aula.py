
class TV:

    cor = 'preta'
    
    def __init__(self, tamanho):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        

tv_sala = TV(tamanho=70)
tv_quarto = TV(tamanho=43)

tv_quarto.mudar_canal('HBO Max')
tv_sala.mudar_canal('YouTube')

print(tv_quarto.tamanho, tv_quarto.canal)
print(tv_sala.tamanho, tv_sala.canal)

   
