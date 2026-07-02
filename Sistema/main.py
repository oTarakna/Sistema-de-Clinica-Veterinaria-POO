from database.criacao_tabelas import inicializar_banco
from ui.menu import TerminalUI

inicializar_banco()
app = TerminalUI()
app.exibir_menu_principal()
