from bearlibterminal import terminal as blt
from pygame import mixer
from intro import intro
import config as cfg
import random
import sys
import language

# Abre o blt e o configura: se pode ser arrastado, o titulo da janela e de onde vem o input
blt.open()
blt.set("""
    window.resizeable=false;
    window.title='egOS - Cybercrime';
    input: filter={keyboard};
""")
blt.set('window.size=85x35')

while True:
    # Definição de idioma
    blt.print(36, 16, '1) Português')
    blt.print(36, 17, '2) English')
    blt.refresh()

    key = blt.read()

    if key == blt.TK_1:
        cfg.game_state['current_language'] = 'pt_BR'
        print(cfg.game_state['current_language'])
        break  # Exit the loop if a valid key is pressed

    elif key == blt.TK_2:
        cfg.game_state['current_language'] = 'en'
        print(cfg.game_state['current_language'])
        break  # Exit the loop if a valid key is pressed

    elif key in (blt.TK_CLOSE, blt.TK_ESCAPE):     
        sys.exit()

    blt.clear()
    blt.refresh()
        
    # Limpa a fila de input
    cfg.clear_input_queue()

#TIRA O # QUANDO FOR EXPORTAR!!!!! V V V 
#intro()

# Musica usando o Mixer do Pygame
cfg.play_music('bgm/menu.ogg', volume=0.6, loop=-1, crossfade_duration=2000)

def main_menu():
    blt.set("""
    window.resizeable=false;
    window.title='egOS - Cybercrime';
    input: filter={keyboard};
""")
    blt.set('window.size=85x35')
    blt.clear()
    blt.refresh()
    blt.bkcolor('#FFB000')
    blt.color('#fff4e6')

    # Pega a arte do arquivo .txt e printa na tela
    cfg.ascii_art('res/novo_menu.txt', 32, 3)
    # Vai ter que colocar esse print caso tenha caractere ANSI
    blt.printf(32, 3, " ")
    
    blt.print(50,19, '[COLOR:(#6fcb9f]--            --[/COLOR]')
    blt.print(56,21, '[COLOR:(#6fcb9f]DEMO[/COLOR]')
    blt.refresh()
    
    # Menu de escolhas
    blt.bkcolor('black')
    language.get_localized_text('menu1', section='menu')
    language.get_localized_text('menu2', section='menu')
    language.get_localized_text('menu3', section='menu', color="#ffb000")
    language.get_localized_text('menu4', section='menu', color="#fff4e6")
    language.get_localized_text('menu5', section='menu', color="#fff4e6")
    language.get_localized_text('menu6', section='menu', color="#fff4e6")
    language.get_localized_text('menu7', section='menu', color="#fff4e6")
    language.get_localized_text('menu8', section='menu', color="#fff4e6")
    blt.refresh()

    logic()
    
def logic():
    text = "CYBERCRIME"

    while True:
        # Embaralha as letras
        text = list(text)  # Converte para uma lista de caracteres
        random.shuffle(text)  # Embaralha os caracteres
        text = "".join(text)  # Os converte devolta para uma string

        # Revela uma letra por vez
        for i in range(len(text)):
            blt.color('white')
            blt.bkcolor('#FFB000')
            blt.put(53 + i, 19, text[i])  
            blt.refresh()
            blt.delay(50)  

        if blt.has_input():
            # Lê qual tecla o usuario apertou
            key = blt.read()
            blt.bkcolor('black')

            if key == blt.TK_1:
                # Animação de fade out na tela - frame 1
                blt.clear()
                blt.color('gray')
                cfg.play_sound('sfx/sfx_tvOn.ogg', volume=0.5, loop = 0)
                    
                if cfg.game_state['current_language'] == 'en': 
                    cfg.ascii_art('res/menuFADE_en.txt', 1, 1)
                else:
                    cfg.ascii_art('res/menuFADE.txt', 1, 1)
                
                blt.print(1, 1, " ")
                blt.print(1, 1, " ")
                blt.refresh()
                blt.delay(1000)

                # Frame 2
                blt.clear()
                blt.color('#171717')

                if cfg.game_state['current_language'] == 'en': 
                    cfg.ascii_art('res/menuFADE_en.txt', 1, 1)
                else:
                    cfg.ascii_art('res/menuFADE.txt', 1, 1)

                blt.print(1, 1, " ")
                blt.refresh()
                blt.delay(1000)

                # Frame 3
                blt.clear()
                blt.refresh()
                from desktop.OS import os
                mixer.music.fadeout(1000)
                cfg.clear_input_queue()
                os()

            # Cutscene de como jogar o jogo
            elif key == blt.TK_2:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.clear()
                from howtoplay import tutorial
                tutorial()

            # Os créditos
            elif key == blt.TK_3:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.clear()
                from credits import credits
                credits()

            # Configurações
            elif key == blt.TK_4:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.clear()
                from options import options
                options()

            # Ativar a tela-cheia
            elif key == blt.TK_F4:
                cfg.toggle_fullscreen()

            # DEBUG - REMOVE DEPOIS
            elif key == blt.TK_8:
                cfg.clear_input_queue()
                from desktop.desktop import terminal
                terminal()

            # Sair
            elif key in (blt.TK_CLOSE, blt.TK_5, blt.TK_ESCAPE):     
                sys.exit()

            # Caso aperte alguma tecla que não devia
            else:
                cfg.clear_input_queue()
                main_menu()

            cfg.clear_input_queue()

if __name__ == "__main__": 
    main_menu()