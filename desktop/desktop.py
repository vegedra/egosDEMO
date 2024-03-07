from bearlibterminal import terminal as blt
import config as cfg
import language

# Animação do OS inicializando
def terminal():
    # Mostra as varíaveis do jogo e seus valores
    cfg.game_state['options_toDesktop'] = 1
    print(cfg.game_state)

    blt.set(f"window.title='egOS - Desktop'; window.size=85x35")
    blt.color('#FFB000')

    logic()
    
def logic():
    while True:
        blt.clear()
        blt.color('#FFB000')
        if cfg.game_state['current_language'] == 'en': 
            cfg.ascii_art('res/desktop/desktop_en.txt', 5, 1)
        else:
            cfg.ascii_art('res/desktop/desktop.txt', 5, 1)

        blt.print(5, 1, " ")

        # Verifica se o usuario já realizou o primeiro puzzle da Esfinge e exibe o programa do Hoobler
        if cfg.game_state['enigma_esfingeA'] == 1:
            blt.printf(59, 11, 'H')
            blt.printf(61, 11, 'Hoobler.exe')
        else:
            language.get_localized_text('desk5', section='desktop', color="#ffb000")

        # Verifica se o jogador já acessou o password.txt
        if cfg.game_state['enigma_pesquisa'] == 1:
            blt.printf(14, 12, '(S)password.txt')
        else:
            blt.printf(7, 12, ' ')

        language.get_localized_text('desk6', section='desktop', color="#ffb000")
        blt.color('#FFB000')
        if cfg.game_state['current_language'] == 'pt_BR':
            cfg.relogio(56, 33)
            blt.printf(65, 33, ">>")
        else:
           cfg.relogio(48, 33)
           blt.printf(60, 33, ">>")
        blt.refresh()

        if blt.has_input():

            key = blt.read()

            if key == blt.TK_E:
                # Abre o EgoText
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from pages.welcome import saudacao
                blt.clear()
                cfg.clear_input_queue()
                saudacao()

            #elif key == blt.TK_C:
                # Cifra de César
                #from desktop.caesar import tabela
                #blt.clear()
                #tabela() 

            elif key == blt.TK_P:
                # Pesquisa sobre o Thera-24
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from desktop.thera import pesquisa
                blt.clear()
                cfg.clear_input_queue()
                pesquisa()

            elif key == blt.TK_M:
                #Abre o manual do OS
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from desktop.manual import manual
                blt.clear()
                cfg.clear_input_queue()
                manual()

            elif key == blt.TK_H:
                # Verifica se o usuario já realizou o primeiro puzzle da Esfinge e o permite executar o Hoobler
                if cfg.game_state['enigma_esfingeA'] == 1:
                    from hoobler.intro_hoobler import first_time
                    if first_time:
                        # Primeira vez que o jogador for abrir o Hoobler
                        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                        from hoobler.intro_hoobler import intro
                        cfg.clear_input_queue()
                        intro()
                    else:
                        # Segunda vez que o jogador abrir o Hoobler
                        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                        from hoobler.hoobler1 import hoobler
                        cfg.clear_input_queue()
                        hoobler()
                else:
                    blt.clear()
                    cfg.clear_input_queue()
                    logic() 

            elif key == blt.TK_S:
                # Abre o password.txt
                if cfg.game_state['enigma_pesquisa'] == 1:
                    cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                    from desktop.password import password
                    blt.clear()
                    cfg.clear_input_queue()
                    password()
                else:
                    cfg.clear_input_queue()
                    terminal()

            elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                from desktop.terminal import ego_code
                ego_code()

            elif key == blt.TK_F4:
                from config import toggle_fullscreen
                cfg.clear_input_queue()
                toggle_fullscreen()

            elif key in (blt.TK_CLOSE, blt.TK_ESCAPE):      
                from exit_confirmation import main
                cfg.clear_input_queue()
                main()      

            else:
                blt.clear()
                cfg.clear_input_queue()
                logic() 

            cfg.clear_input_queue()
            
if __name__ == "__main__": 
    terminal() 