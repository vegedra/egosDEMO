from bearlibterminal import terminal as blt
import config as cfg
import language
from pygame import mixer

def sair():
    if blt.has_input():
        # Check for the exit key
        key = blt.read()
        if key in (blt.TK_CLOSE, blt.TK_5, blt.TK_ESCAPE):
            cfg.clear_input_queue()
            blt.clear()
            from main import main_menu
            main_menu() 

def tutorial():
    blt.set('window.size=85x35')
    blt.color('white')
    tv = """
     _____________________________________________________________ 
    /                                                             \ 
    |   ________________________________________________________   |
    |  /                                                        \  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  |                                                        |  |
    |  \________________________________________________________/  |
    |                                                              |
    |                                                              |
    |                                                _       _     |
    |                  ----------------------       ( )     ( )    |
    |                                                              |
    \______________________________________________________________/
    """
    blt.print(7, 2, '' + tv)

    language.get_localized_text('intro1', section='howtoplay', color="yellow")
    language.get_localized_text('intro2', section='howtoplay')
    blt.refresh()
    sair()
    blt.delay(2000)
    language.get_localized_text('intro3', section='howtoplay')
    language.get_localized_text('intro4', section='howtoplay', color="red")
    blt.refresh()
    sair()
    blt.delay(2000) 
    language.get_localized_text('intro5', section='howtoplay')
    language.get_localized_text('intro6', section='howtoplay')
    blt.refresh()
    sair()
    
    if cfg.game_state['current_language'] == 'pt_BR':
        blt.delay(2000)
        language.get_localized_text('intro7', section='howtoplay', color="red")
        
    if cfg.game_state['current_language'] == 'en': 
        blt.delay(2000)
        language.get_localized_text('intro7', section='howtoplay')
        
    blt.refresh()
    sair()
    
    if cfg.game_state['current_language'] == 'pt_BR':
        blt.delay(2000)
    
    language.get_localized_text('intro8', section='howtoplay')
    language.get_localized_text('intro9', section='howtoplay')
    
    if cfg.game_state['current_language'] == 'pt_BR':
        language.get_localized_text('intro10', section='howtoplay')
    
    blt.refresh()
    sair()
    blt.delay(6000)

    # Frame 2 (fade out)
    blt.clear()
    blt.print(7, 2, '' + tv)
    blt.refresh()
    sair()
    language.get_localized_text('intro1', section='howtoplay', color="#3d3d08")
    language.get_localized_text('intro2', section='howtoplay', color ="gray")
    language.get_localized_text('intro3', section='howtoplay', color ="gray")
    language.get_localized_text('intro4', section='howtoplay', color="#4a171f")
    language.get_localized_text('intro5', section='howtoplay', color ="gray")
    language.get_localized_text('intro6', section='howtoplay', color ="gray")
    
    if cfg.game_state['current_language'] == 'pt_BR':
        language.get_localized_text('intro7', section='howtoplay', color="#4a171f")
        
    if cfg.game_state['current_language'] == 'en': 
        language.get_localized_text('intro7', section='howtoplay', color ="gray")
        
    language.get_localized_text('intro8', section='howtoplay', color ="gray")
    language.get_localized_text('intro9', section='howtoplay', color ="gray")
    
    if cfg.game_state['current_language'] == 'pt_BR':
        language.get_localized_text('intro10', section='howtoplay', color ="gray")
    blt.refresh()
    sair()
    blt.delay(1000)

    # Frame 3 (fade out)
    blt.print(7, 2, '' + tv)
    blt.refresh()
    language.get_localized_text('intro1', section='howtoplay', color="#171717")
    language.get_localized_text('intro2', section='howtoplay', color="#171717")
    language.get_localized_text('intro3', section='howtoplay', color="#171717")
    language.get_localized_text('intro4', section='howtoplay', color="#171717")
    language.get_localized_text('intro5', section='howtoplay', color="#171717")
    language.get_localized_text('intro6', section='howtoplay', color="#171717")
    language.get_localized_text('intro7', section='howtoplay', color="#171717")
    language.get_localized_text('intro8', section='howtoplay', color="#171717")
    language.get_localized_text('intro9', section='howtoplay', color="#171717")
    
    if cfg.game_state['current_language'] == 'pt_BR':
        language.get_localized_text('intro10', section='howtoplay', color="#171717")
    blt.refresh()
    sair()
    blt.delay(1000)

    # Frame 4 (fade out)
    blt.clear()
    blt.refresh()
    blt.color('#fff4e6')
    sair()
    blt.delay(2000)
    
    cfg.clear_input_queue()

    from main import main_menu
    main_menu()

# Sinceramente nao sei, mas deve ser importante
if __name__ == "__main__": 
    tutorial() 