from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

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
        blt.printf(6, 0, 'EGOTEXT   << 105 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')
        blt.printf(14, 4, 'Eu sou a esfinge, me diga qual o clima de hoje.')
        import config as cfg
        cfg.ascii_art('res/egotext/esfinge.txt', 12, 6)
        blt.printf(12, 6, ' ')

        blt.printf(22, 26, 'Pressione Enter para digitar')
        blt.puts(1, 33, " " * 70)
        blt.refresh()

        if blt.has_input():
            key = blt.read()

            if key == blt.TK_ENTER:
                blt.print(22, 27, "> ")
                rc, clima = blt.read_str(23, 27, "", 20)

                # Resposta certa para o enigma
                if clima == "27":
                    blt.puts(24, 26, " " * 50)
                    blt.refresh()
                    blt.clear()
                    cfg.ascii_art('res/egotext/esfinge.txt', 12, 6)

                    blt.printf(5, 26, 'Muito bem. Agora atravesse meu labirinto antes que o tempo acabe!')
                    blt.printf(18, 27, 'Use as setas do teclado para tocar no $.')
                    blt.printf(18, 28, 'Pressione Enter para iniciar o desafio.')
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
                    blt.printf(28, 26, 'ERRADO! ERRADO!')
                    blt.refresh()
                    blt.delay(1500)
                    blt.clear()
                    esfinge_A()

            elif key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.art_face import art
                blt.clear()
                art()

            elif key == blt.TK_RIGHT:
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

            elif key == blt.TK_S:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)  
                from pages.search import match_pages
                match_pages()

            elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)  
                from desktop.terminal import ego_code
                ego_code()

            elif key == blt.TK_ESCAPE:      
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)  
                from desktop.desktop import terminal
                blt.clear()
                terminal()

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
    esfinge_A() 