from bearlibterminal import terminal as blt
from pygame import mixer

def esfinge_B():
    #blt.open()
    blt.set("window: size=75x35, cellsize=0x0")
    
    mixer.music.unpause()

    logic()

def logic():
    while True:
        import config as cfg
        blt.color('#ffdc73') 
        language.get_localized_text('welcome5', section='egotext', color="#ffdc73") 
        blt.printf(20, 0, '105')

        cfg.ascii_art('res/egotext/esfinge_rosto.txt', 12, 6)
    
        language.get_localized_text('esfinge_b1', section='egotext', color="#ffdc73") 
        blt.puts(1, 33, " " * 70)
        blt.refresh()

        if blt.has_input():
            cfg.egotext_input()

            if cfg.key == blt.TK_ENTER:
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
                from desktop.desktop import terminal
                blt.clear()
                terminal()

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
                    esfinge_B()

            else:
                blt.clear()
                esfinge_B()

if __name__ == "__main__": 
    esfinge_B() 