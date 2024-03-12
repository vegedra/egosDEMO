from bearlibterminal import terminal as blt
from pygame import mixer
import time
import config as cfg
import language

cfg.play_music('bgm/egotext_loop1.ogg', volume=0.8, loop=-1, crossfade_duration=10)
cfg.play_sound('bgm/computer_noise_loop.ogg', volume=0.2, loop=-1)

def saudacao():
    blt.set(f"window.title='EGOTEXT'; window.size=75x35")

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
        language.get_localized_text('welcome1', section='egotext', color="#96b4dd")
        blt.printf(3, 14, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(3, 15, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

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
        blt.printf(3, 30, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        language.get_localized_text('welcome2', section='egotext', color="#5d6f87") 
        blt.printf(3, 31, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

        language.get_localized_text('welcome3', section='egotext', color="#d6945e") 
        language.get_localized_text('welcome4', section='egotext', color="#d6945e") 
        blt.puts(1, 33, " " * 10)
        blt.refresh()

        blt.printf(3, 15, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        language.get_localized_text('welcome5', section='egotext', color="#695bd4") 
        if time.time() % frequency < frequency / 2:
          language.get_localized_text('welcome7', section='egotext', color="#5d6f87") 
          language.get_localized_text('welcome6', section='egotext', color="#695bd4") 
        blt.printf(19, 0, '100')
        blt.refresh()

        # Verifica se o usuario apertou alguma tecla e a lê
        if blt.has_input():

          cfg.egotext_input()

          if cfg.key == blt.TK_LEFT:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            blt.refresh()
            from pages.unlock_B import erroo
            blt.clear()
            cfg.clear_input_queue()
            erroo()

          elif cfg.key == blt.TK_RIGHT:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            blt.refresh()
            from pages.weather import clima
            blt.clear()
            cfg.clear_input_queue()
            clima()

if __name__ == "__main__": 
    saudacao() 