from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def olho():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#f20505') 
        cfg.ascii_art('res/egotext/olho1.txt', 5, 4)
        blt.printf(5, 4, '@')

        language.get_localized_text('welcome5', section='egotext', color="#f0e046") 
        blt.printf(19, 0, '[color=#f0e046]102[/color]')

        language.get_localized_text('adfilme1', section='egotext', color="#f0e046") 
        language.get_localized_text('adfilme2', section='egotext', color='#f20505')
        language.get_localized_text('adfilme3', section='egotext', color="#f0e046") 
        blt.puts(1, 33, " " * 30)
        blt.refresh()

        if blt.has_input():
             cfg.egotext_input()

             if cfg.key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.weather import clima
                blt.clear()
                clima()

             elif cfg.key == blt.TK_RIGHT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.ad_porn import porn
                blt.clear()
                porn()

             else:
                logic()    

if __name__ == "__main__": 
    olho()