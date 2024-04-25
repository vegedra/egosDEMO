from bearlibterminal import terminal as blt
import time
from pygame import mixer

def puzzle():
    blt.set("window: size=50x30, cellsize=14x14")
    blt.color("#f2dda0")

    # Variaveis que serão usadas
    map_data = []
    player_x = 0
    player_y = 0
    start_time = time.time()
    frame_time = 1 / 30  # Set a fixed time step (30 FPS)

    # Abre o mapa por um txt e o lê
    with open("res/labirintos/map1.txt", "r") as file:
        for line in file:
            map_data.append(list(line.strip()))

    # Pega as dimensões do mapa do txt
    map_height = len(map_data)
    map_width = len(map_data[0])

    # Procura pelo '@' no mapa.txt e faz ele servir como spawn pro jogador, depois o apaga
    for y in range(map_height):
        for x in range(map_width):
            if map_data[y][x] == '@':
                player_x, player_y = x, y
                map_data[y][x] = ' '

    # Procura o '$' no mapa.txt e faz ele ser tocavel e fazer o jogo ser ganho
    point_x, point_y = None, None
    for y in range(map_height):
        for x in range(map_width):
            if map_data[y][x] == '$':
                point_x, point_y = x, y

    # Game loop
    while True:
        # Grava o tempo de início do frame
        frame_start_time = time.time()

        # Calcula o tempo restante
        remaining_time = int(15 - (time.time() - start_time))

        blt.clear()

        # Renderiza o mapa
        for y in range(map_height):
            for x in range(map_width):
                blt.put(x, y, ord(map_data[y][x]))

        # Renderiza o jogador
        blt.put(player_x, player_y, ord('@'))

        # Mostra o tempo restante
        import config as cfg
        if cfg.game_state['current_language'] == 'en': 
            blt.printf(0, map_height + 1, f"Time remaining:{remaining_time}")
        else:
            blt.printf(0, map_height + 1, f"Tempo restante:{remaining_time}")
        blt.refresh()

        # Verifica se os 15 segundos se passaram
        if time.time() - start_time > 15:
            if cfg.game_state['current_language'] == 'en': 
                blt.printf(0, map_height + 3, "[color=white]Time's Over![/color]")
            else:
                blt.printf(0, map_height + 3, "[color=white]O tempo acabou![/color]")
            blt.refresh()
            blt.delay(1000)

            # Restart the game loop
            start_time = time.time()
            continue  # This will skip the rest of the loop and start a new iteration

        # Se o jogador encostar no ponto
        if player_x == point_x and player_y == point_y:
            import config as cfg
            cfg.game_state['enigma_esfingeA'] = 1

            print(cfg.game_state['enigma_esfingeA'])

            unlock = mixer.Sound('sfx/surprise.ogg')
            unlock.play()
            unlock.set_volume(0.3)

            if cfg.game_state['current_language'] == 'en': 
                blt.printf(0, map_height + 3, "You did it!")
            else:
                blt.printf(0, map_height + 3, "Você conseguiu!")
            blt.refresh()
            blt.delay(2000)

            blt.set("window: size=50x30, cellsize=0x0")
            blt.refresh()
            
            from pages.esfinge_B import esfinge_B
            blt.clear()
            cfg.clear_input_queue()
            esfinge_B()

        # Controles que mudam a posição do jogador (@)
        if blt.has_input():
            key = blt.read()

            if key in (blt.TK_A, blt.TK_LEFT):
                if player_x > 0 and map_data[player_y][player_x - 1] != "#":
                    player_x -= 1
            elif key in (blt.TK_D, blt.TK_RIGHT):
                if player_x < map_width - 1 and map_data[player_y][player_x + 1] != "#":
                    player_x += 1
            elif key in (blt.TK_W, blt.TK_UP):
                if player_y > 0 and map_data[player_y - 1][player_x] != "#":
                    player_y -= 1
            elif key in (blt.TK_S, blt.TK_DOWN):
                if player_y < map_height - 1 and map_data[player_y + 1][player_x] != "#":
                    player_y += 1
            elif key in (blt.TK_ESCAPE, blt.TK_CLOSE):
                blt.set("window: size=50x30, cellsize=0x0")
                from exit_confirmation import main
                main()

        # Calculate the time spent in the frame
        frame_time_elapsed = time.time() - frame_start_time

        # Cap the frame rate by delaying the remaining time using delta time
        time.sleep(max(0, frame_time - frame_time_elapsed))

# TODO NOS FUTUROS PUZZLES: MAIS CORES E MAPAS MAIS COMPLEXOS
