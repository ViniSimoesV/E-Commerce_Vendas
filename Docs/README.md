# Documentação do Projeto


## Diagrama de Classe
Diagrama do sistema, apresentando atributos e seus tipos, métodos com seus parametros e retornos.
![Backlog Sprint 1](img/DER-Vendas-Ecommerce.drawio.png "DER ")


## Apresentação
Este é um projeto feito por Vinícius Simões como entregavel para uma atividade da disciplina Fundamentos de Software do 1° período do curso.
O projeto, feito na linguagem Python, é um E-commerce de venda e compra de produtos, contando com função de contas (vendedor e cliente), permitindo que o vendedor gerencie produtos em estoque e que clientes possam vizualizar os produtos disponiveis para compra e visualizar sua nota fiscal após finalizar a compra.


## Backlog do produto
- Dia (27/06) - Backlog Sprint 1, Organização do backlog.
![Backlog Sprint 1](img/backlog1.png "Divisão de Tarefas")

- Dia (28/06) - Sprint 1 finalizada, DER criado e já no GitHub. O DER possui os métodos e atributos já definidos para implementação do programa.
- Início da Sprint 2, implementação do código em python. Será apenas um arquivo que conterá todas funções e aplicações com métodos documentados.
![Backlog Sprint 1 & 2](img/backlog2.png "Divisão de Implementação")

- Dia (29/06) - Backlog Sprint 2, concluida. Ajustes ainda serão necessários no código.
- Na Sprint 3, desenho de casos de testes, documentados em arquivo "testes.txt" e aqui neste README.md. Foram levantados ao menos dois cenários para opção do no menu do sistema.
![Backlog Sprint 1](img/backlog3.png "Divisão de Tarefas")

- Dia (30/06) - Backlog Sprint 3, concluida.
- Na Sprint 4, os casos de testes foram executados e os ajustes no código foram implementados.
- Adição de novos casos de testes especiais ao arquivo de testes.
![Backlog Sprint 1](img/backlog4.png "Divisão de Tarefas")

- Dia (01/07) - Projeto concluido. Corrigida documentação do projeto.
![Backlog Sprint 1](img/backlog5.png "Divisão de Tarefas")

## Lista de assinatura das funções e parâmetros

1. def printMenu (tipoMenu)
   - função retorna print dependendo do inteiro recebido, sendo os menus de cada operação (inicio, vendas, produtos, vendedores e compradores).
   
2. def gerar_prox_cod_venda ()
   - Função retorna qual será o próximo código de vendas.
   
3. def calc_preco_produto (preco_unitario, qtneDesejada_venda)
   - Função retorna calculo do total que será cobrado pela quantidade desejado de um determinado produto.

4. def adicionar_ao_carrinho (cpf_comprador_venda, cod_produto_venda, qtneDesejada_venda, cod_vendedor_venda)
   - Função monta uma lista de produtos em "carrinho". Testa cada parâmetro para saber se existe no sistema, caso não existe, não insere à lista.

6. def finalizar_compra ()
   - Função escreve todos produtos armazenados na lista "carrinho" para um arquivo "notaFiscal.txt" que armazena todas compras realizadas. Essa função também chama métodos para atualizar o estoque do produto comprado e atribuir comissão ao vendedor que fechou a compra.

7. def ver_carrinho():
   - Função mostra todos produtos presentes no carrinho.

8. def ler_venda ( ):
   - Função mostra toda a nota fiscal, presentes no arquivo "notaFiscal.txt"

9. def criar_produto (cod_produto, nome_produto, qtde_estoque, preco_unitario):
   - Função escreve produto em arquivo "produto.txt".

10. def ler_produto ():
   - Função mostra todos os produtos escritos no arquivo "produto.txt"

11. def atualizar_produto (antigo_cod_produto, novo_cod_produto, novo_nome_produto, novo_qtde_estoque, novo_preco_unitario):
   - Função busca produto por seu código e atualiza todas suas entredas, sobreescrevendo sua linha original no arquivo "produtos.txt".

