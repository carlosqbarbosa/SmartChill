import datetime
from datetime import datetime, timedelta

estoque = []


def verificar_estoque():
    return print(estoque)


def adicionar_item(nome, quantidade, preco, data_validade):
    item = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "data_validade": data_validade,
    }
    estoque.append(item)


def verificar_datas_validade():
    hoje = datetime.now().date()
    for item in estoque:
        data_validade_dt = datetime.strptime(item["data_validade"], "%Y-%m-%d").date()
        if data_validade_dt <= hoje:
            print(f"{item['nome']} está vencido!")
        elif data_validade_dt <= hoje + timedelta(days=2):
            print(f"{item['nome']} vai vencer em breve!")
        else:
            print(f"{item['nome']} ainda é válido.")


def escanear_qrcode(id_geladeira):
    geladeira_selecionada = id_geladeira
    print(f"A Geladeira {geladeira_selecionada} foi aberta!")


def adicionar_quantidade(produto, quantidade):
    """Adiciona uma quantidade ao produto existente no estoque."""
    for item in estoque:
        if produto == item["nome"]:
            if quantidade <= item["quantidade"]:
                item["quantidade"] -= quantidade
                return f"Quantidade de {produto} selecionada: {quantidade}."
            else:
                return f"A quantidade selecionada excede o estoque disponível."
    return f"O produto {produto} não está no estoque."


def ajustar_temperatura(temp_atual, temp_alvo):
    if temp_atual < temp_alvo:
        print(f"Temperatura atual: {temp_atual}º. Aumentando a temperatura da geladeira para {temp_alvo}º.")
    elif temp_atual > temp_alvo:
        print(f"Temperatura atual: {temp_atual}º. Diminuindo a temperatura da geladeira para {temp_alvo}º.")
    else:
        print("A temperatura da geladeira está ótima.")


def verificar_status_camera(camera_id, id_geladeira):
    print(f"Câmera {camera_id} da geladeira {id_geladeira} está funcionando devidamente.")


def escolher_produto(nome_produto):
    produto_selecionado = nome_produto
    print(f"O produto {produto_selecionado} foi selecionado!")


def escolher_forma_pagamento(forma_pagamento):
    print(f"Forma de pagamento selecionada: {forma_pagamento}")


def pagamento():
    escolher_forma_pagamento("Cartão de Crédito")
    for item in estoque:
        print(f"Pagamento com o valor de {item['preco']}R$ referente ao produto {item['nome']} realizado com sucesso!")


    # Testando as funções
    adicionar_item("Coca-Cola", 12, 5, "2024-12-31")
    verificar_datas_validade()
    escanear_qrcode("01")
    ajustar_temperatura(25, 20)
    verificar_status_camera("01", "01")
    escolher_produto("Coca-Cola")
    print(adicionar_quantidade("Coca-Cola", 5))
    pagamento()
