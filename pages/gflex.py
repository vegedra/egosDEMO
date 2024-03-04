from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def gflex():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#00b41b')  #010100
        blt.printf(6, 0, 'EGOTEXT   << 98 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')
        cfg.ascii_art('res/egotext/GFLEX.txt', 7, 7)
        blt.printf(7, 7,' ')
        blt.printf(12, 25,'Um oferecimento G-FLEX Etiquetas e Rótulos Adesivos.')
        blt.printf(24, 26,'www.gflexetiquetas.com.br')

        blt.refresh()

        if blt.has_input():
             key = blt.read()

             if key == blt.TK_RIGHT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                from pages.unlock_B import erroo
                blt.clear()
                cfg.clear_input_queue()
                erroo()

             elif key == blt.TK_S:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from pages.search import match_pages
                cfg.clear_input_queue()
                match_pages()

             elif key == blt.TK_ESCAPE:   
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
    gflex()