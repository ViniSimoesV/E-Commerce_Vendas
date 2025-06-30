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
        case "GVenda":
            print ("*" * 11, " VENDA ", "*" * 10)
            print ("*", " 1 - Ver Produtos"        , " " * 8, "*")
            print ("*", " 2 - Chamar Vendedor"     , " " * 5, "*")
            print ("*", " 3 - Colocar no Carrinho" , " " * 1, "*")
            print ("*", " 4 - Emitir Notas Fiscais", " " * 0, "*")
            print ("*", " 0 - VOLTAR", " " * 14, "*")
            print ("*" * 30)
        case "GProdutos":
            print ("*" * 8, " PRODUTOS ", "*" * 8)
            print ("*", " 1 - Adicionar Produto", " " * 1, "*")
            print ("*", " 2 - Listar Produtos"  , " " * 3, "*")
            print ("*", " 3 - Alterar Produtos" , " " * 2, "*")
            print ("*", " 4 - Remover Produto"  , " " * 3, "*")
            print ("*", " 0 - VOLTAR  ", " " * 10, "*")
            print ("*" * 28)
        case "GVendedores":
            print ("*" * 8, " Vendedores ", "*" * 8)
            print ("*", " 1 - Adicionar Vendedores", " *")
            print ("*", " 2 - Listar Vendedores"   , " " * 3 , "*")
            print ("*", " 3 - Atualizar Vendedores", " " * 0 , "*")
            print ("*", " 4 - Remover Vendedores"  , " " * 2 , "*")
            print ("*", " 0 - VOLTAR  "            , " " * 12, "*")
            print ("*" * 30)
        case "GCompradores":
            print ("*" * 8, " COMPRADORES ", "*" * 8)
            print ("*", " 1 - Adicionar Compradores", " *")
            print ("*", " 2 - Listar Compradores"   , " " * 3 , "*")
            print ("*", " 3 - Atualizar Compradores", " " * 0 , "*")
            print ("*", " 4 - Remover Compradores"  , " " * 2 , "*")
            print ("*", " 0 - VOLTAR  "             , " " * 13, "*")
            print ("*" * 31)

## Gerenciar Vendas ##
# Atributos
codVenda:int   # auto incremeto
cpf_comprador: str
cod_vendedor: int
cod_produto: int

## Gerenciar Produtos ##
# Atributos
codProduto = int
nomeProduto = str
qtdeEstoque = int
precoUnitario:float = 10.0

# adicionar produto (Crud)
def criar_produto (codProduto, nomeProduto, qtdeEstoque, precoUnitario):
    # Verifica se já existe
    with open ("produto.txt", "r") as f:
        linhas = f.readlines()
        encontrado = False
        for linha in linhas:
            if codProduto in linha:
                encontrado = True
    # Já existe. Cancela.
    if encontrado == True:            
        print (f"Erro! Produto de codigo {codProduto} já existe. Ação interrompida.")
    # Nao existe. Cria novo.
    else:
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


## Gerenciar Vendedores ##
# Atributos
codVendedor: int 
nomeVendedor = str
salarioFixo:float = 10.0
comissao:float = 10.0

# autoincremente cod
def gerar_prox_codVendedor ():
    try:
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines()

            if not linhas:
                return 1
            
            ultimo_codVendedor = [int(linha.split(",")[0]) for linha in linhas]
            return max (ultimo_codVendedor) + 1
        
    except FileNotFoundError:
        print ("Arquivo não encontrado")

# Criar vendedor
# Cod com autoincremente
def criar_vendedor (nomeVendedor, salarioFixo):
    try:
        # recebe codVendedor atual
        codVendedor = gerar_prox_codVendedor()
        
        # escreve novo vendedor
        with open ("vendedor.txt", "a") as f:
            comissao = 0.00
            f.write (f"{codVendedor}, {nomeVendedor}, {salarioFixo}, {comissao}\n")
            print (f"O vendedor {nomeVendedor}, de codigo {codVendedor}, foi registrado com sucesso.")

    except FileNotFoundError:
        print ("Arquivo não encontrado")

