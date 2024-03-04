from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def art():
    #blt.open()
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('purple')
        cfg.ascii_art('res/egotext/g_art_face.txt', 8, 2)
        blt.printf(8, 2, " ")

        blt.color('pink') 
        blt.printf(6, 0, 'EGOTEXT   << 104 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')
        blt.printf(33, 33, 'prope est')
        blt.puts(1, 33, " " * 30)
        blt.refresh()

        if blt.has_input():
             key = blt.read()

             if key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)    
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.ad_porn import porn
                blt.clear()
                porn()

             elif key == blt.TK_RIGHT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)    
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.esfinge_A import esfinge_A
                blt.clear()
                esfinge_A()

             elif key == blt.TK_S:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                from pages.search import match_pages
                match_pages()

             elif key == blt.TK_ESCAPE:     
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

             else:
                logic()  

if __name__ == "__main__": 
    art()