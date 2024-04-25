from bearlibterminal import terminal as blt
from pygame import mixer
import language

def esfinge_C():
    #blt.open()
    blt.set("window: size=75x35, cellsize=0x0") 
    mixer.music.unpause()

    logic()
    
def logic():
    while True:
        import config as cfg
        blt.color('#ffdc73')
        language.get_localized_text('welcome5', section='egotext', color="#ffdc73") 
        blt.printf(20, 0, '106')

        cfg.ascii_art('res/egotext/esfinge_rosto.txt', 12, 6)
        cfg.ascii_art('res/egotext/esfinge_rosto.txt', 12, 6)
    
        language.get_localized_text('esfinge_c1', section='egotext', color="#ffdc73") 
        language.get_localized_text('esfinge_c2', section='egotext', color="#ffdc73") 
        language.get_localized_text('esfinge_c3', section='egotext', color="#ffdc73") 
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