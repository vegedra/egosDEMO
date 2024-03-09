from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def arctic():
    blt.set('window.size=75x35')
    
    cfg.play_music('bgm/cincozerocinco.ogg', volume=0.8, loop=-1, crossfade_duration=100)

    logic()

def logic():
    while True:
        blt.color('#FFFAFA') 
        language.get_localized_text('welcome5', section='egotext', color="#FFFAFA") 
        blt.printf(10, 13, """
I'm going back to 505
If it's a seven-hour flight or a 45-minute drive
In my imagination, you're waiting lying on your side
With your hands between your thighs
               """)
        blt.printf(19, 0, '505')
        blt.puts(1, 33, " " * 70)
        blt.refresh()

        if blt.has_input():
             cfg.egotext_input()

             if cfg.key == blt.TK_S:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                from pages.search import match_pages
                match_pages()

             elif cfg.key in (blt.TK_ESCAPE, blt.TK_LEFT): 
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)      
                from desktop.desktop import terminal
                blt.clear()
                terminal()

if __name__ == "__main__": 
    arctic()
