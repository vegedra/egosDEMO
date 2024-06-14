from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def espaco():
    blt.set('window.size=75x35')

    cfg.play_music('bgm/portal.ogg', volume=0.2, loop=-1, crossfade_duration=10)

    logic()

def logic():
    while True:
        blt.color('#FFF8E7') 
        language.get_localized_text('welcome5', section='egotext', color="#FFF8E7") 
        blt.printf(19, 0, '999')
        cfg.ascii_art('res/egotext/space.txt', 0, 2, True)
        blt.refresh()

        if blt.has_input():
             mixer.music.fadeout(1000)
             cfg.egotext_input()

             if cfg.key in (blt.TK_ESCAPE, blt.TK_LEFT):   
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)   
                from desktop.desktop import terminal
                blt.clear()
                cfg.clear_input_queue()
                terminal()

if __name__ == "__main__": 
    espaco()