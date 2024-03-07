from bearlibterminal import terminal as blt
from pygame import mixer

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
        blt.printf(6, 0, 'EGOTEXT   << 666 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')
        cfg.ascii_art('res/egotext/ele.txt', 0, 1)
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