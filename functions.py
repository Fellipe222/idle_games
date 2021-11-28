import pyautogui
import time
import subprocess
import threading
import os
import psutil


class Jogo:
    def __init__(self):
        self.parar_jogo = False

    def idle_td(self):
        print('iniciando funcao : idle_td()')
        root = os.getcwd() + r'\images\idle_monster_td'
        lap = 0
        while True:
            if self.parar_jogo == True:
                print('Jogo parado')
                break

            icon    = pyautogui.locateOnScreen(root + r'\icon_idle_monster_td.png', confidence=0.8)
            caixa   = pyautogui.locateOnScreen(root + r'\treasure.png', confidence=0.8)
            gold    = pyautogui.locateOnScreen(root + r'\gold.png')
            exp     = pyautogui.locateOnScreen(root + r'\exp.png')
            worm    = pyautogui.locateOnScreen(root + r'\worm.png')
            play    = pyautogui.locateOnScreen(root + r'\play.png')
            essence = pyautogui.locateOnScreen(root + r'\essence.png')
            close   = pyautogui.locateOnScreen(root + r'\close.png', confidence=0.8)

            campos = [icon, caixa, gold, exp, essence, worm, play, close]

            for campo in campos:
                if campo != None:
                    pyautogui.click(campo)

            time.sleep(4)

    def almost_a_hero(self):
        print('iniciando funcao : almost_a_hero()')
        root = os.getcwd() + r'\images\almost_a_hero'
        ini_timer = time.time()
        lap  = 0
        aeon = 0
        while True:
            if self.parar_jogo == True:
                print('Jogo parado')
                break
            icon    = pyautogui.locateOnScreen(root + r'\icon_almost_a_hero.png', confidence=0.8)
            start   = pyautogui.locateOnScreen(root + r'\start_btn.png', confidence=0.8)
            collect = pyautogui.locateOnScreen(root + r'\collect_btn.png', confidence=0.8)
            gates   = pyautogui.locateOnScreen(root + r'\gates.png')
            no_btn  = pyautogui.locateOnScreen(root + r'\no_btn.png')


            campos = [icon,start, collect, gates, no_btn]

            for campo in campos:
                if campo != None:
                    pyautogui.click(campo)      


            if collect != None:
                aeon  += 263
                lap += 1
                fim_timer = time.time()
                tempo = fim_timer - ini_timer
                tempo = tempo.__round__(2)
                print(f"\n--> Lap {lap} => {tempo} segundos\nAEON's : {aeon}")
                ini_timer = time.time()

            time.sleep(4)

    def idlecus(self):
        print('iniciando funcao : idlecus()')
        root = os.getcwd() + r'\images\idlecus'
        hr,min,seg = 0,0,0
        vender_itens = 0

        while True:
            caldeirao   = pyautogui.locateOnScreen(root + r'\caldeirao.png') 
            voltar      = pyautogui.locateOnScreen(root + r'\voltar.png')
            erro        = pyautogui.locateOnScreen(root + r'\erro.png') 
            erro2       = pyautogui.locateOnScreen(root + r'\erro2.png') 
            mochila     = pyautogui.locateOnScreen(root + r'\mochila.png')
            vender      = pyautogui.locateOnScreen(root + r'\vender.png') 
            fechar      = pyautogui.locateOnScreen(root + r'\fechar.png')  
            x,y         = pyautogui.position()

            seg += 1

            if seg == 60: 
                min +=1
                vender_itens +=1
                seg = 0

            if min == 60:
                hr+=1  
                min = 0  

            os.system('cls')
            print(f'x: {x} y: {y}\n{hr} h {min} min {seg} seg\nvender_itens: {vender_itens}')
            time.sleep(1)
            # Caso o botao voltar aparecer na tela, significa que o boneco morreu
            if voltar:
                pyautogui.click(voltar)
                time.sleep(0.2)
                pyautogui.moveTo(649,565) #move o mouse para o centro da tela
                pyautogui.dragTo(649,428,5, button='left') # arrasta o personagem para o campo de batalha

            if erro or erro2:
                pyautogui.click(x=646, y=565) # ignora a mensagem de erro do app

            if vender_itens == 5: # vende os itens indesejados periodicamente 
                pyautogui.click(mochila)
                time.sleep(0.5)

                lixeira = pyautogui.locateOnScreen(root + r'\lixeira.png')
                pyautogui.click(lixeira)
                time.sleep(0.5)

                vender = pyautogui.locateOnScreen(root + r'\vender.png')
                fechar = pyautogui.locateOnScreen(root + r'\fechar.png')
                pyautogui.click(vender) if vender else pyautogui.click(fechar)
                time.sleep(0.5)

                fechar = pyautogui.locateOnScreen(root + r'\fechar.png')
                pyautogui.click(fechar)

                vender_itens = 0
 
    def stop_jogo(self):
        self.parar_jogo = True

class Nox:  
    def __init__(self):
        self.nox_pid = ''

    def check_path(self):
        path = open("nox_path.txt","r")
        path = path.read()
        if 'Nox.exe' not in path:
            return -1

    def inicializar(self): 
        path = open("nox_path.txt","r")
        path = path.read()   
        print('Abrindo Nox...')
        try:
            nox = subprocess.Popen(path)
            self.nox_pid = nox.pid
            print(f'Nox pid : {nox.pid}')
        except FileNotFoundError:
            print(f'O diretorio "{path}" não foi encontrado')
            return -1

    def fechar(self):
        kill_nox = psutil.Process(self.nox_pid)
        kill_nox.terminate()
        print('Nox fechado')

a = Jogo().idlecus()

        

        

