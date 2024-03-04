from bearlibterminal import terminal as blt
import config as cfg
import language

def pesquisa():
    #blt.open()
    blt.set(f"window.title='egOS - Pesquisa'; window.size=85x35") 
    blt.color('#FFB000')

    logic()

def logic():
    while True:
        blt.clear()
        if cfg.game_state['current_language'] == 'en': 
            cfg.ascii_art('res/desktop/thera_en.txt', 3, 4)
        else:
            cfg.ascii_art('res/desktop/thera.txt', 3, 4)
        blt.print(3, 4, " ")

        language.get_localized_text('manual1', section='manual', color="#ffb000")
        language.get_localized_text('manual3', section='manual', color="#ffb000")

        if cfg.game_state['current_language'] == 'pt_BR':
            cfg.relogio(57, 1)
            blt.printf(66, 1, ">>")
        else:
           cfg.relogio(48, 1)
           blt.printf(60, 1, ">>")
        blt.refresh()

        if blt.has_input():

            key = blt.read()

            if key == blt.TK_SPACE:
                # Abre o EGO++
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                from desktop.terminal import ego_code
                ego_code()

            elif key == blt.TK_F4:
                cfg.clear_input_queue()
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from config import toggle_fullscreen
                toggle_fullscreen()

            elif key in (blt.TK_CLOSE, blt.TK_ESCAPE, blt.TK_LEFT):    
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                from desktop.desktop import terminal
                blt.clear()
                cfg.clear_input_queue()
                terminal()

if __name__ == "__main__": 
    pesquisa() 