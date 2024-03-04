from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def djabo():
    blt.set('window.size=75x35')

    import config as cfg
    cfg.game_state['666']  = 1

    mixer.music.stop()

    logic()

def logic():
    while True:
        blt.color('#ae0000') 
        blt.printf(6, 0, 'EGOTEXT   << 666 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')
        cfg.ascii_art('res/egotext/ele.txt', 0, 1)
        blt.refresh()

        if blt.has_input():
            key = blt.read()

            if key == blt.TK_S:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                import config as cfg
                cfg.game_state['666']  = 0
                from pages.search import match_pages
                match_pages()

            elif key in (blt.TK_ESCAPE, blt.TK_LEFT):    
                import config as cfg
                cfg.game_state['666']  = 0  
                from desktop.desktop import terminal
                blt.clear()
                terminal()

            elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                from desktop.terminal import ego_code
                ego_code()

            elif key == blt.TK_CLOSE:    
                import config as cfg
                cfg.game_state['666']  = 0  
                from exit_confirmation import main
                main()    

            elif key == blt.TK_F4:
                from config import toggle_fullscreen
                toggle_fullscreen()

if __name__ == "__main__": 
    djabo()