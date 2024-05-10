from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

# Carrega o txt contendo os rostos de Hoobler
with open('res/hoobler.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

f = open('res/hoobler_choices.txt', 'r', encoding="utf-8")
r = f.read()

# Cada linha do .txt equivale a uma emoção/rosto
normal = lines[0]
happy = lines[2]
angry = lines[4]
sad = lines[6]
confused = lines[8]
cat = lines[10]
        
def tela_escrita(player_escrita, face, escrita, x, texto):
    blt.clear()
    blt.color('#7b7bf4')
    blt.puts(18, 0, " " * 10)
    blt.printf(x, 0, face) 
    blt.printf(x, 0, " ")
            
    language.get_localized_text('hoobler3', section='hoobler1', color="#7b7bf4")
    
    if texto == 1:
        language.get_localized_text('hoobler16', section='hoobler1', color="#FFB000")
        language.get_localized_text('hoobler17', section='hoobler1', color="#7b7bf4")
        language.get_localized_text('hoobler18', section='hoobler1', color="#7b7bf4")
    else: 
        pass
    
    if player_escrita == True:
        if escrita == 1:
            # Se aparece a mensagem pro jogador digitar, se for False, não mostra
            language.get_localized_text('hoobler5', section='hoobler1', color="#303047")
        if escrita == 2:
            language.get_localized_text('hoobler10', section='hoobler1', color="#303047")
        else:
            pass
    blt.refresh()
    
# Função que faz as falas de Hoobler terem uma animação de 'typerwritter'
def hoobler_type(text, x, y, tempo):
    # Posição do texto
    cursor_x = x
    cursor_y = y
    
    # Loop que faz as letras aparecerem a cada x milisegundos
    for c in text:
        blt.print(cursor_x, cursor_y, c)
        cursor_x += 1
        blt.refresh()
        blt.delay(tempo)
        
        if blt.has_input():
            # Check for the exit key
            key = blt.read()
            if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                mixer.music.fadeout(200)
                from desktop.desktop import terminal
                cfg.clear_input_queue()
                terminal()
            cfg.clear_input_queue()

# Função que faz o jogador "escrever" a própria fala, tipo no jogo 'Emily is Away'
def player_type(message, x, y):
    global paused
    index = 0
    finished = False
    mixer.init()
    typing_sound = mixer.Sound("sfx/keyboard.ogg")

    while not finished:
        # O jogador pode escrever qualquer coisa que sairá a mensagem pré-escrita
        key = blt.read()

        # Caso o jogador aperte o botão de fechar a janela do jogo
        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            mixer.music.fadeout(200)
            from desktop.desktop import terminal
            cfg.clear_input_queue()
            terminal()

        # Caso o jogador aperte qualquer tecla
        elif key != 0 and not finished:
            blt.color('#FFB000')
            typing_sound.stop()
            typing_sound.play()
            blt.print(x, y, message[index])
            blt.refresh()
            blt.delay(100)
            index += 1
            x += 1

            # Se o jogador apertou alguma tecla o número de vezes necessário para escrever 
            # a mensagem:
            if index == len(message):
                finished = True
                return