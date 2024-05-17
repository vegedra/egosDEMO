from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def password():
    #blt.open()
    blt.set(f"window.title='egOS - Password'; window.size=85x35") 
    blt.color('#FFB000')

    cfg.game_state['enigma_pesquisa']  = 1

    logic()

def logic():
    while True:
        blt.clear()

        cfg.ascii_art('res/password.txt', 15, 4, False)
        blt.print(2, 33, '<- VOLTAR PARA O DESKTOP')
        blt.printf(12, 1, '<< SEGUNDA-FEIRA - 11 DE ABRIL, 1996 /')
        blt.refresh()

        # Mostra a hora em tempo real
        if cfg.game_state['current_language'] == 'pt_BR':
            cfg.relogio(57, 1)
            blt.printf(66, 1, ">>")
        else:
           cfg.relogio(48, 1)
           blt.printf(60, 1, ">>")

        if blt.has_input():

            key = blt.read()

            if key in (blt.TK_CLOSE, blt.TK_ESCAPE, blt.TK_LEFT):    
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                from desktop.desktop import terminal
                blt.clear()
                terminal()

            elif key == blt.TK_F4:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from config import toggle_fullscreen
                toggle_fullscreen()

            elif key == blt.TK_SPACE:
                # Abre o EGO++
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                blt.refresh()
                from desktop.terminal import ego_code
                ego_code()

if __name__ == "__main__": 
    password() 