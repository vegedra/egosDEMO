from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def espaco():
    blt.set('window.size=75x35')

    cfg.play_music('bgm/portal.ogg', volume=0.2, loop=-1, crossfade_duration=10)

    logic()

def logic():
    while True:
        blt.color('#FFF8E7') 
        blt.printf(6, 0, 'EGOTEXT   << 999 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')
        cfg.ascii_art('res/egotext/space.txt', 0, 2)
        blt.refresh()

        if blt.has_input():
             key = blt.read()

             if key == blt.TK_S:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                from pages.search import match_pages
                cfg.clear_input_queue()
                match_pages()

             elif key in (blt.TK_ESCAPE, blt.TK_LEFT):   
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)   
                mixer.music.fadeout(1000)
                from desktop.desktop import terminal
                blt.clear()
                cfg.clear_input_queue()
                terminal()

             elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from desktop.terminal import ego_code
                cfg.clear_input_queue()
                ego_code()

             elif key == blt.TK_CLOSE:    
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                mixer.music.fadeout(1000)
                from exit_confirmation import main
                cfg.clear_input_queue()
                main()    

             elif key == blt.TK_F4:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from config import toggle_fullscreen
                cfg.clear_input_queue()
                toggle_fullscreen()

if __name__ == "__main__": 
    espaco()