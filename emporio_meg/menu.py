import os
import getpass

class Menu():


    def menu_principal():
        print("###########################")
        print("        EMPORIO MEG        ")
        print("###########################")
        print("1 - LOGIN")
        print("2 - AJUDA")
        print("0 - SAIR")
        print(" ")
        print("SELECIONE UMA OPCAO: ")

    def login():
        os.system("cls")
        print("#### LOGIN ####")
        print("USUARIO: ")
        usuario = str(input())
        senha = getpass.getpass("SENHA: ")
        
    def submenu_login():
        print("################################")
        print("      SISTEMA EMPORIO MEG       ")
        print("################################")
        print("1 - ADMINISTRADOR")
        print("2 - SEGURANÇA")
        print("3 - ESTOQUE")
        print("4 - CAIXA")
        print("5 - FINANCEIRO")
        print("0 - VOLTAR")
        print(" ")
        print("SELECIONE UMA OPCAO: ") 

    def administrador():
        print("#### ADMINISTRADOR ####")
        print(" ")
        print("PRESSIONE ENTER PARA CONTINUAR...")                      

    def submenu_seguranca():
        print("####   SEGURANCA   ####")
        print(" ")
        print("1 - CADASTRAR USUÁRIO")
        print("2 - BUSCAR USUÁRIO")
        print("3 - LISTAR USUÁRIOS")
        print("0 - VOLTAR")
        print(" ")
        print("PRESSIONE ENTER PARA CONTINUAR: ") 

    def submenu_estoque():
        print("####   ESTOQUE   ####")
        print(" ")
        print("1 - CADASTRAR PRODUTO")
        print("2 - BUSCAR PRODUTO")
        print("3 - EXIBIR ESTOQUE")
        print("0 - VOLTAR")
        print(" ")
        print("PRESSIONE ENTER PARA CONTINUAR: ") 

    def submenu_caixa():
        print("####   CAIXA   ####")
        print(" ")
        print("1 - ABRIR CAIXA")
        print("2 - REGISTRAR COMPRA")
        print("3 - FECHAR CAIXA")
        print("0 - VOLTAR")
        print(" ")
        print("PRESSIONE ENTER PARA CONTINUAR: ") 

    def submenu_financeiro():
        print("####   FINANCEIRO   ####")
        print(" ")
        print("1 - RELATORIO DIARIO")
        print("2 - RELATORIO MENSAL")
        print("0 - VOLTAR")
        print(" ")
        print("PRESSIONE ENTER PARA CONTINUAR: ") 

    def ajuda():
        os.system("cls")
        print("#### AJUDA ####")
        print("VERSAO: 1.0.0")
        print("CRIADO POR: TABATA POLLI")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())

    def sair():
        print("SAINDO...")
        quit

    def opcao_invalida():
        print("OPCAO INDISPONIVEL.")
        print("PRESSIONE ENTER PARA CONTINUAR...")