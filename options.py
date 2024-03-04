from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

# No idioma: jogador aperta 1 e o idioma muda, continuar apertando vai pro proximo
# Fullscreen mesma coisa

def options():  
    # Cria a janela
    idioma = cfg.game_state['current_language']
    blt.clear()
    blt.set('window.size=85x35')
    blt.refresh()

    logic()
    
def logic():
    while True:
        blt.clear()
        blt.color('#fff4e6')
        blt.bkcolor('black')

        cfg.ascii_art('res/option.txt', 10, 3)
        blt.print(8, 3, "    ") 

        language.get_localized_text('opt1', section='options', color="#ffb000")
        language.get_localized_text('opt2', section='options')
        language.get_localized_text('opt3', section='options')
        language.get_localized_text('credit2', section='credits', color="#ffb000")

        if cfg.is_fullscreen == True:
            language.get_localized_text('opt4', section='options', color="#ffb000")
        else:
            language.get_localized_text('opt5', section='options', color="#ffb000")
            
        if cfg.game_state['current_language'] == 'pt_BR':
            language.get_localized_text('opt7', section='options', color="#ffb000")
       
        if cfg.game_state['current_language'] == 'en':
            language.get_localized_text('opt6', section='options', color="#ffb000")
        
        blt.refresh()
        key = blt.read()
        blt.bkcolor('black')

        # Muda o idioma
        if key == blt.TK_1:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            if cfg.game_state['current_language'] == 'pt_BR':
                cfg.game_state['current_language'] = 'en'
            else:
                cfg.game_state['current_language'] = 'pt_BR'

        # Tela cheia
        elif key in (blt.TK_2, blt.TK_F4):   
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            from config import toggle_fullscreen
            toggle_fullscreen()

        # Sai das opções e volta ou pro menu inicial ou pro desktop
        elif key in (blt.TK_CLOSE, blt.TK_ESCAPE, blt.TK_LEFT):
            if cfg.game_state['options_toDesktop'] == 1:
                blt.clear()
                cfg.clear_input_queue()
                from desktop.desktop import terminal
                terminal()
            else:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                cfg.clear_input_queue()
                blt.clear()
                from main import main_menu
                main_menu() 
                
    cfg.clear_input_queue()

if __name__ == "__main__": 
    options()