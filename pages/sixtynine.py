from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def meianove():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#FE524D') 
        language.get_localized_text('welcome5', section='egotext', color="#FE524D") 
        blt.printf(20, 0, '69')
        cfg.ascii_art('res/egotext/meianove.txt', 18, 8)
        blt.puts(1, 33, " " * 70)
        blt.refresh()

        if blt.has_input():
             cfg.egotext_input()

             if cfg.key in (blt.TK_ESCAPE, blt.TK_LEFT):  
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)    
                from desktop.desktop import terminal
                blt.clear()
                terminal()

if __name__ == "__main__": 
    meianove()