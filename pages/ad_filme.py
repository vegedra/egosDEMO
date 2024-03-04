from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def olho():
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('#f20505') 
        cfg.ascii_art('res/egotext/olho1.txt', 5, 4)
        blt.printf(5, 4, '@')

        blt.printf(6, 0, '[color=#f0e046]EGOTEXT   << 102 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h[/color]')
        blt.printf(26, 2, '[color=#f0e046]UM FILME DE ETHAN ZACHARY[/color]')
        blt.printf(35, 32, 'O Olho')
        blt.printf(34, 33, '[color=#f0e046]Em breve...[/color]')
        blt.puts(1, 33, " " * 30)
        blt.refresh()

        if blt.has_input():
             key = blt.read()

             if key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.weather import clima
                blt.clear()
                clima()

             elif key == blt.TK_RIGHT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.ad_porn import porn
                blt.clear()
                porn()

             elif key == blt.TK_S:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)  
                from pages.search import match_pages
                match_pages()

             elif key == blt.TK_ESCAPE:      
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                from desktop.desktop import terminal
                blt.clear()
                terminal()

             elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)  
                from desktop.terminal import ego_code
                ego_code()

             elif key == blt.TK_CLOSE:      
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                from exit_confirmation import main
                main()    

             elif key == blt.TK_F4:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                from config import toggle_fullscreen
                toggle_fullscreen()

             else:
                logic()    

if __name__ == "__main__": 
    olho()