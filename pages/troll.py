from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def troll():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#fffff8') 
        language.get_localized_text('welcome5', section='egotext', color="#F73718") 
        blt.printf(20, 0, '777')
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