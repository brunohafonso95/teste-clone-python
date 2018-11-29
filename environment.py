
"""		Pyautomator Framework de teste 

			novo_projeto_python"""

from Pyautomators.web import Web
from Pyautomators.Drivers import Manager_Install
from Pyautomators import Ambiente # conversar com pastas e S.O
from Pyautomators import Log
from time import sleep
from pages.pages import Home

# iniciando a captura de logs e criando o arquivo no qual
# serão armazenados os logs
# Obs: caso essa anotação não seja iniciada os logs serão exibidos em console
Log.setup('log/teste.log')

# usando um decorator para capturar o log deste passo
@Log.before_all
def before_all(context):
    # pagando os dados do yaml
	navegador = context.config.userdata['navegador']
	context.url = context.config.userdata['url']
	# usando o driver manager para baixar o driver
	# context é usado para extender o escopo das variaveis para todos os arquivos do teste
	context.app = Web(navegador, Manager_Install(navegador).get_manager())
	# instancioando as pages
	context.home = Home(context.app, context.url) 

# usando um decorator para capturar o log deste passo
@Log.after_steps
def after_step(context,step):
	pass

# usando um decorator para capturar o log deste passo
@Log.after_all
def after_all(context):
	context.app.fechar_programa()

