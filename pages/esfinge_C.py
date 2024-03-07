from bearlibterminal import terminal as blt
from pygame import mixer

def esfinge_C():
    #blt.open()
    blt.set("window: size=75x35, cellsize=0x0") 
    mixer.music.unpause()

    logic()
    
def logic():
    while True:
        import config as cfg
        blt.color('#ffdc73')
        blt.printf(6, 0, 'EGOTEXT   << 106 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')

        cfg.ascii_art('res/egotext/esfinge_rosto.txt', 12, 6)
    
        blt.printf(22, 26, 'Parabéns por completar a demo.')
        blt.printf(22, 27, 'Eu tenho um presente para você!')
        blt.printf(31, 28, 'Vá para 777.')
        blt.refresh()

        if blt.has_input():
            cfg.egotext_input()

            if cfg.key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)   
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.esfinge_A import esfinge_A
                blt.clear()
                esfinge_A()

            else:
                logic()  

if __name__ == "__main__": 
    esfinge_C() 