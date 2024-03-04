from bearlibterminal import terminal as blt
from pygame import mixer
import time
import config as cfg

def saudacao():
    blt.set(f"window.title='EGOTEXT'; window.size=75x35")
    #mixer.music.rewind()
    cfg.play_music('bgm/egotext_loop1.ogg', volume=0.8, loop=-1, crossfade_duration=10)

    logic()

def logic():
      frequency = 2

      while True:
        # COLOQUE O TEXTO E ARTE NO WHILE TRUE PARA NÃO BUGAR O EGO++
        blt.bkcolor('black')
    
        blt.printf(3, 2, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 3, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 4, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 5, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

        blt.printf(3, 6, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 7, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 8, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 9, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 10, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

        blt.printf(3, 11, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 12, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 13, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉ BEM-VINDO(A) AO EGOTEXT ▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 14, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    

        blt.printf(3, 16, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 17, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 18, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 19, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 20, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

        blt.printf(3, 21, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 22, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 23, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 24, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 25, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

        blt.printf(3, 26, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 27, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 28, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 29, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 30, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉ PRESSIONE ESC PARA VOLTAR AO DESKTOP! ▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 31, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

        blt.color('#d6945e')
        blt.print(15, 33, "<--- USE AS SETAS DO TECLADO PARA NAVEGAR ---> ")
        blt.print(12, 34, "APERTE 'S' PARA PESQUISAR POR UMA PÁGINA ESPECÍFICA ")
        blt.puts(1, 33, " " * 10)
        blt.refresh()


        blt.printf(3, 15, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(6, 0, '[color=#695bd4]EGOTEXT   << 100 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h[/color]')
        if time.time() % frequency < frequency / 2:
          blt.color('#5d6f87')
          blt.printf(3, 15, "[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉ TE DEIXANDO ATUALIZADO(A) BYTE A BYTE ▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]")
          blt.printf(6, 0, "[color=#695bd4]EGOTEXT   << 100 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:14h[/color]")
        blt.refresh()

        # Verifica se o usuario apertou alguma tecla e a lê
        if blt.has_input():

          key = blt.read()

          if key == blt.TK_LEFT:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            blt.refresh()
            from pages.unlock_B import erroo
            blt.clear()
            cfg.clear_input_queue()
            erroo()

          elif key == blt.TK_RIGHT:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            blt.refresh()
            from pages.weather import clima
            blt.clear()
            cfg.clear_input_queue()
            clima()

          elif key == blt.TK_S:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            from pages.search import match_pages
            cfg.clear_input_queue()
            match_pages()

          elif key == blt.TK_ESCAPE:   
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)   
            mixer.music.fadeout(1000)
            from desktop.desktop import terminal
            blt.clear()
            cfg.clear_input_queue()
            terminal()

          elif key == blt.TK_SPACE:
            # Abre o EGO++
            blt.refresh()
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            from desktop.terminal import ego_code
            cfg.clear_input_queue()
            ego_code()

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
    saudacao() 