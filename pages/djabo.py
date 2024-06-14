from bearlibterminal import terminal as blt
from pygame import mixer
import language

def djabo():
    import config as cfg
    blt.set('window.size=75x35')
    cfg.game_state['666'] = 1
    mixer.music.stop()

    logic()

def logic():
    import config as cfg
    while True:
        blt.color('#ae0000') 
        language.get_localized_text('welcome5', section='egotext', color="#ae0000") 
        blt.printf(19, 0, '666')
        cfg.ascii_art('res/egotext/ele.txt', 0, 1, True)
        blt.refresh()

        if blt.has_input():
            cfg.egotext_input()

            if cfg.key in (blt.TK_ESCAPE, blt.TK_LEFT):    
                import config as cfg
                cfg.game_state['666'] = 0  
                from desktop.desktop import terminal
                blt.clear()
                terminal()

if __name__ == "__main__": 
    djabo()