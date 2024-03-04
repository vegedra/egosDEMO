from bearlibterminal import terminal as blt
from datetime import datetime
from pygame import mixer

def tabela():
    #blt.open()
    blt.set(f"window.title='egOS - Cifra'; window.size=85x35") 
    blt.color('#FFB000')

    logic()

def logic():
    while True:
        # Define as variaveis para mostrar a hora em tempo real
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        blt.clear()

        f = open('res/desktop/caesar_tab.txt', 'r', encoding="utf-8")
        r = f.read()
        blt.printf(16, 2, '' + r)
        blt.print(16, 2, " ")
        blt.print(2, 33, '<- VOLTAR')

        # Mostra a hora em tempo real
        blt.printf(18, 1, '<< SEGUNDA-FEIRA - 11 DE ABRIL, 1996 /')
        blt.print(57, 1, s=f"{hour:02d}:{minute:02d}:{second:02d} >>")

        blt.refresh()

        if blt.has_input():

            key = blt.read()

            if key == blt.TK_SPACE:
                # Abre o EGO++
                blt.refresh()
                from desktop.terminal import ego_code
                ego_code()

            elif key == blt.TK_F4:
                from config import toggle_fullscreen
                toggle_fullscreen()

            elif key in (blt.TK_CLOSE, blt.TK_ESCAPE, blt.TK_LEFT):    
                    sfx = mixer.Sound('sfx/sound_menu_close.ogg') 
                    sfx.play()
                    sfx.set_volume(0.5)
                    blt.refresh()
                    from desktop.desktop import terminal
                    blt.clear()
                    terminal()

if __name__ == "__main__": 
    tabela() 