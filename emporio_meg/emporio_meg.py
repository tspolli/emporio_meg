from .menu import Menu
import os

class EmporioMeg(object):
    
    
    def __init__(self):
        pass

    def run(self):
        Menu.menu_principal()
        opcao = int(input())
        
        while opcao!=0:
            while opcao!=1 and opcao!=2:
                Menu.opcao_invalida()
                enter = str(input())
            else:
                if opcao==1:
                    Menu.login()
                    os.system("cls")
                    Menu.submenu_login()
                    opcao = int(input())
                    while opcao!=0 and opcao!=1 and opcao!=2 and opcao!=3 and opcao!=4 and opcao!=5: 
                        Menu.opcao_invalida()
                        enter = str(input())
                    else:
                        if opcao==1:
                            os.system("cls")
                            Menu.administrador()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        if opcao==2:
                            os.system("cls")
                            Menu.submenu_seguranca()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        if opcao==3:
                            os.system("cls")
                            Menu.submenu_estoque()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        if opcao==4:
                            os.system("cls")
                            Menu.submenu_caixa()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        if opcao==5:
                            os.system("cls")
                            Menu.submenu_financeiro()
                            enter = str(input())
                            Menu.submenu_login()
                            opcao = int(input())
                        if opcao==0:
                            Menu.menu_principal()
                            opcao = int(input())
                elif opcao==2:
                    Menu.ajuda()
                    Menu.menu_principal()
                    opcao = int(input())
        else:
            Menu.sair()