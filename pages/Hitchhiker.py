from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def resposta():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#C1E3ED') 
        language.get_localized_text('welcome6_1', section='egotext', color="#C1E3ED") 
        blt.printf(19, 0, '42')

        language.get_localized_text('hitchhiker', section='egotext', color="#C1E3ED") 
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
    resposta()