from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

def porn():
    #blt.open()
    blt.set('window.size=75x35')

    logic()

def logic():
    while True:
        blt.color('pink') 
        cfg.ascii_art('res/egotext/dama.txt', 1, 5)
        blt.printf(1, 5, ' ')

        blt.color('yellow')
        cfg.ascii_art('res/egotext/dama_tel.txt', 14, 27)
        blt.printf(14, 27, ' ')

        blt.color('pink') 
        blt.printf(6, 0, 'EGOTEXT   << 103 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')
        blt.printf(5, 6, 'MULHERES NUAS (E SEM ROUPAS!)')
        blt.printf(5, 9, 'Saia do computador e')
        blt.printf(5, 10, "venha 'curtir'!")
        blt.printf(5, 12, 'AVISO: NÃO MORDA OU ARRANHE AS')
        blt.printf(5, 13, 'GAROTAS!')
        blt.puts(1, 33, " " * 70)
        blt.refresh()

        if blt.has_input():
             key = blt.read()

             if key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.ad_filme import olho
                blt.clear()
                olho()

             elif key == blt.TK_RIGHT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.art_face import art
                blt.clear()
                art()

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
    porn()