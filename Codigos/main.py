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
cod_venda:int   # auto incremeto
controle_estoque: int
valor_compra_produto:float
valor_venda: float

# código de venda com auto incremento
def gerar_prox_cod_venda ():
    try:
        with open ("notaFiscal.txt", "r") as f:
            linhas = f.readlines()

            if not linhas:
                return 1
            
            ultimo_cod_venda = [int(linha.split(",")[0]) for linha in linhas]
            return max (ultimo_cod_venda) + 1
        
    except FileNotFoundError:
        print ("Arquivo não encontrado")

# calcualr valor do produto
def calc_preco_produto (preco_unitario, qtneDesejada_venda):
    # forçar para float
    float_preco_unitario = float (preco_unitario)
    float_qtneDesejada_venda = float (qtneDesejada_venda)
    valor_compra_produto = float_preco_unitario * float_qtneDesejada_venda
    return valor_compra_produto

# adicionar compra
def criar_venda (cpf_comprador_venda, cod_produto_venda, qtneDesejada_venda, cod_vendedor_venda):
    try:
        # recebe lista de produtos
        with open ("produto.txt", "r") as f:
            linha_p = f.readlines()

        # recebe lista de vendedores
        with open ("vendedor.txt", "r") as f:
            linha_v = f.readlines()

        # recebe lista de compradores
        with open ("comprador.txt", "r") as f:
            linha_c = f.readlines()

        # recebe código atual
        cod_venda_atual = gerar_prox_cod_venda()

        # cria venda
        with open ("notaFiscal.txt", "a") as f:
            # encontrar produto
            produto_encontrado = False
            for linha_p in f:
                cod_produto, nome_produto, qtde_estoque, preco_unitario = linha_p.strip().split(", ")
                if cod_produto_venda == cod_produto:
                    produto_encontrado = True
                    info_produto = cod_produto, nome_produto, qtde_estoque, preco_unitario
                if not produto_encontrado:
                    return "Produto não encontrado. Cancelando venda. \n"
            
            # encontrar vendedor
            vendedor_encontrado = False
            for linha_v in f:
                cod_vendedor, nomeVendedor, salarioFixo, comissao = linha_v.strip().split(",")
                if cod_vendedor_venda == cod_vendedor:
                    vendedor_encontrado = True
                    info_vendedor = cod_vendedor, nomeVendedor, salarioFixo, comissao
                if not vendedor_encontrado:
                    return "Produto não encontrado. Cancelando venda. \n"

            
            # verificar se comprador existe no banco
            comprador_encontrado = False
            for linha_c in f:
                cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado = linha_c.strip().split(",")
                if cpf_comprador_venda == cpf_comprador:
                    comprador_encontrado = True
                if not comprador_encontrado:
                    return "Comprador não encontrado. Cancelando venda. \n"
            
            # atualizar estoque

            # calcular valor total da compra do produto
            valor_venda = calc_preco_produto (preco_unitario, qtneDesejada_venda)

            # calcular frete

            # atribuir comissao

            # salvar 
            info_venda = info_produto + info_vendedor
            f.write (f"{cod_venda_atual}, {cpf_comprador_venda}, {nome_produto}, {cod_produto_venda}, {qtneDesejada_venda}, {preco_unitario}, {valor_venda}, {cod_vendedor_venda}\n")
            print (f"Venda: {cod_venda_atual}, do cliente: {cpf_comprador_venda} finalizada com sucesso. Valor total a pagar: {valor_venda + frete}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Ler vendedor (atendimento)
def ler_venda ( ):
    try:
        with open ("notaFiscal.txt", "r") as f:
            for linha in f:
                cod_venda_atual, cpf_comprador_venda, nome_produto, cod_produto_venda, qtneDesejada_venda, preco_unitario, valor_venda, cod_vendedor_venda = linha.strip().split(",")
                print (f"{cod_venda_atual}, {cpf_comprador_venda}, {nome_produto}, {cod_produto_venda}, {qtneDesejada_venda}, {preco_unitario}, {valor_venda}, {cod_vendedor_venda}.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")


## Gerenciar Produtos ##
# Atributos
cod_produto = int
nome_produto = str
qtde_estoque = int
preco_unitario:float = 10.0

# adicionar produto (Crud)
def criar_produto (cod_produto, nome_produto, qtde_estoque, preco_unitario):
    # Verifica se já existe
    with open ("produto.txt", "r") as f:
        linhas = f.readlines()
        encontrado = False
        for linha in linhas:
            if cod_produto in linha:
                encontrado = True
    # Já existe. Cancela.
    if encontrado == True:            
        print (f"Erro! Produto de codigo {cod_produto} já existe. Ação interrompida.")
    # Nao existe. Cria novo.
    else:
        with open ("produto.txt", "a") as f:
            f.write(f"{cod_produto}, {nome_produto}, {qtde_estoque}, {preco_unitario}\n")
            print (f"Produto {nome_produto} adicionado com sucesso.")

# ler produto (cRud)
def ler_produto ():
    try:
        with open ("produto.txt", "r") as f:
            for linha in f:
                cod_produto, nome_produto, qtde_estoque, preco_unitario = linha.strip().split(", ")
                print (f"Codigo: {cod_produto}, Nome: {nome_produto}, Quantidade em estoque: {qtde_estoque}, Preco Unitario: {preco_unitario}")
    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# atualizar produto (crUd)
def atualizar_produto (antigo_cod_produto, novo_cod_produto, novo_nome_produto, novo_qtde_estoque, novo_preco_unitario):
    try:
        with open ("produto.txt", "r") as f:
            linhas = f.readlines()
        
        with open ("produto.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                cod_produto, nome_produto, qtde_estoque, preco_unitario = linha.strip().split(", ")
                if cod_produto == antigo_cod_produto:
                    f.write (f"{novo_cod_produto}, {novo_nome_produto}, {novo_qtde_estoque}, {novo_preco_unitario}\n")
                    encontrado = True
                    print (f"Produto de codigo {antigo_cod_produto} atualizado com sucesso para codigo {novo_cod_produto}")
                else:
                    f.write(linha)
            if not encontrado:
                print (f"{antigo_cod_produto} não encontrado.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# deletar produto (cruD)
def deletar_produto (cod_produto):
    try:
        with open ("produto.txt", "r") as f:
            linhas = f.readlines()
        
        with open ("produto.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                if cod_produto not in linha:
                    f.write (linha)
                else:
                    encontrado = True
                    print (f"O produto {cod_produto} foi deletado.")
            if not encontrado:
                print (f"O produto {cod_produto} não foi encontrado.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")


## Gerenciar Vendedores ##
# Atributos
cod_vendedor: int 
nomeVendedor = str
salarioFixo:float = 10.0
comissao:float = 10.0

# autoincremente cod
def gerar_prox_cod_vendedor ():
    try:
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines()

            if not linhas:
                return 1
            
            ultimo_cod_vendedor = [int(linha.split(",")[0]) for linha in linhas]
            return max (ultimo_cod_vendedor) + 1
        
    except FileNotFoundError:
        print ("Arquivo não encontrado")

# Criar vendedor
# Cod com autoincremente
def criar_vendedor (nomeVendedor, salarioFixo):
    try:
        # recebe cod_vendedor atual
        cod_vendedor = gerar_prox_cod_vendedor()
        
        # escreve novo vendedor
        with open ("vendedor.txt", "a") as f:
            comissao = 0.00
            f.write (f"{cod_vendedor}, {nomeVendedor}, {salarioFixo}, {comissao}\n")
            print (f"O vendedor {nomeVendedor}, de codigo {cod_vendedor}, foi registrado com sucesso.")

    except FileNotFoundError:
        print ("Arquivo não encontrado")

# Ler vendedor
def ler_vendedor ( ):
    try:
        with open ("vendedor.txt", "r") as f:
            for linha in f:
                cod_vendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                floatSalarioFixo = float(salarioFixo)
                floatComissao = float(comissao)
                salarioMes = floatSalarioFixo + floatComissao
                print (f"{nomeVendedor}, cód:{cod_vendedor}. Salario fixo: {salarioFixo}, Comissão acumulada: {comissao}, Salario do mês: {salarioMes}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Ler vendedor (atendimento)
def ler_vendedor_atendendo ( ):
    try:
        with open ("vendedor.txt", "r") as f:
            for linha in f:
                cod_vendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                print (f"{nomeVendedor}, cód:{cod_vendedor}.")

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
                cod_vendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                if nomeVendedor == antigo_nomeVendedor:
                    f.write (f"{cod_vendedor}, {novo_nomeVendedor}, {novo_salarioFixo}, {comissao}\n")
                    encontrado = True
                    print (f"O(a) vendedor(a) {novo_nomeVendedor}, antigo {antigo_nomeVendedor}, foi atualizado com sucesso.")
                else:
                    f.write(linha)

                if not encontrado:
                    print (f"Vendedor(a) {antigo_nomeVendedor} não foi encontrado(a). Encerrando ação.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Deletar vendedor
def deletar_vendedor (apagar_cod_vendedor):
    try:
        # receber lista
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines( )

        # buscar codigo do vendedor a ser deletado
        with open ("vendedor.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                cod_vendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                if apagar_cod_vendedor == cod_vendedor:
                    encontrado = True
                    print(f"Vendedor(a) {nomeVendedor}, de código {apagar_cod_vendedor}, foi deletado(a).")
                else:
                    f.write(linha)
                
                if not encontrado:
                    print (f"O código {apagar_cod_vendedor}, não foi encontrado.")
    
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
                cod_vendedor, nomeVendedor, salarioFixo, comissao = linha.strip().split(",")
                
                # verificar se é o vendedor
                if nomeVendedor in linha:
                    encontrado = True
                    # valor de comissao anterior mais percentual de 3% do total da nova venda
                    comissao = comissao + (valor_venda * (3/100))
                    f.write (f"{cod_vendedor}, {nomeVendedor}, {salarioFixo}, {comissao}\n")
                else:
                    print (f"Vendedor(a) {nomeVendedor} não encontrado(a).")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")


## Gerenciar Comprador ##
# Atributos
cpf_comprador:str
email: str
nomeComprador: str
cep: str
rua: str
bairro: str
cidade: str
estado: str

# Criar comprador
def criar_comprador (cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado):
    try:
        # escreve novo comprador
        with open ("comprador.txt", "a") as f:
            f.write (f"{cpf_comprador}, {email}, {nomeComprador}, {cep}, {rua}, {bairro}, {cidade}, {estado}\n")
            print (f"O comprador {nomeComprador}, foi registrado com sucesso.")

    except FileNotFoundError:
        print ("Arquivo não encontrado")

# Ler comprador
def ler_comprador ( ):
    try:
        with open ("comprador.txt", "r") as f:
            for linha in f:
                cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado = linha.strip().split(",")
                print (f"Nome: {nomeComprador}, cpf_comprador: {cpf_comprador}, Contato: {email}, CEP:{cep}, Endereço: {rua}, {bairro}, {cidade}, {estado}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Atualizar comprador
def atualizar_comprador (antigo_cpf_comprador, novo_cpf_comprador, novo_email, novo_nomeComprador, novo_cep, novo_rua, novo_bairro, novo_cidade, novo_estado):
    try:
        # recebe comprador
        with open ("comprador.txt", "r") as f:
            linhas = f.readlines()
        
        # buscar vendedor
        with open ("comprador.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado = linha.strip().split(",")
                if cpf_comprador == antigo_cpf_comprador:
                    f.write (f"{novo_cpf_comprador}, {novo_email}, {novo_nomeComprador}, {novo_cep}, {novo_rua}, {novo_bairro}, {novo_cidade}, {novo_estado}\n")
                    encontrado = True
                    print (f"O(a) compador(a) {novo_nomeComprador}, foi atualizado com sucesso.")
                else:
                    f.write(linha)

                if not encontrado:
                    print (f"Vendedor(a) {antigo_cpf_comprador} não foi encontrado(a). Encerrando ação.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Deletar comprador
def deletar_comprador (apagar_cpf_comprador):
    try:
        # receber lista
        with open ("comprador.txt", "r") as f:
            linhas = f.readlines( )

        # buscar codigo do comprador a ser deletado
        with open ("comprador.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado = linha.strip().split(",")
                if apagar_cpf_comprador == cpf_comprador:
                    encontrado = True
                    print(f"Comprador(a) {nomeComprador}, de cpf_comprador {apagar_cpf_comprador}, foi deletado(a).")
                else:
                    f.write(linha)
                
                if not encontrado:
                    print (f"O código {apagar_cpf_comprador}, não foi encontrado.")
    
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
                        # Ler produtos
                        case 1:
                            ler_produto()

                        # Conhecer vendedores
                        case 2:
                            ler_vendedor_atendendo()

                        # Criar venda   
                        case 3:
                            cpf_comprador_venda = input ("Entrar com CPF do comprador:  ")
                            cod_produto_venda = input ("Código do produto desejado:  ")
                            qtneDesejada_venda = input ("Quantidade desejado do produto:  ")
                            cod_vendedor_venda = input ("Qual código do vendedor atendente:  ")
                            criar_venda (cpf_comprador_venda, cod_produto_venda, qtneDesejada_venda, cod_vendedor_venda)

                        # mostrar notas fiscais
                        case 4:
                            ler_venda()

                        # Voltar menu
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
                            cod_produto = input("Entrar codigo do produto (ex.: XXX):  ")
                            nome_produto = input("Entrar nome do produto (ex.: Tomada):  ")
                            qtde_estoque = input("Entrar quantidade do produto (ex.: XX):  ")
                            preco_unitario = input("Entrar preco do produto (ex.: XX.XX):  ")
                            criar_produto (cod_produto, nome_produto, qtde_estoque, preco_unitario)
                        # Ler produtos cadastrados
                        case 2:
                            ler_produto()
                        # Atualizar produto
                        case 3:
                            antigo_cod_produto = input ("Codigo do produto que deseja atualizar:  ")
                            novo_cod_produto = input("Entrar codigo do produto (ex.: XXX):  ")
                            novo_nome_produto = input("Entrar nome do produto (ex.: Tomada):  ")
                            novo_qtde_estoque = input("Entrar quantidade do produto (ex.: XX):  ")
                            novo_preco_unitario = input("Entrar preco do produto (ex.: XX,XX):  ")
                            atualizar_produto (antigo_cod_produto, novo_cod_produto, novo_nome_produto, novo_qtde_estoque, novo_preco_unitario)
                        # Deletar produto
                        case 4:
                            cod_produto = input ("Codigo do produto que deseja deletar:  ")
                            deletar_produto (cod_produto)
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
                            cod_vendedor = input("Entre com o código do vendedor:  ")
                            deletar_vendedor (cod_vendedor)

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
                            cpf_comprador = input ("Entre com o cpf_comprador:  ")
                            email = input ("Entre com o email:  ")
                            nomeComprador = input ("Entre com o nome:  ")
                            cep = input ("Entre com o CEP:  ")
                            rua = input ("Entre com o Rua:  ")
                            bairro = input ("Entre com o Bairro:  ")
                            cidade = input ("Entre com o Cidade:  ")
                            estado = input ("Entre com o Estado (Ex.: AA):  ")
                            criar_comprador (cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado)
                            
                        # Listar compradores
                        case 2:
                            ler_comprador()
                        
                        # Atualizar comprador
                        case 3:
                            antigo_cpf_comprador = input ("Entre com o cpf_comprador antigo:  ")
                            novo_cpf_comprador = input ("Entre com novo cpf_comprador:  ")
                            novo_email = input ("Entre com o email:  ")
                            novo_nomeComprador = input ("Entre com o nome:  ")
                            novo_cep = input ("Entre com o CEP:  ")
                            novo_rua = input ("Entre com o Rua:  ")
                            novo_bairro = input ("Entre com o Bairro:  ")
                            novo_cidade = input ("Entre com o Cidade:  ")
                            novo_estado = input ("Entre com o Estado (Ex.: AA):  ")
                            atualizar_comprador(antigo_cpf_comprador, novo_cpf_comprador, novo_email, novo_nomeComprador, novo_cep, novo_rua, novo_bairro, novo_cidade, novo_estado)
                        
                        # Deletar comprador
                        case 4:
                            apagar_cpf_comprador = input ("Identifique quem deseja apagar. Qual o cpf_comprador?  ")
                            deletar_comprador (apagar_cpf_comprador)

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