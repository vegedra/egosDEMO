from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg

first_time = 1

def intro():
    global first_time
    #blt.open()
    blt.set(f"window.title='Hoobler'; window.size=50x20")
    blt.color('#7b7bf4')
    mixer.music.fadeout(200)

    # Essa animação deve tocar apenas uma vez durante todo o jogo
    if first_time:

        # Valores para a barra de carregamento
        total = 48
        current = 0

        # Toca o som tema da EgoCorp
        cfg.play_sound('sfx/jingle.ogg', volume=0.7, loop = 0)

        # Animação da barra de loading com o logo da Relicorp em um .txt
        while current <= total:
            blt.clear()
            cfg.ascii_art('res/logo_egocorp.txt', 4, 1)
            blt.printf(44, 1, '®️')
            blt.printf(45, 1, " ")

            # Preenche a barra de carregamento
            for i in range(current):
                blt.print(1+i, 10, "█")
            blt.refresh()

            current += 1
            blt.delay(50)

        first_time = 0

        while True:
            blt.delay(500)
            if cfg.game_state['current_language'] == 'en': 
                blt.print(14, 15, "STARTING HOOBLER.EXE")
            else:
                blt.print(12, 15, "INICIALIZANDO HOOBLER.EXE")
            blt.refresh()
            blt.delay(2000)
            from hoobler.hoobler1 import hoobler
            blt.delay(100)
            cfg.clear_input_queue()

        else:
            intro()

    blt.clear()
    from hoobler.hoobler1 import hoobler
    cfg.clear_input_queue()
    hoobler()
    
intro()

