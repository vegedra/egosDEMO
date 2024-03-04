from bearlibterminal import terminal as blt
import config as cfg
import language

def manual():
    #blt.open()
    blt.color('#FFB000')

    # Verifica que o usuario abriu o manual
    import config as cfg
    cfg.game_state['manualEGO'] = 1

    # Verifica se o jogador deve acessar o manual original ou o modificado
    if cfg.game_state['manual_2'] == 1:
        # Hoobler arrumou o manual
        import config as cfg
        cfg.game_state['manual_2'] = 1
        logic2()
    else:
        # Hoobler ainda não arrumou o manual
        logic()

def logic():
    while True:
        blt.set(f"window.title='egOS - Manual'; window.size=85x35") 
        blt.clear()

        if cfg.game_state['current_language'] == 'en': 
            cfg.ascii_art('res/desktop/manual1_en.txt', 3, 4)
        else:
            cfg.ascii_art('res/desktop/manual1.txt', 3, 4)
        blt.print(3, 4, " ")

        language.get_localized_text('manual1', section='manual', color="#ffb000")
        language.get_localized_text('manual2', section='manual', color="#ffb000")
        language.get_localized_text('manual3', section='manual', color="#ffb000")

        if cfg.game_state['current_language'] == 'pt_BR':
            cfg.relogio(57, 1)
            blt.printf(66, 1, ">>")
        else:
           cfg.relogio(48, 1)
           blt.printf(60, 1, ">>")
        blt.refresh()

        if blt.has_input():

            key = blt.read()

            if key == blt.TK_RIGHT:
                # Segunda página
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                blt.clear()
                cfg.clear_input_queue()
                page2()

            elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                from desktop.terminal import ego_code
                ego_code()
            
            elif key == blt.TK_F4:
                cfg.clear_input_queue()
                from config import toggle_fullscreen
                toggle_fullscreen()

            elif key in (blt.TK_CLOSE, blt.TK_ESCAPE, blt.TK_LEFT):    
                    cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                    blt.refresh()
                    from desktop.desktop import terminal
                    blt.clear()
                    cfg.clear_input_queue()
                    terminal()

def page2():
    while True:
        blt.set(f"window.title='egOS - ?'; window.size=85x35") 
        blt.clear()

        blt.printf(3, 4,  
"""             01110011 00111011 00001010 00001010 01010101 01001110 
             01010011 01000101 01010100 00100000 00101101 00100000    
             01000100 01100101 01110011 01100110 01100001 01111010 
             00100000 01100001 01110011 00100000 01101101 01110101 
             01100100 01100001 01101110 11100111 01100001 01110011 
             00100000 01100110 01100101 01101001 01110100 01100001 
             01110011 00100000 01110000 01100101 01101100 01101111 
             00100000 11111010 01101100 01110100 01101001 01101101 
             01101111 00100000 01100011 01101111 01101101 01100001 
             01101110 01100100 01101111 00100000 01010011 01000101 
             01010100 00100000 01100101 01110011 01100011 01110010 
             01101001 01110100 01101111 00101110 

""")
        language.get_localized_text('manual1', section='manual', color="#ffb000")
        language.get_localized_text('manual3', section='manual', color="#ffb000")
        if cfg.game_state['current_language'] == 'pt_BR':
            cfg.relogio(57, 1)
            blt.printf(66, 1, ">>")
        else:
           cfg.relogio(48, 1)
           blt.printf(60, 1, ">>")
        blt.refresh()
        blt.refresh()

        if blt.has_input():

            key = blt.read()

            if key == blt.TK_LEFT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                blt.clear()
                cfg.clear_input_queue()
                manual()

            elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                from desktop.terminal import ego_code
                ego_code()

            elif key == blt.TK_F4:
                cfg.clear_input_queue()
                from config import toggle_fullscreen
                toggle_fullscreen()

            elif key in (blt.TK_CLOSE, blt.TK_ESCAPE):    
                    cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                    blt.refresh()
                    from desktop.desktop import terminal
                    blt.clear()
                    cfg.clear_input_queue()
                    terminal() 

def logic2():
    while True:
        blt.set(f"window.title='egOS - Manual'; window.size=85x35") 
        blt.clear()

        if cfg.game_state['current_language'] == 'en': 
            cfg.ascii_art('res/desktop/manual2_en.txt', 3, 4)
        else:
            cfg.ascii_art('res/desktop/manual2.txt', 3, 4)
        blt.print(3, 4, " ")

        language.get_localized_text('manual1', section='manual', color="#ffb000")
        language.get_localized_text('manual2', section='manual', color="#ffb000")
        language.get_localized_text('manual3', section='manual', color="#ffb000")

        if cfg.game_state['current_language'] == 'pt_BR':
            cfg.relogio(57, 1)
            blt.printf(66, 1, ">>")
        else:
           cfg.relogio(48, 1)
           blt.printf(60, 1, ">>")
        blt.refresh()

        if blt.has_input():

            key = blt.read()

            if key == blt.TK_RIGHT:
                # Segunda página
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                blt.clear()
                cfg.clear_input_queue()
                page2()

            elif key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                from desktop.terminal import ego_code
                ego_code()

            elif key == blt.TK_F4:
                cfg.clear_input_queue()
                from config import toggle_fullscreen
                toggle_fullscreen()

            elif key in (blt.TK_CLOSE, blt.TK_ESCAPE, blt.TK_LEFT):    
                    cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                    blt.refresh()
                    from desktop.desktop import terminal
                    blt.clear()
                    cfg.clear_input_queue()
                    terminal()

if __name__ == "__main__": 
    manual() 