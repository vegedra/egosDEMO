from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def jamesbond():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#fffff8') 
        language.get_localized_text('welcome5', section='egotext', color="#fffff8") 
        blt.printf(19, 0, '007')

        cfg.ascii_art('res/egotext/james.txt', 1, 2)

        blt.color('#F5BD02') 
        blt.printf(2, 25, """
         .-.  .-.  --..::==
        (   )(   )  //"
         '-'  '-'  /    
        GOLDENEYE - 007
""")
        blt.puts(1, 33, " " * 70)
        blt.refresh()

        if blt.has_input():
             cfg.egotext_input()

             if cfg.key in (blt.TK_ESCAPE, blt.TK_LEFT):   
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)   
                from desktop.desktop import terminal
                blt.clear()
                terminal()

if __name__ == "__main__": 
    jamesbond()