from bearlibterminal import terminal as blt
import config as cfg
import language

def intro():
    blt.set('window.size=85x35')
    blt.color('white')
    
    # Frame 1
    # Printa texto: (x, y, 'texto')
    blt.clear()
    blt.print(31, 17, 'Pedro Ivo (c) 2022-2024')

    # Updata a tela do BLT e imprime o que foi escrito
    blt.refresh()
 
    # Delay em milisegundos
    blt.delay(2000)

    # limpa o blt
    blt.clear()

    # Frame 2
    language.get_localized_text('intro1', section='intro')
    blt.refresh()
    blt.delay(2000)
    blt.clear()   

    # Pega a arte do arquivo .txt e printa na tela
    cfg.ascii_art('res/digitalcakestudio.txt', 0, 0, False)
    blt.refresh()
    blt.delay(3000)
    
    # Clear the input queue
    cfg.clear_input_queue()

# Vai para o main.py
from main import main_menu
main_menu()