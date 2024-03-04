from bearlibterminal import terminal as blt
from pygame import mixer
from itertools import cycle
import config as cfg

def erro():
    #blt.open()
    blt.set('window.size=75x20')
    blt.color('black')
    blt.printf(6, 0, '[color=yellow]EGOTEXT   << 0 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h[/color]')

    blt.printf(12, 4, '[color=#ff71ce]       ___   ___   ________  ____   ___        [/color]')
    blt.printf(12, 5, '[color=#01cdfe]      |\  \ |\  \ /\   __  \|\   \ |\  \       [/color]')
    blt.printf(12, 6, '[color=#05ffa1]      \ \  \|_\  \  \  \/\  \ \   \__\  \      [/color]')
    blt.printf(12, 7, '[color=#b967ff]       \ \_____   \  \  \ \  \ \______   \     [/color]')
    blt.printf(12, 8, '[color=#fffb96]        \|____|\   \  \  \_\  \|_____|\   \    [/color]')
    blt.printf(12, 9, '[color=#ff3f3f]              \ \___\  \_______\     \ \___\   [/color]')
    blt.printf(12, 10, '[color=#001eff]               \|___|\_|_______|      \|___|  [/color]')  

    blt.printf(26, 13, '[color=#674ea7]PÁGINA NÃO ENCONTRADA[/color]')  
    blt.refresh()

    logic()

def logic():
    # Define os frames da animação de loading
    loading_animation = cycle(['|', '/', '-', '\\'])
    blt.color('#674ea7')
      
    # Loop da animação, que roda 30 vezes  
    for i in range(15):
        blt.delay(100)
        blt.print(48, 13, next(loading_animation))
        blt.refresh()

    from pages.welcome import saudacao
    blt.clear()
    cfg.clear_input_queue()
    saudacao()

if __name__ == "__main__": 
    erro() 