from bearlibterminal import terminal as blt
import language
import config as cfg

def credits():
    #blt.open()
    blt.set('window.size=85x35')
    blt.color('#fff4e6')
        
    if cfg.game_state['current_language'] == 'en': 
        cfg.ascii_art('res/credits_en.txt', 5, 3)
    else:
        cfg.ascii_art('res/credits.txt', 5, 3)    
    blt.print(5, 3, " ")   
 
    language.get_localized_text('credit1', section='credits', color="#ffb000")
    language.get_localized_text('credit2', section='credits', color="#ffb000")
    blt.refresh()

    logic()

def logic():
    while True:
        if cfg.game_state['current_language'] == 'en':
            cfg.relogio(60, 0)
        else:
            cfg.relogio(68, 0)
        blt.refresh()

        if blt.has_input():
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            cfg.clear_input_queue()
            from main import main_menu
            main_menu() 

if __name__ == "__main__": 
    credits()