# Ler vendedor
def ler_vendedor ( ):
    try:
        with open ("vendedor.txt", "r") as f:
            for linha in f:
                codVendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                salarioMes = salarioFixo + comissao
                print (f"{nomeVendedor}, cód:{codVendedor}. Salario fixo: {salarioFixo}, Comissão acumulada: {comissao}, Salario do mês: {salarioMes}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Atualizar vendedor
def atualizar_vendedor (antigo_nomeVendedor, novo_nomeVendedor, novo_salarioFixo):
    try:
        # recebe vendedor
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines()
        
        # buscar vendedor
        with open ("vendedor.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                codVendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                if nomeVendedor == antigo_nomeVendedor:
                    f.write (f"{codVendedor}, {novo_nomeVendedor}, {novo_salarioFixo}, {comissao}\n")
                    encontrado = True
                    print (f"O(a) vendedor(a) {novo_nomeVendedor}, antigo {antigo_nomeVendedor}, foi atualizado com sucesso.")
                else:
                    f.write(linha)

                if not encontrado:
                    print (f"Vendedor(a) {antigo_nomeVendedor} não foi encontrado(a). Encerrando ação.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Deletar vendedor
def deletar_vendedor (apagar_codVendedor):
    try:
        # receber lista
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines( )

        # buscar codigo do vendedor a ser deletado
        with open ("vendedor.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                codVendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                if apagar_codVendedor == codVendedor:
                    encontrado = True
                    print(f"Vendedor(a) {nomeVendedor}, de código {apagar_codVendedor}, foi deletado(a).")
                else:
                    f.write(linha)
                
                if not encontrado:
                    print (f"O código {apagar_codVendedor}, não foi encontrado.")
    
    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Receber comissão
def adicionar_comissao_vendedor (nomeVendedor, valor_venda):
    try:
        # receber vendedores
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines( )
        
        # buscar vendedor e aplicar comissao quando encontrar
        with open ("vendedor.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                codVendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                
                # verificar se é o vendedor
                if nomeVendedor in linha:
                    encontrado = True
                    # valor de comissao anterior mais percentual de 3% do total da nova venda
                    comissao = comissao + (valor_venda * (3/100))
                    f.write (f"{codVendedor}, {nomeVendedor}, {salarioFixo}, {comissao}\n")
                else:
                    print (f"Vendedor(a) {nomeVendedor} não encontrado(a).")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")


## Gerenciar Comprador ##
# Atributos
cpf:str
email: str
nomeComprador: str
cep: str
rua: str
bairro: str
cidade: str
estado: str

# Criar comprador
def criar_comprador (cpf, email, nomeComprador, cep, rua, bairro, cidade, estado):
    try:
        # escreve novo comprador
        with open ("comprador.txt", "a") as f:
            f.write (f"{cpf}, {email}, {nomeComprador}, {cep}, {rua}, {bairro}, {cidade}, {estado}\n")
            print (f"O comprador {nomeComprador}, foi registrado com sucesso.")

    except FileNotFoundError:
        print ("Arquivo não encontrado")

# Ler comprador
def ler_comprador ( ):
    try:
        with open ("comprador.txt", "r") as f:
            for linha in f:
                cpf, email, nomeComprador, cep, rua, bairro, cidade, estado = linha.strip().split(",")
                print (f"Nome: {nomeComprador}, CPF: {cpf}, Contato: {email}, CEP:{cep}, Endereço: {rua}, {bairro}, {cidade}, {estado}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Atualizar comprador
def atualizar_comprador (antigo_cpf, novo_cpf, novo_email, novo_nomeComprador, novo_cep, novo_rua, novo_bairro, novo_cidade, novo_estado):
    try:
        # recebe comprador
        with open ("comprador.txt", "r") as f:
            linhas = f.readlines()
        
        # buscar vendedor
        with open ("comprador.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                cpf, email, nomeComprador, cep, rua, bairro, cidade, estado = linha.strip().split(",")
                if cpf == antigo_cpf:
                    f.write (f"{novo_cpf}, {novo_email}, {novo_nomeComprador}, {novo_cep}, {novo_rua}, {novo_bairro}, {novo_cidade}, {novo_estado}\n")
                    encontrado = True
                    print (f"O(a) compador(a) {novo_nomeComprador}, foi atualizado com sucesso.")
                else:
                    f.write(linha)

                if not encontrado:
                    print (f"Vendedor(a) {antigo_cpf} não foi encontrado(a). Encerrando ação.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Deletar comprador
def deletar_comprador (apagar_cpf):
    try:
        # receber lista
        with open ("comprador.txt", "r") as f:
            linhas = f.readlines( )

        # buscar codigo do comprador a ser deletado
        with open ("comprador.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                cpf, email, nomeComprador, cep, rua, bairro, cidade, estado = linha.strip().split(",")
                if apagar_cpf == cpf:
                    encontrado = True
                    print(f"Comprador(a) {nomeComprador}, de CPF {apagar_cpf}, foi deletado(a).")
                else:
                    f.write(linha)
                
                if not encontrado:
                    print (f"O código {apagar_cpf}, não foi encontrado.")
    
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

            # Navegar para menus
            match entrada:
                # Gerenciar Venda FAZER!!
                case 1:
                    print ("\n")
                    printMenu("GVenda")
                    entrada = int (input("Digite o menu desejado:  "))
                    match entrada:
                        case 1:
                            print ("vendendo...")
                        case 2:
                            print ("negocando...")
                        case 3:
                            print ("bagulhando...")
                        case 0:
                            print ("Voltando...\n")

                # Gerenciar Produtos
                case 2:
                    print ("\n")
                    printMenu("GProdutos")
                    
                    # navegar menu
                    entrada = int (input ("Digite o menu desejado:  "))
                    match entrada:
                        # Criar produto
                        case 1:
                            codProduto = input("Entrar codigo do produto (ex.: XXX):  ")
                            nomeProduto = input("Entrar nome do produto (ex.: Tomada):  ")
                            qtdeEstoque = input("Entrar quantidade do produto (ex.: XX):  ")
                            precoUnitario = input("Entrar preco do produto (ex.: XX.XX):  ")
                            criar_produto (codProduto, nomeProduto, qtdeEstoque, precoUnitario)
                        # Ler produtos cadastrados
                        case 2:
                            ler_produto()
                        # Atualizar produto
                        case 3:
                            antigo_codProduto = input ("Codigo do produto que deseja atualizar:  ")
                            novo_codProduto = input("Entrar codigo do produto (ex.: XXX):  ")
                            novo_nomeProduto = input("Entrar nome do produto (ex.: Tomada):  ")
                            novo_qtdeEstoque = input("Entrar quantidade do produto (ex.: XX):  ")
                            novo_precoUnitario = input("Entrar preco do produto (ex.: XX,XX):  ")
                            atualizar_produto (antigo_codProduto, novo_codProduto, novo_nomeProduto, novo_qtdeEstoque, novo_precoUnitario)
                        # Deletar produto
                        case 4:
                            codProduto = input ("Codigo do produto que deseja deletar:  ")
                            deletar_produto (codProduto)
                        # Retroceder menu
                        case 0:
                            print ("Encerrar programa")
                
                # Gerenciar Vendedores
                case 3:
                    print ("\n")
                    printMenu("GVendedores")

                    # nevegar menu
                    entrada = int (input("Digite o menu desejado:  "))
                    match entrada:
                        # criar vendedor
                        case 1:
                            nomeVendedor = input ("Entrar com o nome do(a) vendedor(a) (Ex.: Caio):  ")
                            salarioFixo = input ("Entrar com o salario fixo do(a) vendedor(a) (Ex.: 1500.00):  ")
                            criar_vendedor (nomeVendedor, salarioFixo)

                        # listar vendedores
                        case 2:
                            ler_vendedor()

                        # Atualizar vendedor
                        case 3:
                            antigo_nomeVendedor = input ("Entrar com o antigo nome do(a) vendedor(a) (Ex.: Caio):  ")
                            novo_nomeVendedor = input ("Entrar com novo nome do(a) vendedor(a) (Ex.: Pedro):  ")
                            novo_salarioFixo = input ("Entrar com novo salario fixo do(a) vendedor(a) (Ex.: 2500.00):  ")
                            atualizar_vendedor (antigo_nomeVendedor, novo_nomeVendedor, novo_salarioFixo)

                        # Deletar vendedor
                        case 4:
                            codVendedor = input("Entre com o código do vendedor:  ")
                            deletar_vendedor (codVendedor)

                        case 0:
                            print ("Retornando ao menu inicial.")

                # Gerenciar Compradores
                case 4:
                    print ("\n")
                    printMenu("GCompradores")

                    # navegar menu
                    entrada = int (input("Digite o menu desejado:  "))
                    match entrada:
                        # Criar comprador
                        case 1:
                            cpf = input ("Entre com o CPF:  ")
                            email = input ("Entre com o email:  ")
                            nomeComprador = input ("Entre com o nome:  ")
                            cep = input ("Entre com o CEP:  ")
                            rua = input ("Entre com o Rua:  ")
                            bairro = input ("Entre com o Bairro:  ")
                            cidade = input ("Entre com o Cidade:  ")
                            estado = input ("Entre com o Estado (Ex.: AA):  ")
                            criar_comprador (cpf, email, nomeComprador, cep, rua, bairro, cidade, estado)
                            
                        # Listar compradores
                        case 2:
                            ler_comprador()
                        
                        # Atualizar comprador
                        case 3:
                            antigo_cpf = input ("Entre com o CPF antigo:  ")
                            novo_cpf = input ("Entre com novo CPF:  ")
                            novo_email = input ("Entre com o email:  ")
                            novo_nomeComprador = input ("Entre com o nome:  ")
                            novo_cep = input ("Entre com o CEP:  ")
                            novo_rua = input ("Entre com o Rua:  ")
                            novo_bairro = input ("Entre com o Bairro:  ")
                            novo_cidade = input ("Entre com o Cidade:  ")
                            novo_estado = input ("Entre com o Estado (Ex.: AA):  ")
                            atualizar_comprador(antigo_cpf, novo_cpf, novo_email, novo_nomeComprador, novo_cep, novo_rua, novo_bairro, novo_cidade, novo_estado)
                        
                        # Deletar comprador
                        case 4:
                            apagar_cpf = input ("Identifique quem deseja apagar. Qual o CPF?  ")
                            deletar_comprador (apagar_cpf)

                        # Voltar menu
                        case 0:
                            print ("Vontando para o inicio... \n")

                # Encerrar sistema
                case 0:
                    print ("\n")
                    print ("Encerrando sistema.")
                    break

                # lidar com entrada inesperada
                case _:
                    entrada = int (input("Valor invalido, deve ser entre 0 a 4. Digite novamente:  "))
        
        except Exception as e:
            print(f"Erro no loop main: {e}")

if __name__ ==  "__main__":
    main()