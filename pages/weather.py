from bearlibterminal import terminal as blt
import config as cfg
from pygame import mixer

def clima():
    #blt.open()
    blt.set('window.size=75x35')

    # FAZ COM QUE VERIFIQUE SE JA N TA TOCANDO A VERSAO FULL
    # Toca a OST adaptativa
    cfg.play_music('bgm/egotext_loop2.ogg', volume=0.8, loop=-1, crossfade_duration=10)

    logic()

def logic():
    while True:
        blt.color('black') 
        blt.bkcolor('black') 
        blt.printf(6, 0, '[color=yellow]EGOTEXT   << 101 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h[/color]')
        blt.bkcolor('#73a8d1')
        blt.printf(1, 1, """
                                                                        
                                                                        
                                                                        
                                                                        
                                       ▒▒▒▒▒▒                           
                                ▒▒     ▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒       
                              ▒▒▒▒▒    ▒▒▒▒▒▒      ▒▒▒   ▒▒▒▒▒▒▒▒       
         ▒▒▒▒        ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒     ▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▒▒▓▓▓▒▒▒     ▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▓▓▓▓▓▓▓▒     ▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▓▓ ▓ ▓▓▒     ▒▒
▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒
▒▒▒   ▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓ ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓ ▓ ▓▓▒▓▓▓▓▒▒▒
▒▒▒░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▒▓▓ ▓▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓ ▓▒▒▒▒▓▓▒▒▒▒▒▓▓ ▓ ▓ ▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▒▒▒
▒▒▒▒▓▓▓▒▒▒▒▓▓ ▓▓ ▓▓▓▓  ▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓  ▓ ▓ ▓▒▒▒▒▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▓▓ ▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
""")
        blt.printf(1, 29, '[color=white] CLIMA DE HOJE: 27° C                NUBLADO                   ↓ 8 km/h [/color]')
        blt.printf(1, 30, '[color=white] Chuva: 4%                                                 Umidade: 49% [/color]')
        blt.refresh()

        if blt.has_input():

            key = blt.read()

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

            elif key == blt.TK_S:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from pages.search import match_pages
                cfg.clear_input_queue()
                match_pages()

            elif key == blt.TK_SPACE:
                #blt.color('white')
                #blt.bkcolor('black')
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                from desktop.terminal import ego_code
                cfg.clear_input_queue()
                ego_code()

            elif key == blt.TK_ESCAPE: 
                blt.color('white')
                blt.bkcolor('black')
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                mixer.music.fadeout(1000)
                blt.refresh()     
                from desktop.desktop import terminal
                blt.clear()
                cfg.clear_input_queue()
                terminal()

            elif key == blt.TK_CLOSE:      
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                mixer.music.fadeout(1000)
                from exit_confirmation import main
                cfg.clear_input_queue()
                main()     

            elif key == blt.TK_F4:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from config import toggle_fullscreen
                cfg.clear_input_queue()
                toggle_fullscreen()

if __name__ == "__main__": 
    clima() 