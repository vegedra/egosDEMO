from bearlibterminal import terminal as blt
from pygame import mixer
from hoobler.hoobler_core import *
import config as cfg

# Facilitar minha vida
def sair():
    global key
    key = blt.read()
    
    if key in (blt.TK_ESCAPE, blt.TK_LEFT):   
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        mixer.music.fadeout(200)
        blt.refresh()
        from desktop.desktop import terminal
        cfg.clear_input_queue()
        terminal()
        
    elif key == blt.TK_CLOSE:   
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)        
        mixer.music.fadeout(200)
        from exit_confirmation import main
        main()  

# Final do dialogo 3-1
def dialogofinal():
        blt.clear()
        blt.color('#7b7bf4')
        blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
        blt.printf(18, 0, " ")
        blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
        blt.printf(11, 6, '' + r)
        blt.printf(11, 6, " ")

        blt.printf(14, 7, '1) Sobre EgoCorp')
        blt.printf(12, 8, '║ 2) Esfinge       ║')
        blt.printf(12, 9, '║ 3) Hora          ║')

        import config as cfg
        if cfg.game_state['viu_99'] == 1:
            blt.printf(12, 10, '║ 4) Página 99     ║')
            blt.printf(12, 11, '╚══════════════════╝')
        else:
            blt.printf(12, 10, '╚══════════════════╝')

        blt.refresh()

        sair()

        if key == blt.TK_1:
            blt.clear()
            blt.printf(18, 0, normal) 
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Quem é EgoCorp e o que é egOS?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            hoobler_type("> EgoCorp é uma empresa de tecnologia", 1, 7, 70)
            hoobler_type("fundada em 1990. egOS é o sistema operacional", 1, 8, 70)
            hoobler_type("que essa máquina está usando.", 1, 9, 70)
            blt.refresh()
            blt.delay(1000)
            dialogofinal()
            
        elif key == blt.TK_2:
            blt.clear()
            blt.printf(18, 0, normal) 
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Você sabe quem é aquela Esfinge?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            hoobler_type("> Não sei dizer com precisão. Eu diria que", 1, 7, 70)
            hoobler_type("ela é uma anomalia dentro do sistema.", 1, 8, 70)
            hoobler_type("Mesmo assim, não a considero uma ameaça.", 1, 9, 70)
            blt.refresh()
            blt.delay(1000)
            dialogofinal()

        elif key == blt.TK_3:
            blt.clear()
            blt.printf(18, 0, normal) 
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Por que a hora está parada?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            hoobler_type("> Como o sistema EGOTEXT não está mais", 1, 7, 70)
            hoobler_type("funcional, a hora mostrada é a exata", 1, 8, 70)
            hoobler_type("hora em que o serviço foi terminado.", 1, 9, 70)
            blt.refresh()
            blt.delay(1000)
            dialogofinal()

        elif key == blt.TK_4:
            blt.clear()
            import config as cfg
            if cfg.game_state['enigma_pesquisa'] == 1:
                dialogo4()
            else:
                blt.printf(18, 0, normal) 
                blt.printf(18, 0, " ")
                blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
                blt.refresh()

                blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
                blt.refresh()
                player_type("Qual é a senha da página 99?", 1, 5)
                blt.delay(1000)

                blt.color('#7b7bf4')
                hoobler_type("> Acredito que a resposta para sua pergunta", 1, 7, 70)
                hoobler_type("esteja dentro do manual de sistema.", 1, 8, 70)
                blt.delay(1000)
      
                blt.delay(1000)  #ERRO 223
                dialogofinal()

        elif key == blt.TK_F4:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            from config import toggle_fullscreen
            toggle_fullscreen()
            dialogofinal()

        else:
            dialogofinal()

