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







