from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def esfinge_A():
    #blt.open()
    blt.set("window: size=75x35, cellsize=0x0")

    if cfg.game_state['enigma_esfingeA'] == 0:
        logic() 

    else:
        from pages.esfinge_B import esfinge_B
        blt.clear()
        esfinge_B()

def logic():
    while True:
        blt.color('#ffdc73') 
        language.get_localized_text('welcome5', section='egotext', color="#ffdc73") 
        blt.printf(19, 0, '105')
        language.get_localized_text('esfinge_a1', section='egotext', color="#ffdc73") 
        import config as cfg
        cfg.ascii_art('res/egotext/esfinge.txt', 12, 6, False)
        blt.printf(12, 6, ' ')

        language.get_localized_text('esfinge_a2', section='egotext', color="#ffdc73") 
        blt.puts(1, 33, " " * 70)
        blt.refresh()

        if blt.has_input():
            cfg.egotext_input()

            if cfg.key == blt.TK_ENTER:
                blt.print(22, 27, "> ")
                rc, clima = blt.read_str(23, 27, "", 20)

                # Resposta certa para o enigma
                if clima == "27" or clima == "80":
                    blt.puts(24, 26, " " * 50)
                    blt.refresh()
                    blt.clear()
                    cfg.ascii_art('res/egotext/esfinge.txt', 12, 6, True)

                    language.get_localized_text('esfinge_a3', section='egotext', color="#ffdc73") 
                    language.get_localized_text('esfinge_a4', section='egotext', color="#ffdc73") 
                    language.get_localized_text('esfinge_a5', section='egotext', color="#ffdc73") 
                    blt.refresh()

                    # Ignora qualquer input q n seja ENTER
                    key = None

                    while key != blt.TK_ENTER:
                        key = blt.read()
                
                    cfg.play_music('bgm/egotext_minigame.ogg', volume=0.8, loop=-1, crossfade_duration=100)
                    from pages.minigame import puzzle
                    blt.clear()
                    puzzle()

                # Resposta errada para o enigma
                else:
                    blt.puts(22, 26, " " * 50)
                    language.get_localized_text('esfinge_a6', section='egotext', color="#ffdc73") 
                    blt.refresh()
                    blt.delay(1500)
                    blt.clear()
                    esfinge_A()

            elif cfg.key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.art_face import art
                blt.clear()
                art()

            elif cfg.key == blt.TK_RIGHT:
                import config as cfg
                if cfg.game_state['finaldemo'] == 1:
                    cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                    blt.color('white')
                    blt.bkcolor('black')
                    blt.refresh()
                    from pages.esfinge_C import esfinge_C
                    blt.clear()
                    esfinge_C()
                else:
                    esfinge_A()

            else:
                logic()  

if __name__ == "__main__": 
    esfinge_A() 