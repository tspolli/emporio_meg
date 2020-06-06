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
        print("SELECIONE UMA OPCAO: ")

    def login():
        os.system("cls")
        print("#### LOGIN ####")
        print("USUARIO: ")
        usuario = str(input())
        senha = getpass.getpass("SENHA: ")
        
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