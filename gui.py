import PySimpleGUI as sg
import time
import functions as func
import threading
import sys

parar_jogo = False
class Tela1 :
    def __init__(self):
        self.nox_app = func.Nox()
        self.jogo = func.Jogo()
        self.nox_inicializado = False
        self.thread_jogo = ''

        path = open("nox_path.txt","rt").read()
        #layout
        sg.theme('DarkGreen3')
        layout = [
            [sg.Text('Este aplicativo foi feito para pessoas preguiçosas que não têm paciência de jogar jogos IDLE, porém, desejam ter um bom progresso neles :D.\n\n', size=(60,2))],
            [sg.Text('Selecione o local do executável do Nox :')],
            [sg.Input(default_text=path, text_color="#0000f0", key="diretorio"),sg.FileBrowse("...", key="troca_diretorio",enable_events=True),sg.Button('Atualizar',key="atualizar_diretorio")],
            [sg.Text('\n\nSelecione abaixo qual jogo desejas jogar no modo automático', size=(60,0))],
            [sg.InputOptionMenu(('Idle Monster TD','Almost a hero'),default_value='Idle Monster TD',text_color='#0000f0', key='jogo_escolhido',size=(40,1)),sg.Button('JOGAR!',tooltip='Pode ir dormir agora...'),sg.Button('PARAR',tooltip='O Nox será encerrado.')],
            [sg.Text('', key='output', size=(60,2),text_color="#FF0000")]
            #[sg.Output(size=(60,4))]
        ]
        #Janela
        self.janela = sg.Window('AUTO IDLE PLAYER').layout(layout)
    
    def Iniciar(self):
        while True:
            # Extrair dados da tela
            self.event, self.values  = self.janela.Read()
            print('ping...')

            if self.event == sg.WIN_CLOSED:
                self.nox_app.fechar()
                self.jogo.stop_jogo()
                sys.exit()
                break

            if self.event == 'JOGAR!':
                if self.nox_app.check_path() == -1:
                    sg.popup('Selecione o diretório que contenha o executável do aplicativo Nox',title='Aviso')
                else:
                    if self.nox_inicializado == False:  
                        if self.nox_app.inicializar() == -1:
                            sg.popup('Você não possui o Nox neste diretório \n\nAcesse: https://pt.bignox.com/ para fazer o download.',title='Aviso')
                            sys.exit()
                        else:
                            self.nox_app.inicializar()
                            self.nox_inicializado = True
                            print(f"Jogo escolhido : {self.values['jogo_escolhido']}")  
                                     
                    if self.values['jogo_escolhido'] == 'Idle Monster TD':
                        self.thread_jogo = threading.Thread(target=self.jogo.idle_td).start()
                        
                    elif self.values['jogo_escolhido'] == 'Almost a hero':   
                        self.thread_jogo = threading.Thread(target=self.jogo.almost_a_hero).start()                                  
                                                                
            if self.event == 'atualizar_diretorio':
                diretorio = self.values['diretorio']
                #C:\Program Files (x86)\Nox\bin\Nox.exe
                path = open('nox_path.txt','w')
                path.write(diretorio)
                path.close()

            if self.event == 'PARAR':
                self.jogo.stop_jogo()
                
                
tela = Tela1()
tela.Iniciar()