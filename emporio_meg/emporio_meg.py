from pymongo import MongoClient
from .menu import Menu
import os

class EmporioMeg(object):
    
    
    def __init__(self):
       self.client = MongoClient("mongodb+srv://tspolli:adivinha@clusterproject-wbem2.mongodb.net/Emporio_meg?retryWrites=true&w=majority")


    def run(self):
        banco = self.client["Emporio_meg"]
        collection_usuario = banco["Usuario"]
        
        #  novo_usuario = {
        #  "usuario": "Felipe",
        #  "senha": "teste",
        #  "nome": "Felipe Carasco"    
        #  }
        #  a = collection_usuario.insert_one(novo_usuario).inserted_id

        Menu.menu_principal()
        opcao = int(input())

        while opcao!=0:  
            if opcao==1:
                dados_retornados = Menu.login()
                os.system("cls")
                login_validado = collection_usuario.find_one({"usuario": dados_retornados[0], "senha": dados_retornados[1]})
                if login_validado != None: 
                    print("LOGIN EFETUADO COM SUCESSO")
                    print("PRESSIONE ENTER PARA CONTINUAR...")
                    enter = str(input())
                    Menu.submenu_login()
                    opcao = int(input())
                    while opcao!=0:
                        if opcao==1:
                            os.system("cls")
                            Menu.administrador()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        elif opcao==2:
                            os.system("cls")
                            Menu.submenu_seguranca()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        elif opcao==3:
                            os.system("cls")
                            Menu.submenu_estoque()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        elif opcao==4:
                            os.system("cls")
                            Menu.submenu_caixa()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        elif opcao==5:
                            os.system("cls")
                            Menu.submenu_financeiro()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        else:
                            Menu.opcao_invalida()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                    else:
                        Menu.menu_principal()
                        opcao = int(input())
                else:
                    print("USUÁRIO E/OU SENHA INVÁLIDO(S)")
                    print("PRESSIONE ENTER PARA CONTINUAR...")
                    enter = str(input())
                    Menu.menu_principal()
                    opcao = int(input())
            elif opcao==2:
                Menu.ajuda()
                Menu.menu_principal()
                opcao = int(input())
            else:
                Menu.opcao_invalida()
                enter = str(input())
                Menu.menu_principal()
                opcao = int(input())
        else:
            Menu.sair()