from .menu import Menu 

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
                    Menu.menu_principal()
                    opcao = int(input())
                elif opcao==2:
                    Menu.ajuda()
                    Menu.menu_principal()
                    opcao = int(input())
        else:
            Menu.sair()