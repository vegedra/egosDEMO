from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def art():
    #blt.open()
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('purple')
        cfg.ascii_art('res/egotext/g_art_face.txt', 8, 2, True)
        blt.printf(8, 2, " ")

        blt.color('pink') 
        language.get_localized_text('welcome5', section='egotext', color="pink") 
        blt.color('pink') 
        blt.printf(19, 0, '104')
        blt.printf(33, 33, 'prope est')
        blt.puts(1, 33, " " * 30)
        blt.refresh()

        if blt.has_input():
             cfg.egotext_input()

             if cfg.key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)    
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.ad_porn import porn
                blt.clear()
                porn()

             elif cfg.key == blt.TK_RIGHT:
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
    art()