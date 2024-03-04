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
        cfg.ascii_art('res/egotext/otroll.txt', 3, 1)
        blt.puts(1, 33, " ")
        blt.puts(3, 1, "@B@B@B@B@B@B@B@B@B@B@B@B@B@@@B@B@B@B@B@B@@@B@B@B@@@B@B@B@B@B@B@B@B@B") 
        blt.refresh()

        if blt.has_input():
             key = blt.read()

             if key == blt.TK_S:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                from pages.search import match_pages
                match_pages()

             elif key in (blt.TK_ESCAPE, blt.TK_LEFT):  
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)    
                from desktop.desktop import terminal
                blt.clear()
                terminal()

             elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                from desktop.terminal import ego_code
                ego_code()

             elif key == blt.TK_CLOSE:    
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0) 
                from exit_confirmation import main
                main()    

             elif key == blt.TK_F4:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0) 
                from config import toggle_fullscreen
                toggle_fullscreen()

if __name__ == "__main__": 
    troll()