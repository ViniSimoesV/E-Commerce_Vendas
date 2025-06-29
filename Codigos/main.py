# sistema de Compra e venda de produtos
# Trabalho produzido para atividade de 1o periodo, Fundamentos de Software
# Sistema permite que o gerenciamento de Vendedor, Produto e Comprador.
# Autor: Vinícius Simões
# Inicio de produção: 27/06/2025
# Conclusão de produção: XX/06/2025

##### IMPORT #####
import os


##### METODOS #####

# exibir menu
def printMenu (tipoMenu):
    match tipoMenu:
        case "inicio":
            print ("*" * 11, " MENU ", "*" * 11)
            print ("*", " 1 - Realizar Compra"      , " " * 5, "*")
            print ("*", " 2 - Gerenciar Produtos"   , " " * 2, "*")
            print ("*", " 3 - Gerenciar Vendedores" , " " * 0, "*")
            print ("*", " 4 - Gerenciar Compradores", "*")
            print ("*", " 0 - SAIR", " " * 16, "*")
            print ("*" * 30)
        case "venda":
            print ("*" * 11, " VENDA ", "*" * 10)
            print ("*", " 1 - Ver produtos"     , " " * 8, "*")
            print ("*", " 2 - Chamar vendedores", " " * 3, "*")
            print ("*", " 3 - Comprar Produto"  , " " * 5, "*")
            print ("*", " 0 - SAIR", " " * 16, "*")
            print ("*" * 30)
        case "GProdutos":
            print ("*" * 8, " PRODUTOS ", "*" * 8)
            print ("*", " 1 - Adicionar Produto", " " * 1, "*")
            print ("*", " 2 - Listar Produtos"  , " " * 3, "*")
            print ("*", " 3 - Alterar Produtos" , " " * 2, "*")
            print ("*", " 4 - Remover Produto"  , " " * 3, "*")
            print ("*", " 0 - SAIR  ", " " * 12, "*")
            print ("*" * 28)
        case "GVendedores":
            print ("*" * 8, " Vendedores ", "*" * 8)
            print ("*", " 1 - Adicionar Vendedores", " *")
            print ("*", " 2 - Remover Vendedores"  , " " * 2 , "*")
            print ("*", " 3 - Listar Vendedores"   , " " * 3 , "*")
            print ("*", " 0 - SAIR  "              , " " * 14, "*")
            print ("*" * 30)
        case "GCompradores":
            print ("*" * 8, " COMPRADORES ", "*" * 8)
            print ("*", " 1 - Adicionar Compradores", " *")
            print ("*", " 2 - Remover Compradores"  , " " * 2 , "*")
            print ("*", " 3 - Listar Compradores"   , " " * 3 , "*")
            print ("*", " 0 - SAIR  "               , " " * 15, "*")
            print ("*" * 31)

## Gerenciar Produtos ##
# Atributos
codProduto = int
nomeProduto = str
qtdeEstoque = int
precoUnitario = float

# adicionar produto (Crud)
def criar_produto (codProduto, nomeProduto, qtdeEstoque, precoUnitario):
    with open ("produto.txt", "a") as f:
        f.write(f"{codProduto}, {nomeProduto}, {qtdeEstoque}, {precoUnitario}\n")
        print (f"Produto {nomeProduto} adicionado com sucesso.")

# ler produto (cRud)
def ler_produto ():
    try:
        with open ("produto.txt", "r") as f:
            for linha in f:
                codProduto, nomeProduto, qtdeEstoque, precoUnitario = linha.strip().split(", ")
                print (f"Codigo: {codProduto}, Nome: {nomeProduto}, Quantidade em estoque: {qtdeEstoque}, Preco Unitario: {precoUnitario}")
    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# atualizar produto (crUd)
def atualizar_produto (antigo_codProduto, novo_codProduto, novo_nomeProduto, novo_qtdeEstoque, novo_precoUnitario):
    try:
        with open ("produto.txt", "r") as f:
            linhas = f.readlines()
        
        with open ("produto.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                codProduto, nomeProduto, qtdeEstoque, precoUnitario = linha.strip().split(", ")
                if codProduto == antigo_codProduto:
                    f.write (f"{novo_codProduto}, {novo_nomeProduto}, {novo_qtdeEstoque}, {novo_precoUnitario}\n")
                    encontrado = True
                    print (f"Produto de codigo {antigo_codProduto} atualizado com sucesso para codigo {novo_codProduto}")
                else:
                    f.write(linha)
            if not encontrado:
                print (f"{antigo_codProduto} não encontrado.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# deletar produto (cruD)
def deletar_produto (codProduto):
    try:
        with open ("produto.txt", "r") as f:
            linhas = f.readlines()
        
        with open ("produto.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                if codProduto not in linha:
                    f.write (linha)
                else:
                    encontrado = True
                    print (f"O produto {codProduto} foi deletado.")
            if not encontrado:
                print (f"O produto {codProduto} não foi encontrado.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")



##### MAIN #####

def main():
    while True:
        try:
            # Variaveis
            entrada: int = 0;

            # Exibir menu
            print("\n")
            printMenu ("inicio")

            # navegar menu
            entrada = int (input ("Digite o menu desejado:  "))

            # direcionar para menus
            match entrada:
                case 1:
                    print (f"indo para {entrada}...")
                    printMenu("venda")
                case 2:
                    print (f"indo para {entrada}...")
                    printMenu("GProdutos")
                    # navegar menu
                    entrada = int (input ("Digite o menu desejado:  "))
                    match entrada:
                        case 1:
                            codProduto = input("Entrar codigo do produto (ex.: XXX):  ")
                            nomeProduto = input("Entrar nome do produto (ex.: Tomada):  ")
                            qtdeEstoque = input("Entrar quantidade do produto (ex.: XX):  ")
                            precoUnitario = input("Entrar preco do produto (ex.: XX.XX):  ")
                            criar_produto (codProduto, nomeProduto, qtdeEstoque, precoUnitario)
                        case 2:
                            ler_produto()
                        case 3:
                            antigo_codProduto = input ("Codigo do produto que deseja atualizar:  ")
                            novo_codProduto = input("Entrar codigo do produto (ex.: XXX):  ")
                            novo_nomeProduto = input("Entrar nome do produto (ex.: Tomada):  ")
                            novo_qtdeEstoque = input("Entrar quantidade do produto (ex.: XX):  ")
                            novo_precoUnitario = input("Entrar preco do produto (ex.: XX,XX):  ")
                            atualizar_produto (antigo_codProduto, novo_codProduto, novo_nomeProduto, novo_qtdeEstoque, novo_precoUnitario)
                        case 4:
                            codProduto = input ("Codigo do produto que deseja deletar:  ")
                            deletar_produto (codProduto)
                        case 0:
                            print ("Encerrar programa")
                        
                case 3:
                    print (f"indo para {entrada}...")
                    printMenu("GVendedores")
                case 4:
                    print (f"indo para {entrada}...")
                    printMenu("GCompradores")
                case 0:
                    print ("Encerrando sistema")
                    break
                case _:
                    entrada = int (input("Valor invalido, deve ser entre 0 a 4. Digite novamente:  "))
        except Exception as e:
            print(f"Erro no loop main: {e}")

if __name__ ==  "__main__":
    main()