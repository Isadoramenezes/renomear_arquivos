import os

for arquivo in os.listdir('./arquivos_para_renomear'):
    dados = str(arquivo).split("-")
    if(dados[0]=="DOEAL"):
        dados_padrao_doeal = str(dados[1]).split("_")
        ano = dados_padrao_doeal[2]
        mes = dados_padrao_doeal[1]
        dia = dados_padrao_doeal[0]

    else:
        ano = dados[0]
        mes = dados[1]
        dia = str(dados[2]).split("_")[0]

    nome_padrao = ano + "-" + mes + "-" + dia + ".pdf"
    os.rename("./arquivos_para_renomear/" + arquivo,"./arquivos_renomeados/" + nome_padrao )
    print("arquivo: " + arquivo + " "+ "renomeado para: " + nome_padrao)
