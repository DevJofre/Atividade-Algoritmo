def extrair_dados(dado):
    
    data, resto = dado.split(": ")
    max_temp = int(resto.split(", ")[0].split("=")[1])
    min_temp = int(resto.split(", ")[1].split("=")[1])
    chuva = float(resto.split(", ")[2].split("=")[1].replace("mm", ""))
    return data, max_temp, min_temp, chuva

def calcular_media(temperaturas):
    
    return sum(temperaturas) / len(temperaturas) if temperaturas else 0

def analisa_meteorologia(dados):
    max_temperaturas = []
    min_temperaturas = []
    dia_maior_precipitacao = None
    dia_menor_temperatura = None
    maior_precipitacao = -1
    menor_temperatura = float('inf')
    dias_quentes_sem_chuva = []

    for dado in dados:
        data, max_temp, min_temp, chuva = extrair_dados(dado)

 
        max_temperaturas.append(max_temp)
        min_temperaturas.append(min_temp)


        if chuva > maior_precipitacao:
            maior_precipitacao = chuva
            dia_maior_precipitacao = data


        if min_temp < menor_temperatura:
            menor_temperatura = min_temp
            dia_menor_temperatura = data


        if max_temp > 30 and chuva == 0:
            dias_quentes_sem_chuva.append(data)


    media_max_temp = calcular_media(max_temperaturas)
    media_min_temp = calcular_media(min_temperaturas)


    print(f"\nMédia de temperatura máxima do mês: {media_max_temp:.2f}")
    print(f"Média de temperatura mínima do mês: {media_min_temp:.2f}")
    print(f"Dia com maior precipitação: {dia_maior_precipitacao} ({maior_precipitacao}mm)")
    print(f"Dia com menor temperatura mínima: {dia_menor_temperatura} ({menor_temperatura}°C)")
    print(f"Dias com temperatura máxima > 30°C e sem chuva: {dias_quentes_sem_chuva}")

def inserir_dados():
    dados = []
    while True:
        entrada = input("Insira os dados no formato 'YYYY-MM-DD: Máxima=X, Mínima=Y, Chuva=Zmm' ou digite 'sair' para finalizar: ")
        if entrada.lower() == 'sair':
            break
        dados.append(entrada)
    return dados


def main():
    print("Bem-vindo ao analisador de dados meteorológicos!")
    dados_meteorologicos = inserir_dados()
    
    if dados_meteorologicos:
        analisa_meteorologia(dados_meteorologicos)
    else:
        print("Nenhum dado foi inserido.")


main()
