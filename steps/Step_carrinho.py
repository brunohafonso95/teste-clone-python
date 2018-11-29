@given(u'Estou na tela de pesquisa de eletronicos')
def step_impl(context):
    context.home.ir_home()
    context.home.selecionar_item_menu(tipo='ELETRONICOS')

@when(u'Clico em um item')
def step_impl(context):
    pass


@then(u'Vou para a pagina do item')
def step_impl(context):
    pass


@then(u'Adiciono no carrinho')
def step_impl(context):
    pass


@then(u'O item vai para o carrinho')
def step_impl(context):
    pass