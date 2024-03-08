from bearlibterminal import terminal as blt
from pygame import mixer
from datetime import datetime

# Define algumas variaveis que rastream o que o jogador faz
game_state = {
    'enigma_esfingeA': 0,   # Se fez o primeiro enigma da Esfinge
    'manualEGO': 0,   # Se leu o manual
    'viu_99': 0,   # Se abriu a página 99
    'fun_factor': 0,  # Variável gerada de forma aleatória que faz cada jogatina ser diferente
    'enigma_pesquisa': 0,  # Caso o jogador tenha chegado no password.txt, desbloqueia fala com o Hoobler
    'manual_2': 0,  # Valor que define qual versão do manual o jogador verá
    'telehill': 0, # Se o jogador liberou o acesso à TeleHill
    'finaldemo': 0, # Se o jogador terminou a versão demo do jogo
    '666': 0, # Se o jogador acessou a página secreta '666'
    'find_password': 0, # O jogador precisa achar primeiro a senha para poder abrí-la
    'trato_hoobler': 0, # Se o jogador já falou sobre o Hubriston com o Hoobler
    'current_language': None,  # Defina o idioma padrão aqui - pt_BR ; en
    'options_toDesktop': 0  # Pro jogador voltar pro desktop ou menu inicial quando fecha as configuraçao
    }

is_fullscreen = False

def toggle_fullscreen():
    # Função que deixa o jogo em tela-cheia
    global is_fullscreen
    is_fullscreen = not is_fullscreen

    if is_fullscreen:
        blt.set("window: fullscreen=true")
        blt.refresh()
        
    else:
        blt.set("window: fullscreen=false")
        blt.refresh()

    blt.delay(10)
    
def clear_input_queue():
    # Clear the input queue
    while blt.has_input():
        blt.read()

def play_music(file_path, volume=0.8, loop=-1, crossfade_duration=2000):
    try:
        # If music is already playing, crossfade to the new track
        mixer.init()
        if mixer.music.get_busy():
            mixer.music.fadeout(crossfade_duration)  # Fade out the current track
            blt.delay(crossfade_duration)     # Wait for the fadeout to complete
        mixer.music.stop()
        mixer.music.load(file_path)
        mixer.music.set_volume(volume)
        mixer.music.play(loop)
    except Exception as e:
        print(repr(e))
    
def play_sound(file_path, volume=0.6, loop=-1):
    try:
        # Quase a mesma coisa que o play_music só que pra som
        mixer.init()
        sound = mixer.Sound(file_path) 
        sound.set_volume(volume)
        sound.play(loops=loop)
        return sound
    except Exception as e:
        print(repr(e))
        return None

def relogio(x, y):
    # Define as variaveis para mostrar a hora em tempo real
    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    # Muda o layout caso esteja em pt-br ou english
    if game_state['current_language'] == 'pt_BR':
        blt.print(x, y, s=f"{hour:02d}:{minute:02d}:{second:02d}")
        
    if game_state['current_language'] == 'en': 
        formatted_time = current_time.strftime("%I:%M:%S %p")
        blt.print(x, y, s=formatted_time)

def ascii_art(file_path, x, y):
    try:
        # Attempt to read the file as UTF-8
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()
            blt.printf(x, y, content)
            blt.printf(x-1, y, " ")
    except UnicodeDecodeError:
        try:
            # If UTF-8 decoding fails, try ANSI decoding
            with open(file_path, 'r', encoding="ansi") as file:
                content = file.read()
                blt.printf(x, y, content)
                blt.printf(x-1, y, " ")
        except UnicodeDecodeError:
            print("Error: Unable to decode the file. Make sure it is saved in either UTF-8 or ANSI encoding.")

def egotext_input():
    global key
    key = blt.read()

    if key == blt.TK_S:
        blt.color('white')
        blt.bkcolor('black')
        play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from pages.search import match_pages
        clear_input_queue()
        match_pages()

    elif key == blt.TK_ESCAPE:   
        play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)   
        mixer.music.fadeout(1000)
        from desktop.desktop import terminal
        blt.clear()
        clear_input_queue()
        terminal()

    elif key == blt.TK_SPACE:
        # Abre o EGO++
        blt.refresh()
        play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from desktop.terminal import ego_code
        clear_input_queue()
        ego_code()

    elif key == blt.TK_CLOSE:   
        play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)   
        mixer.music.fadeout(1000)
        from exit_confirmation import main
        clear_input_queue()
        main()   

    elif key == blt.TK_F4:
        play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from config import toggle_fullscreen
        clear_input_queue()
        toggle_fullscreen()