def manual_arruma_final():
    import config as cfg
    if cfg.game_state['manual_2'] == 1:
        blt.clear()
        blt.printf(18, 0, normal) 
        blt.printf(18, 0, " ")
        blt.print(1,3,"[color=#FFB000]Aceito, conto com você.[/color]")
        blt.refresh()

        blt.color('#7b7bf4')
        hoobler_type("> Uma ferramenta que pode lhe ser útil", 1, 5, 70)
        hoobler_type("é o EGO++. Olhe o manual da máquina.", 1, 6, 70)
        hoobler_type("> Dê uma olhada no comando FIND.", 1, 7, 70)
        blt.refresh()
        blt.delay(1000)  
        dialogofinal()

    else:
        blt.clear()
        blt.printf(18, 0, normal) 
        blt.printf(18, 0, " ")
        blt.print(1,3,"[color=#FFB000]Aceito, conto com você.[/color]")
        blt.refresh()

        blt.color('#7b7bf4')
        hoobler_type("> Uma ferramenta que pode lhe ser útil", 1, 5, 70)
        hoobler_type("é o EGO++, no manual da máquina.", 1, 6, 70)
        blt.delay(1000)
        hoobler_type("> Espere um pouco.", 1, 8, 70)
        hoobler_type("> O manual parece estar corrompido.", 1, 9, 70)
        hoobler_type("> Irei arrumar o que posso...", 1, 10, 70)
        blt.delay(1000)
        cfg.play_sound('sfx/surprise.ogg', volume=0.3, loop = 0)
        hoobler_type("> Pronto!", 1, 12, 70)
        blt.refresh()

        import config as cfg
        cfg.game_state['manual_2'] = 1

        blt.delay(1000)  #ERRO 223
        dialogofinal()

def dialogo6():
    blt.clear()
    blt.printf(18, 0, normal) 
    blt.printf(18, 0, " ")
    blt.print(1,3,"[color=#FFB000]Aceito, conto com você.[/color]")
    blt.refresh()

    blt.color('#7b7bf4')
    hoobler_type("> Bem, posso dizer que o Hubriston passava", 1, 5, 70)
    hoobler_type("muito tempo aqui, trabalhando em um ", 1, 6, 70)
    hoobler_type("projeto que parecia importante.", 1, 7, 70)

    hoobler_type("> Acredito que talvez tenha rastros", 1, 9, 70) 
    hoobler_type("desse 'projeto' no EGOTEXT.", 1, 10, 70)

    hoobler_type("> Porém, o próprio parece estar limitado à ", 1, 12, 70)
    hoobler_type("apenas algumas páginas. Acredito que a tal", 1, 13, 70)
    hoobler_type("da 'Esfinge' possa ter algo a ver com isso. ", 1, 14, 70)
    blt.refresh()
    blt.delay(1000)

    import config as cfg
    cfg.game_state['trato_hoobler'] = 1

    manual_arruma_final()

