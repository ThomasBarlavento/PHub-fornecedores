# Dicionário de fornecedores disponíveis por categorias
fornecedores = {
    1: {
        101: "Casa do Salgado",
        102: "Delícias da Vila",
        103: "Salgadinhos da Vovó",
        104: "Sabor & Cia",
        105: "Salgados Express"
    },
    2: {
        201: "Adega do Amigo",
        202: "Bebidas e Festas",
        203: "Casa das Bebidas",
        204: "Empório das Bebidas"
    },
    3: {
        301: "Encantos do Açúcar",
        302: "Delícias da Vovó",
        303: "Doces Encantados",
        304: "Doce Sabor"
    },
    4: {
        401: "Brinquedos & Alegria",
        402: "Jump & Fun",
        403: "Diversão & Cia",
        404: "Cama Elástica & Diversão"
    },
    5: {
        501: "Som & Luz Eventos",
        502: "Karaokê Show",
        503: "Bandas & Festas",
        504: "Karaokê e Alegria"
    }
}

# Função para exibir fornecedores disponíveis por categoria
def exibir_fornecedores_por_categoria(categoria):
    print("Fornecedores disponíveis:")
    for id_fornecedor, nome_fornecedor in fornecedores[categoria].items():
        print(f"ID: {id_fornecedor} - Fornecedor: {nome_fornecedor}")

# Função para selecionar um fornecedor de uma categoria específica
def selecionar_fornecedor(categoria):
    exibir_fornecedores_por_categoria(categoria)
    while True:
        try:
            selecao_fornecedor = int(input("Digite o ID do fornecedor que deseja selecionar: "))
            if selecao_fornecedor in fornecedores[categoria]:
                print(f"Fornecedor '{fornecedores[categoria][selecao_fornecedor]}' (ID: {selecao_fornecedor}) selecionado com sucesso!")
                return selecao_fornecedor
            else:
                print("ID do fornecedor inválido. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

# Função para alterar a seleção do fornecedor
def alterar_fornecedor(categoria, selecao_atual):
    print(f"Fornecedor atual: {fornecedores[categoria][selecao_atual]} (ID: {selecao_atual})")
    print("Deseja alterar o fornecedor? (s/n)")
    alterar = input().strip().lower()
    if alterar == 's':
        return selecionar_fornecedor(categoria)
    else:
        print("Fornecedor mantido.")
        return selecao_atual

# Exemplo de uso do sistema
def main():
    print("Bem-vindo ao sistema de seleção de fornecedores para eventos!")
    
    # Selecionar fornecedores por categoria
    categorias = {
        1: "Fornecedores de Salgados",
        2: "Fornecedores de Bebidas",
        3: "Fornecedores de Bolos e Doces",
        4: "Entretenimento Infantil",
        5: "Banda ou Som"
    }

    selecao_fornecedores = {}

    for categoria_id, categoria_nome in categorias.items():
        print(f"\nCategoria: {categoria_nome}")
        fornecedor_selecionado = selecionar_fornecedor(categoria_id)
        selecao_fornecedores[categoria_id] = fornecedor_selecionado

        while True:
            print("\nDeseja alterar a seleção do fornecedor para esta categoria? (s/n)")
            resposta = input().strip().lower()
            if resposta == 's':
                fornecedor_selecionado = alterar_fornecedor(categoria_id, selecao_fornecedores[categoria_id])
                selecao_fornecedores[categoria_id] = fornecedor_selecionado
            elif resposta == 'n':
                break
            else:
                print("Opção inválida. Por favor, responda com 's' para sim ou 'n' para não.")
    
    print("\nSeleção final de fornecedores:")
    for categoria_id, fornecedor_id in selecao_fornecedores.items():
        print(f"{categorias[categoria_id]}: {fornecedores[categoria_id][fornecedor_id]} (ID: {fornecedor_id})")

# Executa o programa
if __name__ == "__main__":
    main()