12. def deletar_produto (cod_produto_para_deletar):
   - Função busca produto por seu código e apaga sua linha quando encontrado.

13. def atualizar_estoque (cod_produto_escolhido, qtneDesejada_venda):
   - Função para atualizar o estoque quando a compra do produto é confirmada. Busca o produto pelo código no arquivo e reescreve com seu novo valor de estoque.

14. def gerar_prox_cod_vendedor ():
   - Função identifica o próximo código de vendedor e retorna.

15. def criar_vendedor (nomeVendedor, salarioFixo):
   - Função escreve nova linha em arquivo "vendedor.txt", escrevendo seus parâmetros de entrada, sua comissão inicial em zero e o seu salário total (soma do salario fixo mais as commissões).

16. def ler_vendedor ():
   - Função mostra todos os vendedores escritos no "vendedores.txt"

17. def ler_vendedor_atendendo ():
   - Função específica para chamada no momento de venda para mostrar apenas o nome e código do vendedor.

18. def atualizar_vendedor (antigo_nomeVendedor, novo_nomeVendedor, novo_salarioFixo):
   - Função busca vendedor por seu nome e reescreve com novas entradas caso seja encontrado no arquivo "vendedor.txt"

19. def deletar_vendedor (apagar_cod_vendedor):
   - Função busca vendedor por seu código e apaga seu linha de dados no arquivo "vendedor.txt" caso encontre.

20. def adicionar_comissao_vendedor (nomeVendedor_atendendo, valor_venda):
   - Função busca vendedor por seu nome e atualiza o valor da sua comissão, calculando 3% do valor total da compra

21. def criar_comprador (cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado):
   - Função para escrever novo comprador no arquivo "comprador.txt".

23. def ler_comprador ():
   - Função mostra todos os compradores registrados no arquivo "comprador.txt".

24. def atualizar_comprador (antigo_cpf_comprador, novo_cpf_comprador, novo_email, novo_nomeComprador, novo_cep, novo_rua, novo_bairro, novo_cidade, novo_estado):
   - Função que busca comprador por seu CPF e caso encontre, reescreve seus dados no arquivo "comprador.txt".

25. def deletar_comprador (apagar_cpf_comprador):
   - Função que busca comprador por seu CPF e caso encontre apaga sua linha.

27. def main():
   - Função que executa o sistema, chamando os métodos conforme entrado do usuário.


## Testes
### Casos de Testes do Software:
Os casos de teste englobam todo o código, uma vez que as funções devem receber parâmetros
que podem estar dentro de outras funções ou do código principal.

#### Caso de teste 1: Gerar próximo cód de venda

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |
| Arquivo notaFiscal.txt vazio| Início da contagem                | "1". Caso arquivo não encontrado, sinalizar. | Arquivo notaFiscal.txt com linhas mal formatadas | "1"                         |
| Arquivo notaFiscal.txt com 3 linhas| Continuição da contagem    | "4"                                          | Arquivo notaFiscal.txt com linhas mal formatadas | "4"                         |


#### Caso de teste 2: Calcular preço total do produto

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |
| Valor unitário do produto = 2.00 e quantidade comprada = 2. | Produto existente, estoque disponivel |  4.00    | Produto não existe ou sem estoque.               | 4.00                        |
| Valor unitário do produto = 2.00 e quantidade comprada = -2.| Produto existente, estoque disponivel |  Erro, valor não poder ser negativo. | Produto não existe ou sem estoque. | Erro...       |


#### Caso de teste 3: Adicionar ao carrinho

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |
| CPF, CodProduto, Qtde, CodVendedor | Arquivos produto.txt, vendedor.txt, comprador.txt possuem os registro | Produto adicionado ao carrinho | Ao menos um dos arquivos não possui a entrada| Produto adicionado... |
| CPF, CodProduto, Qtde, -CodVendedor | Arquivos produto.txt, vendedor.txt, comprador.txt possuem os registro | Vendedor não encontrado, cancela pedido | Ao menos um dos arquivos não possui a entrada| Pedido cancelado... |