# Escolha pro trato do Hoobler
def escolha2():
    blt.clear()
    #blt.puts(18, 0, " " * 10)
    blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
    blt.printf(18, 0, " ")
    blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")

    blt.print(1, 5, "[color=#FFB000]Você sabe quem é Hubriston?[/color]")

    blt.print(1,7, "> Você aceita o trato?")

    blt.printf(11, 9, '' + r)
    blt.printf(11, 9, " ")

    blt.printf(14, 10, '1) Sim')
    blt.printf(14, 11, '2) Não')
    blt.refresh()

    sair()

    if key == blt.TK_1:
            blt.clear()
            blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")

            blt.print(1, 5, "[color=#FFB000]Você sabe quem é Hubriston?[/color]")
            blt.print(1,7, "> Você aceita o trato?")

            blt.print(1,9, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Aceito, conto com você.", 1, 9)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.puts(18, 0, " " * 10)
            blt.printf(19, 0, happy) # Mostra o rosto de Hoobler armazenado na emoção dele no momento

            hoobler_type("> Ótimo! Lembre-se de que não sou responsável", 1, 11, 70)
            blt.puts(18, 0, " " * 20)
            blt.printf(22, 0, ';)')
            hoobler_type("por quaisquer danos que possam ocorrer", 1, 12, 70)
            hoobler_type("durante sua investigação. HA HA.", 1, 13, 70)
            blt.refresh()
            blt.delay(2000)
            dialogo6()

    elif key == blt.TK_2:
            blt.clear()
            blt.printf(22, 0, ';)') # Mostra o rosto de Hoobler armazenado na emoção dele no momento
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")

            blt.print(1, 5, "[color=#FFB000]Você sabe quem é Hubriston?[/color]")

            blt.print(1,7, "> Ops, acho que você apertou errado.")
            blt.refresh()

            blt.delay(1000)
            escolha2() 

    elif key == blt.TK_F4:
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from config import toggle_fullscreen
        toggle_fullscreen()
        escolha2()

    else:
        escolha2()

# Continuação do dialogo 3-1
def dialogo5():
    blt.clear()
    blt.printf(18, 0, normal) 
    blt.printf(18, 0, " ")
    blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
    blt.print(1,5, '[color=#FFB000]Eu sou um policial.[/color]')
    hoobler_type("> Porém, posso te ajudar a navegar por esta", 1, 7, 70)
    hoobler_type("máquina e encontrar algo que lhe ajude. ", 1, 8, 70)
    blt.refresh()
    blt.delay(1000)

    blt.color('#7b7bf4')
    hoobler_type("> NO ENTANTO....", 1, 10, 70)
    hoobler_type("> Eu vou querer algo em troca:", 1, 11, 70)
    hoobler_type("> Quero que me liberte desta máquina. ", 1, 12, 70)
    hoobler_type("> Eu sei que não é mais 1996 e não quero", 1, 13, 70)
    hoobler_type("mais ficar aqui preso nesse cenotáfio.", 1, 14, 70)
    hoobler_type("> Então.......", 1, 15, 70)
    hoobler_type("> Você aceita o trato?", 1, 16, 70)
    blt.refresh()
    blt.delay(1000)
    escolha2()
    
def dialogo5_2():
    blt.clear()
    blt.printf(18, 0, normal) 
    blt.printf(18, 0, " ")
    blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
    blt.print(1,5, '[color=#FFB000]Não importa, me conte o que sabe.[/color]')
    hoobler_type("> Porém, posso te ajudar a navegar por esta", 1, 7, 70)
    hoobler_type("máquina e encontrar algo que lhe ajude. ", 1, 8, 70)
    blt.refresh()
    blt.delay(1000)

    blt.color('#7b7bf4')
    hoobler_type("> NO ENTANTO....", 1, 10, 70)
    hoobler_type("> Eu vou querer algo em troca:", 1, 11, 70)
    hoobler_type("> Quero que me liberte desta máquina. ", 1, 12, 70)
    hoobler_type("> Eu sei que não é mais 1996 e não quero", 1, 13, 70)
    hoobler_type("mais ficar aqui preso nesse cenotáfio.", 1, 14, 70)
    hoobler_type("> Então.......", 1, 15, 70)
    hoobler_type("> Você aceita o trato?", 1, 16, 70)
    blt.refresh()
    blt.delay(1000)
    escolha2()

# Arruma o manual
def manual_arruma():
    import config as cfg

    if cfg.game_state['enigma_pesquisa'] == 1:
        dialogo4()

    if cfg.game_state['manual_2'] == 1:
        blt.clear()
        blt.printf(18, 0, normal) 
        blt.printf(18, 0, " ")
        blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
        blt.refresh()
        blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
        blt.refresh()
        player_type("O que mudou no manual?", 1, 5)
        blt.delay(1000)
        blt.color('#7b7bf4')

        hoobler_type("> Veja o comando FIND.", 1, 7, 70)
        blt.refresh()
        blt.delay(1000)  
        dialogo2()

    else:
        blt.clear()
        blt.printf(18, 0, normal) 
        blt.printf(18, 0, " ")
        blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
        blt.refresh()

        blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
        blt.refresh()
        player_type("Qual é a senha da página 99?", 1, 5)
        blt.delay(1000)

        blt.color('#7b7bf4')
        hoobler_type("> Acredito que a resposta para sua pergunta", 1, 7, 70)
        hoobler_type("esteja dentro do manual de sistema.", 1, 8, 70)
        blt.delay(1000)
        hoobler_type("> Espere um pouco.", 1, 9, 70)
        hoobler_type("> O manual parece estar corrompido.", 1, 10, 70)
        hoobler_type("> Irei arrumar o que posso...", 1, 11, 70)
        blt.delay(1000)
        cfg.play_sound('sfx/surprise.ogg', volume=0.3, loop = 0)
        hoobler_type("> Pronto!", 1, 13, 70)
        blt.refresh()

        import config as cfg
        cfg.game_state['manual_2'] = 1

        blt.delay(1000)  #ERRO 223
        dialogo2()

# Se o jogador descobriu a senha da página 99
def dialogo4():
    import config as cfg
    if cfg.game_state['finaldemo'] == 1:
        blt.clear()
        blt.printf(18, 0, happy) 
        blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
        blt.refresh()

        blt.color('#7b7bf4')
        hoobler_type("> Parece que você alcançou o final.", 1, 5, 70)
        hoobler_type("> Meus parabéns!", 1, 6, 70)
        hoobler_type("> Espero que tenha gostado dessa experiência.", 1, 7, 70)
        blt.refresh()
        blt.delay(2000)  
        dialogofinal()
    else:
        blt.clear()
        blt.printf(18, 0, normal) 
        blt.printf(18, 0, " ")
        blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
        blt.refresh()

        blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
        blt.refresh()
        player_type("Eu descobri o arquivo, e agora?", 1, 5)
        blt.delay(1000)

        blt.color('#7b7bf4')
        blt.puts(18, 0, " " * 10)
        blt.printf(19, 0, happy)
        hoobler_type("> Parabéns pela sua descoberta!", 1, 7, 70)
        hoobler_type("> Acredito que seja uma cifra de livro.", 1, 8, 70)
        hoobler_type("> Tente usá-la no lugar com mais texto", 1, 9, 70)
        hoobler_type("  fora o manual no DESKTOP.", 1, 10, 70)
        hoobler_type("> Boa sorte resolvendo esse enigma!", 1, 11, 70)
        blt.refresh()
        blt.delay(1000)
    
        import config as cfg
        if cfg.game_state['enigma_pesquisa'] == 1:
            dialogofinal()
        else:
            dialogo2()

# Quem é você?
def dialogo3():
    blt.clear()
    blt.puts(18, 0, " " * 10)
    blt.printf(20, 0, confused) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
    #blt.printf(18, 0, " ")
    blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")

    blt.print(1, 5, "[color=#FFB000]Você sabe quem é Hubriston?[/color]")
    blt.print(1,7, "> Achei que fosse você...")
    blt.print(1,8, "> Quem é você?")

    blt.printf(11, 10, '' + r)
    blt.printf(11, 10, " ")

    blt.printf(14, 11, '1) Um policial')
    blt.printf(14, 12, '2) Alguém curioso')
    blt.printf(12, 13, '║ 3) Não importa   ║')
    blt.printf(12, 14, '╚══════════════════╝')
    blt.refresh()

    sair()

    if key == blt.TK_1:
            blt.clear()
            blt.printf(20, 0, confused)
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1, 5, "[color=#FFB000]Você sabe quem é Hubriston?[/color]")
            blt.print(1,7, "> Achei que fosse você...")
            blt.print(1,8, "> Quem é você?")

            blt.print(1,10, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Eu sou um policial.", 1, 10)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
            blt.printf(18, 0, " ")

            hoobler_type("> Entendo, por favor, não me prenda...", 1, 12, 70)
            hoobler_type("mas não tenho permissão de te contar.", 1, 13, 70)
            blt.refresh()
            blt.delay(1000)
            dialogo5()

    elif key == blt.TK_2:
            blt.clear()
            #blt.puts(18, 0, " " * 10)
            blt.printf(20, 0, confused)
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1, 5, "[color=#FFB000]Você sabe quem é Hubriston?[/color]")
            blt.print(1,7, "> Achei que fosse você...")
            blt.print(1,8, "> Quem é você?")

            blt.print(1,10, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Apenas alguém curioso.", 1, 10)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.printf(19, 0, cat)
            hoobler_type("> A curiosidade matou o gato, sabia?", 1, 12, 70)
            cfg.play_sound('sfx/cat.ogg', volume=0.5, loop = 0)
            blt.refresh()
            blt.delay(2000)
            dialogo3()

    elif key == blt.TK_3:
            blt.clear()
            blt.printf(20, 0, confused)
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1, 5, "[color=#FFB000]Você sabe quem é Hubriston?[/color]")
            blt.print(1,7, "> Achei que fosse você...")
            blt.print(1,8, "> Quem é você?")

            blt.print(1,10, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Não importa, me conte o que sabe.", 1, 10)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
            blt.printf(18, 0, " ")

            hoobler_type("> Por motivos de privacidade, não posso", 1, 12, 70)
            hoobler_type("te passar informações pessoais sobre o ", 1, 13, 70)
            hoobler_type("dono desta máquina.", 1, 14, 70)
            blt.refresh()
            blt.delay(1000)
            dialogo5_2()

    elif key == blt.TK_F4:
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from config import toggle_fullscreen
        toggle_fullscreen()
        dialogo3()

    else:
        dialogo3()

# Perguntas
def dialogo2():
        blt.clear()
        blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
        blt.printf(18, 0, " ")
        blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
        blt.printf(11, 6, '' + r)
        blt.printf(11, 6, " ")

        blt.printf(14, 7, '1) Sobre EgoCorp')
        blt.printf(14, 8, '2) Hubriston    ')
        blt.printf(12, 9, '║ 3) Esfinge       ║')
        blt.printf(12, 10, '║ 4) Hora          ║')

        import config as cfg
        if cfg.game_state['viu_99'] == 1:
            blt.printf(12, 11, '║ 5) Página 99     ║')
            blt.printf(12, 12, '╚══════════════════╝')
        else:
            blt.printf(12, 11, '╚══════════════════╝')

        blt.refresh()

        sair()

        if key == blt.TK_1:
            blt.clear()
            blt.printf(18, 0, normal) 
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Quem é EgoCorp e o que é egOS?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            hoobler_type("> EgoCorp é uma empresa de tecnologia", 1, 7, 70)
            hoobler_type("fundada em 1990. egOS é o sistema operacional", 1, 8, 70)
            hoobler_type("que essa máquina está usando.", 1, 9, 70)
            blt.refresh()
            blt.delay(1000)
            dialogo2()

        elif key == blt.TK_2:
            blt.clear()
            blt.printf(18, 0, normal) 
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Você sabe quem é Hubriston?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.puts(18, 0, " " * 10)
            blt.printf(20, 0, confused)
            hoobler_type("> Achei que fosse você...", 1, 7, 70)
            hoobler_type("> Quem é você?", 1, 8, 70)
            blt.refresh()
            blt.delay(1000)
            dialogo3()

        elif key == blt.TK_3:
            blt.clear()
            blt.printf(18, 0, normal) 
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Você sabe quem é aquela Esfinge?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            hoobler_type("> Não sei dizer com precisão. Eu diria que", 1, 7, 70)
            hoobler_type("ela é uma anomalia dentro do sistema.", 1, 8, 70)
            hoobler_type("Mesmo assim, não a considero uma ameaça.", 1, 9, 70)
            blt.refresh()
            blt.delay(1000)
            dialogo2()

        elif key == blt.TK_4:
            blt.clear()
            blt.printf(18, 0, normal) 
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()

            blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()
            player_type("Por que a hora está parada no EGOTEXT?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            hoobler_type("> Como o sistema EGOTEXT não está mais", 1, 7, 70)
            hoobler_type("funcional, a hora mostrada é a exata", 1, 8, 70)
            hoobler_type("hora em que o serviço foi terminado.", 1, 9, 70)
            blt.refresh()
            blt.delay(1000)
            dialogo2()

        elif key == blt.TK_5:
            blt.clear()

            import config as cfg
            if cfg.game_state['enigma_pesquisa'] == 1:
                dialogo4()
            if cfg.game_state['manual_2'] == 1:
                blt.clear()
                blt.printf(18, 0, normal) 
                blt.printf(18, 0, " ")
                blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
                blt.refresh()
                blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
                blt.refresh()
                player_type("O que mudou no manual?", 1, 5)
                blt.delay(1000)
                blt.color('#7b7bf4')
    
                hoobler_type("> Veja o comando FIND.", 1, 7, 70)
                blt.refresh()
                blt.delay(1000)  
                dialogo2()
            else:
                blt.printf(18, 0, normal) 
                blt.printf(18, 0, " ")
                blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
                blt.refresh()

                blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
                blt.refresh()
                player_type("Qual é a senha da página 99?", 1, 5)
                blt.delay(1000)

                blt.color('#7b7bf4')
                hoobler_type("> Acredito que a resposta para sua pergunta", 1, 7, 70)
                hoobler_type("esteja dentro do manual de sistema.", 1, 8, 70)
                blt.delay(1000)
                hoobler_type("> Espere um pouco.", 1, 9, 70)
                hoobler_type("> O manual parece estar corrompido.", 1, 10, 70)
                hoobler_type("> Irei arrumar o que posso...", 1, 11, 70)
                blt.delay(1000)
                cfg.play_sound('sfx/surprise.ogg', volume=0.3, loop = 0)
                hoobler_type("> Pronto!", 1, 13, 70)
                blt.refresh()

                import config as cfg
                cfg.game_state['manual_2'] = 1

                blt.delay(1000)  #ERRO 223
                dialogo2()

        elif key == blt.TK_F4:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            from config import toggle_fullscreen
            toggle_fullscreen()
            dialogo2()

        else:
            dialogo2()

# Quem é Hoobler
def escolha1():
    blt.clear()
    blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
    blt.printf(18, 0, " ")
    blt.print(1, 3,"> Olá, eu sou Hoobler, como posso te ajudar?")

    blt.print( 1, 7, "> Sou uma inteligência artificial e sirvo")
    blt.print(1, 8, "para auxiliar o dono desta máquina.")
    blt.print(1, 5, "[color=#FFB000]Olá... quem é você?[/color]")

    blt.printf(11, 10, '' + r)
    blt.printf(11, 10, " ")

    blt.printf(14, 11, '1) Auxiliar?')
    blt.refresh()

    sair()

    if key == blt.TK_1:
        blt.clear()
        blt.printf(18, 0, normal) 
        blt.printf(18, 0, " ")
        blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
        blt.refresh()

        blt.print( 1, 7, "> Sou uma inteligência artificial e sirvo")
        blt.print(1, 8, "para auxiliar o dono desta máquina.")
        blt.print(1, 5, "[color=#FFB000]Olá... quem é você?[/color]")
        blt.refresh()

        blt.print(1, 10, '[color=#303047]Comece a digitar![/color]')
        blt.refresh()
        player_type("Que tipo de auxílio?", 1, 10)

        blt.color('#7b7bf4')
        blt.delay(1000)
        blt.printf(19, 0, happy)
        hoobler_type("> Qualquer tipo. Se achar melhor, faça", 1, 12, 70)
        hoobler_type("alguma pergunta!", 1, 13, 70)
        blt.refresh()
        blt.delay(1000)
        dialogo2()

    elif key == blt.TK_F4:
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from config import toggle_fullscreen
        toggle_fullscreen()
        escolha1() 

    else:
        escolha1()

# Função principal 
def hoobler():
    blt.clear()
    blt.set(f"window.title='Hoobler'; window.size=46x15")
    global key
    
    cfg.play_music('bgm/hoobler1.ogg', volume=0.9, loop=-1, crossfade_duration=100)

    if cfg.game_state['trato_hoobler'] == 1:
        dialogofinal()
    else:
        blt.color('#7b7bf4')
        blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
        blt.printf(18, 0, " ")
        hoobler_type("> Olá, eu sou Hoobler, como posso te ajudar?", 1, 3, 70)
        blt.printf(11, 6, '' + r)
        blt.printf(11, 6, " ")
        blt.printf(14, 7, '1) Quem é você?')
        blt.printf(14, 8, '2) Perguntas')
        blt.refresh()

        sair()

        if key == blt.TK_1:
            blt.clear()
            blt.printf(18, 0, normal) 
            blt.printf(18, 0, " ")
            blt.print(1,3,"> Olá, eu sou Hoobler, como posso te ajudar?")
            blt.refresh()
            blt.print(1,5, '[color=#303047]Comece a digitar![/color]')
            blt.refresh()

            player_type("Olá... quem é você?", 1, 5)

            blt.delay(1000)
            blt.color('#7b7bf4')

            hoobler_type("> Sou uma inteligência artificial e sirvo", 1, 7, 70)
            hoobler_type("para auxiliar o dono desta máquina.", 1, 8, 70)
            blt.refresh()
            blt.delay(1000)
            escolha1()

        elif key == blt.TK_2:
            dialogo2()

        elif key == blt.TK_3:
            if cfg.game_state['manualEGO'] == 1:
                manual_arruma()
            else:
                blt.clear()
                hoobler()

        elif key == blt.TK_F4:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            from config import toggle_fullscreen
            toggle_fullscreen()
            hoobler()

        else:
            hoobler()

hoobler()