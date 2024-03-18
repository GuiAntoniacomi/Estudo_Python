from google import search

def obter_palavras_chave(site, num_resultados=10):
    palavras_chave = []
    try:
        resultados = search(f"site:{site}", num=num_resultados, stop=num_resultados, pause=2)
        for resultado in resultados:
            palavras_chave.extend(resultado.split())
    except Exception as e:
        print("Ocorreu um erro ao realizar a pesquisa:", e)
    
    return palavras_chave

def contar_ocorrencias_palavra_chave(palavras_chave):
    contagem = {}
    for palavra_chave in palavras_chave:
        if palavra_chave in contagem:
            contagem[palavra_chave] += 1
        else:
            contagem[palavra_chave] = 1
    return contagem

def main():
    site = input("Digite o site que deseja analisar: ")
    num_resultados = int(input("Digite o número de resultados de pesquisa a serem analisados (máximo 100): "))
    
    palavras_chave = obter_palavras_chave(site, num_resultados)
    contagem_palavras_chave = contar_ocorrencias_palavra_chave(palavras_chave)
    
    print("\nPalavras-chave e suas contagens:")
    for palavra_chave, contagem in contagem_palavras_chave.items():
        print(f"{palavra_chave}: {contagem}")

if _name_ == "_main_":
    main()