# funcionalidade
@Preencher_Carrinho
Feature: Preencher Carrinho
    
    # cenario da funcionalidade
    @Preencher_com_algo_eletronico
    Scenario: Preencher com algo eletronico
        # pre requisito para iniciar o cenario
        Given Estou na tela de pesquisa de eletronicos
        # passo intermediario
        When Clico em um item
        |Item|
        |TV|
        # resultado
        Then Vou para a pagina do item
        # passo adicional
        And Adiciono no carrinho
        # resultado
        Then O item vai para o carrinho