#### Caso de teste 4: Finalizar compra

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |
| Carrinho vazio              | Carrinho existes                  | O carrinho está vazio. Adicione produtos!    | Não criou lista carrinho                         | O carrinho está vazio...    |
| Carrinho com itens          | Carrinho existes        | Produtos XX comprados com sucesso. Nota fiscal gerada    | Não criou lista carrinho             | Produtos comprados e nota fiscal gerada    |


#### Caso de teste 5: XX

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |


#### Caso de teste 6: XX

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |


#### Caso de teste 7: XX

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |


#### Caso de teste 8: XX

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |


#### Caso de teste 9: XX

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |


#### Caso de teste 10: XX

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |


#### Caso de teste X: XX

|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |

#### Rélatorio de Execução de Teste

|  **Teste 1 - Gerar próximo cód de venda**   |
|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |
| Arquivo notaFiscal.txt vazio| Início da contagem                | "1". Caso arquivo não encontrado, sinalizar. | Arquivo notaFiscal.txt com linhas mal formatadas | "1"                         |

|    **Entradas**       |      **Resultado**      |        **Aprovado?**        |
|       :---:           |        :---:            |            :---:            |
|     Arquivo vazio     |            1            |             sim             |
|  Arquivo com 1 linhas |            2            |             sim             |
|  Arquivo com 2 linhas |            3            |             sim             |
|  Arquivo com 3 linhas |            4            |             sim             |


|  **Teste 2 - Calcular preço total do produto**   |
|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |
| Valor unitário do produto = 2.00 e quantidade comprada = 2. | Produto existente, estoque disponivel |  4.00    | Produto não existe ou sem estoque.               | 4.00                        |

|     **Entradas**        |      **Resultado**      |        **Aprovado?**        |
|        :---:            |        :---:            |            :---:            |
| valor = 5.00, qtde = 1  |          5.00           |             sim             |
| valor = 10.00, qtde = 2 |          20.00          |             sim             |
| valor = 5.00, qtde = -1 |  Erro, valor negativo   |             sim             |
| valor = -5.00, qtde = 1 |  Erro, valor negativo   |             sim             |
| valor = 5.00, qtde = 0  |  Erro, valor negativo   |             sim             |


|  **Teste 3 - Adicionar ao carrinho**   |
|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |
| 10010010010, 001, 3, 4 | Arquivos produto.txt, vendedor.txt, comprador.txt possuem os registro | Produto adicionado ao carrinho | Ao menos um dos arquivos não possui a entrada| Produto adicionado... |

|     **Entradas**        |      **Resultado**           |        **Aprovado?**        |
|        :---:            |        :---:                 |            :---:            |
| 10010010010, 001, 3, 4  | Adicionado ao carrinho       |             sim             |
| 20020020020, 001, -4, 1 | Erro, quantidade negativa    |             sim             |
| 10010010010, 007, 1, -2 | Erro, vendedor não existe    |             sim             |
| 10010010010, -001, 3, 9 | Erro, produto não encontrado |             sim             |




|  **Teste 4 - Fechar ao carrinho**   |
|        **Entradas**         |        **Classes Válidas**        |        **Resultado Esperado**                |        **Classes Inválidas**                     |        **Resultado**        |
| :---:                       | :---:                             | :---:                                        | :---:                                            | :---:                       |
| Carrinho vazio              | Carrinho existes                  | O carrinho está vazio. Adicione produtos!    | Não criou lista carrinho                         | O carrinho está vazio...    |

|     **Entradas**        |      **Resultado**                 |        **Aprovado?**        |
|        :---:            |        :---:                       |            :---:            |
| Carrinho vazio          | Carrinho vazio, adicione produtos! |             sim             |
| Carrinho com 1 produto  | Produto X comprado, valor Y        |             sim             |
| Carrinho com 2 produto  | Produto X comprado, valor Y; Produto Z comprado, valor W | sim   |



## Código fonte com testes automatizados
