from bearlibterminal import terminal as blt
import sys
import config as cfg
import language

def main():
    blt.set(f"window.title='egOS'; window.size=40x21")
    blt.clear()
    blt.color('#8b9dc3')
    blt.bkcolor('black')

    blt.printf(8, 1,  "        _________        ")
    blt.printf(8, 2,  "       / ======= \       ")
    blt.printf(8, 3,  "      / __________\      ")
    blt.printf(8, 4,  "     |  _________  |     ")
    blt.printf(8, 5,  "     | |         | |     ")
    blt.printf(8, 6,  "     | |    :(   | |     ")
    blt.printf(8, 7,  "     | |_________| |     ")
    blt.printf(8, 8,  "     \=____________/     ")
    blt.printf(8, 9,  "     / ''''''''''''\     ")
    blt.printf(8, 10,  "    / ::::::::::::: \   ")
    blt.printf(8, 11,  "   (_________________)  ")
               
    language.get_localized_text('exit1', section='exit', color="#7b7bf4")
    language.get_localized_text('exit2', section='exit', color="#7b7bf4")
    language.get_localized_text('exit3', section='exit', color="#7b7bf4")
    language.get_localized_text('exit4', section='exit', color="#7b7bf4")
    language.get_localized_text('exit5', section='exit', color="#7b7bf4")
    blt.refresh()

    logic()

def logic():
    key = blt.read()

    if key in (blt.TK_CLOSE, blt.TK_4):      
        sys.exit()

    elif key in (blt.TK_ESCAPE, blt.TK_1): 
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        blt.refresh()
        from desktop.desktop import terminal
        terminal()

    elif key == blt.TK_F4:
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from config import toggle_fullscreen
        toggle_fullscreen()
        # Volta pra tela de confirmar saída por causa de um bug
        main()
        
        from main import main_menu
        main_menu()

    elif key == blt.TK_2:    
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from main import main_menu
        main_menu()
        
    elif key == blt.TK_3:
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        blt.clear()
        from options import options
        options()

    else: 
        main()
        
    cfg.clear_input_queue()

if __name__ == '__main__':
    main()