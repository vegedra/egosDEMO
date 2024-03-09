from bearlibterminal import terminal as blt
import config as cfg
from pygame import mixer
import language

def clima():
    #blt.open()
    blt.set('window.size=75x35')
    # Toca a OST adaptativa
    cfg.play_music('bgm/egotext_loop2.ogg', volume=0.8, loop=-1, crossfade_duration=10)

    logic()

def logic():
    while True:
        blt.bkcolor('black') 
        language.get_localized_text('welcome5', section='egotext', color="yellow") 
        blt.printf(19, 0, '[color=yellow]101[/color]')
        blt.bkcolor('#73a8d1')
        blt.color('black') 
        blt.printf(1, 1, """
                                                                         
                                                                         
                                                                         
                                                                         
                                       ▒▒▒▒▒▒                            
                                ▒▒     ▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒        
                              ▒▒▒▒▒    ▒▒▒▒▒▒      ▒▒▒   ▒▒▒▒▒▒▒▒        
         ▒▒▒▒        ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒     ▒▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▒▒▓▓▓▒▒▒     ▒▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▓▓▓▓▓▓▓▒     ▒▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▓▓ ▓ ▓▓▒     ▒▒▒
▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒
▒▒▒   ▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓ ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓ ▓ ▓▓▒▓▓▓▓▒▒▒▒
▒▒▒░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▒▓▓ ▓▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓ ▓▒▒▒▒▓▓▒▒▒▒▒▓▓ ▓ ▓ ▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▒▒▒▒
▒▒▒▒▓▓▓▒▒▒▒▓▓ ▓▓ ▓▓▓▓  ▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓  ▓ ▓ ▓▒▒▒▒▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▓▓ ▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
""")
        language.get_localized_text('welcome8', section='egotext', color="white") 
        language.get_localized_text('welcome9', section='egotext', color="white") 
        blt.refresh()

        if blt.has_input():

            cfg.egotext_input()

            if key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.welcome import saudacao
                blt.clear()
                cfg.clear_input_queue()
                saudacao()

            elif key == blt.TK_RIGHT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)    
                blt.color('white')
                blt.bkcolor('black')
                from pages.ad_filme import olho
                blt.clear()
                cfg.clear_input_queue()
                olho()

if __name__ == "__main__": 
    clima() 