from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def jamesbond():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#fffff8') 
        blt.printf(6, 0, '[color=#F73718]EGOTEXT   << 007 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h[/color]')
        cfg.ascii_art('res/egotext/james.txt', 1, 2)

        blt.color('#F5BD02') 
        blt.printf(2, 25, """
         .-.  .-.  --..::==
        (   )(   )  //"
         '-'  '-'  /    
        GOLDENEYE - EM BREVE
""")
        blt.puts(1, 33, " " * 70)
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
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                blt.refresh()
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
    jamesbond()