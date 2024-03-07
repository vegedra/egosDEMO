from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def troll():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#fffff8') 
        blt.printf(6, 0, '[color=#F73718]EGOTEXT   << 777 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h[/color]')
        cfg.ascii_art('res/egotext/otroll.txt', 3, 2)
        blt.puts(1, 33, " ")
        blt.puts(3, 2, "@B@B@B@B@B@B@B@B@B@B@B@B@B@@@B@B@B@B@B@B@@@B@B@B@@@B@B@B@B@B@B@B@B@B") 
        blt.refresh()

        if blt.has_input():
             cfg.egotext_input()

             if cfg.key in (blt.TK_ESCAPE, blt.TK_LEFT):  
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)    
                from desktop.desktop import terminal
                blt.clear()
                terminal()

if __name__ == "__main__": 
    troll()