from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def porn():
    #blt.open()
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('pink') 
        cfg.ascii_art('res/egotext/dama.txt', 1, 5, False)
        blt.printf(1, 5, ' ')

        blt.color('yellow')
        cfg.ascii_art('res/egotext/dama_tel.txt', 6, 27, True)
        blt.printf(14, 27, ' ')
        language.get_localized_text('welcome5', section='egotext', color="pink") 

        blt.color('pink') 
        blt.printf(19, 0, '103')
        language.get_localized_text('porn2', section='egotext', color="pink") 
        language.get_localized_text('porn3', section='egotext', color="pink") 
        language.get_localized_text('porn4', section='egotext', color="pink") 
        language.get_localized_text('porn5', section='egotext', color="pink") 
        language.get_localized_text('porn1', section='egotext', color="pink") 
        blt.puts(1, 33, " " * 70)
        blt.refresh()

        if blt.has_input():
             cfg.egotext_input()

             if cfg.key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.ad_filme import olho
                blt.clear()
                olho()

             elif cfg.key == blt.TK_RIGHT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.art_face import art
                blt.clear()
                art()

             else:
                logic()  

if __name__ == "__main__": 
    porn()