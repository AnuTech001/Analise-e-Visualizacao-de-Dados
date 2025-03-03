from Bibliotecas_Clima import pandinha as pd
from Bibliotecas_Clima import cor

# Quebra linhas
ql1 = cor.Fore.CYAN + "." * 48 + cor.Style.RESET_ALL
ql2 = cor.Fore.CYAN + "=" * 118 + cor.Style.RESET_ALL
ql3 = cor.Fore.CYAN + "-" * 118 + cor.Style.RESET_ALL

# DataFreme
dados = {
    "Data": ["15/01/2025"] * 5,
    "Cidade": ["São Paulo - SP", 
               "Rio de Janeiro - RJ", 
               "Curitiba - PR",
               "Porto Alegre - RS",
               "Salvador - BA"],
    "Máximas (°C)": [35.5,
                    35.0,
                    24.0,
                    28.0,
                    31.0],
    "Mínimas (°C)": [22.0,
                     25.0,
                     18.0,
                     20.0,
                     24.5],
    "Precipitação (mm)": [12.0,
                          None,
                          8.0,
                          15.0,
                          None],
    "Umidade Relativa (%)": [78,
                             70,
                             None,
                             82,
                             80],
}

df = pd.DataFrame(dados)

# Substituir valores ausentes na coluna Precipitação pela média
df["Precipitação (mm)"] = df["Precipitação (mm)"].fillna(df["Precipitação (mm)"].mean())

# Substituir valores ausentes na coluna Umidade Relativa pela mediana
df["Umidade Relativa (%)"] = df["Umidade Relativa (%)"].fillna(df["Umidade Relativa (%)"].median())


# Adicionar a nova coluna: Amplitude Térmica
df["Amplitude Térmica"] = df["Máximas (°C)"] - df["Mínimas (°C)"]

# Filtro para as cidades com temperaturas superiores a 30 °C
df_filtro = df[df["Máximas (°C)"] > 30]

# Reorganizar colunas
colunas_ordem = [
    "Data", "Cidade", "Máximas (°C)", "Mínimas (°C)",
    "Amplitude Térmica", "Precipitação (mm)", "Umidade Relativa (%)"
]

print(ql1)
print(cor.Fore.LIGHTBLUE_EX + "Bem-vindo ao Programa de Monitoramento Climático" + cor.Style.RESET_ALL)
print(ql1)

while True:
    # Mostrando os DataFrames
    print(ql2)
    print(cor.Fore.GREEN + "DataFrame processado\n" + df.to_string(index=False) + cor.Style.RESET_ALL)
    print(ql3)
    print(cor.Fore.BLUE + "DataFrame Filtrado:\n" + df_filtro.to_string(index=False) + cor.Style.RESET_ALL)
    print(ql2)

    # Perguntar ao usuário se deseja encerrar
    resposta = input(cor.Fore.YELLOW + "\nDeseja Encerrar o programa? n - Não || Sim, qualquer tecla menos 'n': ")

    if resposta.lower() == 'n':
        print(cor.Fore.GREEN + "Continuando o programa...\n" + cor.Style.RESET_ALL)
    else:
        print(cor.Fore.RED + "Programa encerrado.\nPrecione 'Enter' para fechar o terminal" + cor.Style.RESET_ALL)
        break

input()