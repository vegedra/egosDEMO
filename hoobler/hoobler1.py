from bearlibterminal import terminal as blt
from pygame import mixer
from hoobler.hoobler_core import *
import config as cfg
import language

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
        
    elif key == blt.TK_F4:
        # Nao ta funcionando direito, tem que refatorar todo o código
        cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
        from config import toggle_fullscreen
        toggle_fullscreen()
        cfg.clear_input_queue()

def dialogo_hora():
    tela_escrita(True, normal, 1, 18, 0)
            
    if cfg.game_state['current_language'] == 'en': 
        player_type("Why is the time frozen inside EGOTEXT?", 1, 5)
    else:
        player_type("Por que a hora está parada no EGOTEXT?", 1, 5)
    blt.delay(1000)

    blt.color('#7b7bf4')
    if cfg.game_state['current_language'] == 'en': 
        hoobler_type("> As the EGOTEXT system is no longer", 1, 7, 70)
        hoobler_type("functional, the time shown is the same as", 1, 8, 70)
        hoobler_type("the one when the servers were turned off.", 1, 9, 70)
    else:
        hoobler_type("> Como o sistema EGOTEXT não está mais", 1, 7, 70)
        hoobler_type("funcional, a hora mostrada é a exata", 1, 8, 70)
        hoobler_type("hora em que o serviço foi terminado.", 1, 9, 70)
    blt.refresh()
    blt.delay(1000)
    dialogo2()

def dialogo_esfinge():
    tela_escrita(True, normal, 1, 18, 0)
            
    if cfg.game_state['current_language'] == 'en': 
        player_type("Who is the Sphinx?", 1, 5)
    else:
        player_type("Você sabe quem é aquela Esfinge?", 1, 5)
            
    blt.delay(1000)

    blt.color('#7b7bf4')
            
    if cfg.game_state['current_language'] == 'en':
        hoobler_type("> I don't know. I guess she's fine though.", 1, 7, 70)
        hoobler_type("Probably an anomaly in the system...", 1, 8, 70)
        hoobler_type("But I don't think she's a threat.", 1, 9, 70)
    else:
        hoobler_type("> Não sei dizer com precisão. Eu diria que", 1, 7, 70)
        hoobler_type("ela é uma anomalia dentro do sistema.", 1, 8, 70)
        hoobler_type("Mesmo assim, não a considero uma ameaça.", 1, 9, 70)
                
    blt.refresh()
    blt.delay(1000)
    dialogo2()

def arruma_manual():
    tela_escrita(True, normal, 1, 18, 0)
    if cfg.game_state['current_language'] == 'en': 
        player_type("What is the password on page 99?", 1, 5)
    else:
        player_type("Qual é a senha da página 99?", 1, 5)
    blt.delay(1000)

    blt.color('#7b7bf4')
    if cfg.game_state['current_language'] == 'en': 
        hoobler_type("> You should take a look at the system manual.", 1, 7, 70)
        blt.delay(1000)
        hoobler_type("> Wait a sec...", 1, 9, 70)
        hoobler_type("> It seems like the manual is corrupted.", 1, 10, 70)
        hoobler_type("> Let me fix it!", 1, 11, 70)
        blt.delay(1000)
        cfg.play_sound('sfx/surprise.ogg', volume=0.3, loop = 0)
        hoobler_type("> Done!", 1, 13, 70)
    else:
        hoobler_type("> Acredito que a resposta para sua pergunta", 1, 7, 70)
        hoobler_type("esteja dentro do manual de sistema.", 1, 8, 70)
        blt.delay(1000)
        hoobler_type("> Espere um pouco.", 1, 9, 70)
        hoobler_type("> O manual parece estar corrompido.", 1, 10, 70)
        hoobler_type("> Irei arrumar o que consigo...", 1, 11, 70)
        blt.delay(1000)
        cfg.play_sound('sfx/surprise.ogg', volume=0.3, loop = 0)
        hoobler_type("> Pronto!", 1, 13, 70)
    blt.refresh()
    
def manual_changes():
    tela_escrita(True, normal, 1, 18, 0)
            
    if cfg.game_state['current_language'] == 'en': 
        player_type("What has changed in the manual?", 1, 5)
    else:
        player_type("O que mudou no manual?", 1, 5)
    blt.delay(1000)
    blt.color('#7b7bf4')
    
    if cfg.game_state['current_language'] == 'en': 
        hoobler_type("> Take a look at the FIND command.", 1, 7, 70)
    else:
        hoobler_type("> Veja o comando FIND.", 1, 7, 70)
    blt.refresh()
    blt.delay(1000)  

def manual_arruma_final():
    import config as cfg
    blt.clear()
    blt.color('#7b7bf4')
    blt.puts(18, 0, " " * 10)
    blt.printf(18, 0, normal) 
    blt.printf(18, 0, " ")
    language.get_localized_text('hoobler29', section='hoobler1', color="#FFB000")
    blt.refresh()
    blt.color('#7b7bf4')

    if cfg.game_state['manual_2'] == 1:
        if cfg.game_state['current_language'] == 'en':
            hoobler_type("> A tool that can be useful to you is", 1, 5, 70)
            hoobler_type("the EGO++. Take a look at the machine's", 1, 6, 70)
            hoobler_type("> manual and look for the FIND command.", 1, 7, 70)
        else:
            hoobler_type("> Uma ferramenta que pode lhe ser útil", 1, 5, 70)
            hoobler_type("é o EGO++. Olhe o manual da máquina.", 1, 6, 70)
            hoobler_type("> Dê uma olhada no comando FIND.", 1, 7, 70)
        blt.refresh()
        blt.delay(1000)  
        dialogo2()

    else:
        if cfg.game_state['current_language'] == 'en':
            hoobler_type("> A tool that can be useful to you is", 1, 5, 70)
            hoobler_type("the EGO++. Look at the manual.", 1, 6, 70)
            blt.delay(1000)
            hoobler_type("> Wait a sec...", 1, 9, 70)
            hoobler_type("> It seems like the manual is corrupted.", 1, 10, 70)
            hoobler_type("> Let me fix it!", 1, 11, 70)
            blt.delay(1000)
            cfg.play_sound('sfx/surprise.ogg', volume=0.3, loop = 0)
            hoobler_type("> Done!", 1, 13, 70)
        else:
            hoobler_type("> Uma ferramenta que pode lhe ser útil", 1, 5, 70)
            hoobler_type("é o EGO++. Olhe o manual da máquina.", 1, 6, 70)
            blt.delay(1000)
            hoobler_type("> Espere um pouco.", 1, 8, 70)
            hoobler_type("> O manual parece estar corrompido.", 1, 9, 70)
            hoobler_type("> Irei arrumar o que consigo...", 1, 10, 70)
            blt.delay(1000)
            cfg.play_sound('sfx/surprise.ogg', volume=0.3, loop = 0)
            hoobler_type("> Pronto!", 1, 12, 70)
            blt.refresh()

        import config as cfg
        cfg.game_state['manual_2'] = 1

        blt.delay(1000)  #ERRO 223
        dialogo2()

def dialogo6():
    import config as cfg
    blt.clear()
    blt.color('#7b7bf4')
    blt.puts(18, 0, " " * 10)
    blt.printf(18, 0, normal) 
    blt.printf(18, 0, " ")
    language.get_localized_text('hoobler29', section='hoobler1', color="#FFB000")
    blt.refresh()
    blt.color('#7b7bf4')

    if cfg.game_state['current_language'] == 'en':
        hoobler_type("> Well, Hubriston spent a lot of time here", 1, 5, 70)
        hoobler_type("working in a project that seemed important.", 1, 6, 70)

        hoobler_type("> I believe it may have traces left of this", 1, 9, 70) 
        hoobler_type("'project' on EGOTEXT.", 1, 10, 70)

        hoobler_type("> But it seems like it's limited, only", 1, 12, 70)
        hoobler_type("having some pages. I believe that's", 1, 13, 70)
        hoobler_type("Sphinx doing. ", 1, 14, 70)
    else:
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
    cfg.game_state['hoobler_menu'] = 1
    cfg.game_state['trato_hoobler'] = 1

    manual_arruma_final()

# Escolha pro trato do Hoobler
def escolha2():
    tela_escrita(False, normal, 0, 18, 2)

    blt.printf(11, 9, '' + r)
    blt.printf(11, 9, " ")

    language.get_localized_text('hoobler23', section='hoobler1', color="#7b7bf4")
    language.get_localized_text('hoobler24', section='hoobler1', color="#7b7bf4")
    blt.refresh()

    sair()

    if key == blt.TK_1:
            tela_escrita(True, normal, 0, 18, 2)

            language.get_localized_text('hoobler27', section='hoobler1', color="#303047")
            blt.refresh()
            if cfg.game_state['current_language'] == 'en':
                player_type("I accept, I'm counting on you.", 1, 9)
            else:
                player_type("Aceito, conto com você.", 1, 9)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.puts(18, 0, " " * 10)
            blt.printf(19, 0, happy) # Mostra o rosto de Hoobler armazenado na emoção dele no momento

            if cfg.game_state['current_language'] == 'en':
                hoobler_type("> Great! Just a reminder:", 1, 11, 70)
            else:
                hoobler_type("> Ótimo! Lembre-se de que não sou responsável", 1, 11, 70)
            blt.puts(18, 0, " " * 20)
            blt.printf(22, 0, ';)')
            if cfg.game_state['current_language'] == 'en':
                hoobler_type("I'm not responsible for any damages caused.", 1, 12, 70)
            else:
                hoobler_type("por quaisquer danos que possam ocorrer", 1, 12, 70)
                hoobler_type("durante sua investigação. HA HA.", 1, 13, 70)
            blt.refresh()
            blt.delay(2000)
            dialogo6()

    elif key == blt.TK_2:
            blt.clear()
            blt.printf(22, 0, ';)') # Mostra o rosto de Hoobler armazenado na emoção dele no momento
            language.get_localized_text('hoobler3', section='hoobler1', color="#7b7bf4")

            language.get_localized_text('hoobler16', section='hoobler1', color="#FFB000")

            language.get_localized_text('hoobler28', section='hoobler1', color="#7b7bf4")
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

# Continuação do dialogo 3-1 -- TODO: JUNTA COM O DIALOGO 5_2 DEPOIS
def dialogo5():
    tela_escrita(False, normal, 0, 18, 0)
    language.get_localized_text('hoobler25', section='hoobler1', color="#FFB000")
    blt.color('#7b7bf4')
    if cfg.game_state['current_language'] == 'en':
        hoobler_type("> However, I can help you navigate this", 1, 7, 70)
        hoobler_type("machine and find something that can help you.", 1, 8, 70)
    else:
        hoobler_type("> Porém, posso te ajudar a navegar por esta", 1, 7, 70)
        hoobler_type("máquina e encontrar algo que lhe ajude. ", 1, 8, 70)
    blt.refresh()
    blt.delay(1000)

    blt.color('#7b7bf4')
    if cfg.game_state['current_language'] == 'en':
        hoobler_type("> BUT....", 1, 10, 70)
        hoobler_type("> I'm going to want something in return:", 1, 11, 70)
        hoobler_type("> I want you to free me from this machine. ", 1, 12, 70)
        hoobler_type("> I know it's not 1996 anymore and I don't want to", 1, 13, 70)
        hoobler_type("stay locked in here.", 1, 14, 70)
        blt.delay(500)
        hoobler_type("> So.......", 1, 15, 70)
        hoobler_type("> Do you accept the deal?", 1, 16, 70)
    else:
        hoobler_type("> NO ENTANTO....", 1, 10, 70)
        hoobler_type("> Eu vou querer algo em troca:", 1, 11, 70)
        hoobler_type("> Quero que me liberte desta máquina. ", 1, 12, 70)
        hoobler_type("> Eu sei que não é mais 1996 e não quero", 1, 13, 70)
        hoobler_type("ficar preso nesse cenotáfio.", 1, 14, 70)
        hoobler_type("> Então.......", 1, 15, 70)
        hoobler_type("> Você aceita o trato?", 1, 16, 70)
    blt.refresh()
    blt.delay(1000)
    escolha2()
    
def dialogo5_2():
    tela_escrita(False, normal, 0, 18, 0)
    language.get_localized_text('hoobler26', section='hoobler1', color="#FFB000")
    blt.color('#7b7bf4')
    if cfg.game_state['current_language'] == 'en':
        hoobler_type("> However, I can help you navigate this", 1, 7, 70)
        hoobler_type("machine and find something that can help you.", 1, 8, 70)
    else:
        hoobler_type("> Porém, posso te ajudar a navegar por esta", 1, 7, 70)
        hoobler_type("máquina e encontrar algo que lhe ajude. ", 1, 8, 70)
    blt.refresh()
    blt.delay(1000)

    blt.color('#7b7bf4')
    if cfg.game_state['current_language'] == 'en':
        hoobler_type("> BUT....", 1, 10, 70)
        hoobler_type("> I'm going to want something in return:", 1, 11, 70)
        hoobler_type("> I want you to free me from this machine. ", 1, 12, 70)
        hoobler_type("> I know it's not 1996 anymore and I don't", 1, 13, 70)
        hoobler_type("want to stay locked in here.", 1, 14, 70)
        blt.delay(500)
        hoobler_type("> So.......", 1, 15, 70)
        hoobler_type("> Do you accept the deal?", 1, 16, 70)
    else:
        hoobler_type("> NO ENTANTO....", 1, 10, 70)
        hoobler_type("> Eu vou querer algo em troca:", 1, 11, 70)
        hoobler_type("> Quero que me liberte desta máquina. ", 1, 12, 70)
        hoobler_type("> Eu sei que não é mais 1996 e não quero", 1, 13, 70)
        hoobler_type("ficar preso nesse cenotáfio.", 1, 14, 70)
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
        manual_changes()
        dialogo2()

    else:
        arruma_manual()

        import config as cfg
        cfg.game_state['manual_2'] = 1

        blt.delay(1000)  #ERRO 223
        dialogo2()

# Se o jogador descobriu a senha da página 99
def dialogo4():
    import config as cfg
    if cfg.game_state['finaldemo'] == 1:
        tela_escrita(False, happy, 0, 18, 1)

        blt.color('#7b7bf4')
        if cfg.game_state['current_language'] == 'en':
            hoobler_type("> Seems like you reached the end.", 1, 5, 70)
            hoobler_type("> Congratulations!", 1, 6, 70)
            hoobler_type("> I hope you liked the game.", 1, 7, 70)
        else:
            hoobler_type("> Parece que você alcançou o final.", 1, 5, 70)
            hoobler_type("> Meus parabéns!", 1, 6, 70)
            hoobler_type("> Espero que tenha gostado dessa experiência.", 1, 7, 70)
        blt.refresh()
        blt.delay(2000)  
        dialogo2()
    else:
        tela_escrita(True, normal, 1, 18, 0)
        if cfg.game_state['current_language'] == 'en':
            player_type("I've found the file, what I do now?", 1, 5)
        else:
            player_type("Eu descobri o arquivo, e agora?", 1, 5)
        blt.delay(1000)

        blt.color('#7b7bf4')
        blt.puts(18, 0, " " * 10)
        blt.printf(19, 0, happy)
        if cfg.game_state['current_language'] == 'en':
            hoobler_type("> Good work finding it.", 1, 7, 70)
            hoobler_type("> I think it's a book cipher.", 1, 8, 70)
            hoobler_type("> Try using it on a file with a lot of", 1, 9, 70)
            hoobler_type("  text, beside the manual.", 1, 10, 70)
        else:
            hoobler_type("> Parabéns pela sua descoberta!", 1, 7, 70)
            hoobler_type("> Acredito que seja uma cifra de livro.", 1, 8, 70)
            hoobler_type("> Tente usá-la no lugar com mais texto", 1, 9, 70)
            hoobler_type("  fora o manual no DESKTOP.", 1, 10, 70)
            hoobler_type("> Boa sorte resolvendo esse enigma!", 1, 11, 70)
        blt.refresh()
        blt.delay(1000)
    
        import config as cfg
        if cfg.game_state['enigma_pesquisa'] == 1:
            dialogo2()
        else:
            dialogo2()

# Quem é você?
def dialogo3():
    blt.clear()
    tela_escrita(False, confused, 0, 20, 1)

    blt.printf(11, 10, '' + r)
    blt.printf(11, 10, " ")

    language.get_localized_text('hoobler19', section='hoobler1', color="#7b7bf4")
    language.get_localized_text('hoobler20', section='hoobler1', color="#7b7bf4")
    language.get_localized_text('hoobler21', section='hoobler1', color="#7b7bf4")
    blt.printf(12, 14, '╚══════════════════╝')
    blt.refresh()

    sair()

    if key == blt.TK_1:
            tela_escrita(True, confused, 2, 20, 1)

            if cfg.game_state['current_language'] == 'en':
                player_type("I'm from the police.", 1, 10)
            else:
                player_type("Eu sou um policial.", 1, 10)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
            blt.printf(18, 0, " ")

            if cfg.game_state['current_language'] == 'en':
                hoobler_type("> Oh, ok... don't arrest me, but", 1, 12, 70)
                hoobler_type("I can't tell you.", 1, 13, 70)
            else: 
                hoobler_type("> Entendo, por favor, não me prenda...", 1, 12, 70)
                hoobler_type("mas não tenho permissão de te contar.", 1, 13, 70)
            blt.refresh()
            blt.delay(1000)
            dialogo5()

    elif key == blt.TK_2:
            tela_escrita(True, confused, 2, 20, 1)

            if cfg.game_state['current_language'] == 'en':
                player_type("Just curious.", 1, 10)
            else:
                player_type("Apenas alguém curioso.", 1, 10)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.printf(19, 0, cat)
            if cfg.game_state['current_language'] == 'en':
                hoobler_type("> Did you know that curiosity killed", 1, 12, 70)
                hoobler_type("the cat?", 1, 13, 70)
            else:
                hoobler_type("> A curiosidade matou o gato, sabia?", 1, 12, 70)
            cfg.play_sound('sfx/cat.ogg', volume=0.5, loop = 0)
            blt.refresh()
            blt.delay(2000)
            dialogo3()

    elif key == blt.TK_3:
            tela_escrita(True, confused, 2, 20, 1)

            if cfg.game_state['current_language'] == 'en':
                player_type("It doesn't matter, tell me what you know.", 1, 10)
            else: 
                player_type("Não importa, me conte o que sabe.", 1, 10)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
            blt.printf(18, 0, " ")

            if cfg.game_state['current_language'] == 'en':
                hoobler_type("> For privacy reasons, I cannot tell you", 1, 12, 70)
                hoobler_type("personal information from the machine's", 1, 13, 70)
                hoobler_type("owner.", 1, 14, 70)
            else:
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
        import config as cfg
        tela_escrita(False, normal, 0, 18, 0)
        blt.printf(11, 6, '' + r)
        blt.printf(11, 6, " ")

        language.get_localized_text('hoobler11', section='hoobler1', color="#7b7bf4")
        if cfg.game_state['hoobler_menu'] == 0: 
            language.get_localized_text('hoobler12', section='hoobler1', color="#7b7bf4")
            language.get_localized_text('hoobler13', section='hoobler1', color="#7b7bf4")
            language.get_localized_text('hoobler14', section='hoobler1', color="#7b7bf4")
        else:
            language.get_localized_text('hoobler31', section='hoobler1', color="#7b7bf4")
            language.get_localized_text('hoobler32', section='hoobler1', color="#7b7bf4")

        import config as cfg
        if cfg.game_state['hoobler_menu'] == 1: 
            language.get_localized_text('hoobler30', section='hoobler1', color="#7b7bf4")
            blt.printf(12, 11, '╚══════════════════╝')

        if cfg.game_state['viu_99'] == 1:
            if cfg.game_state['hoobler_menu'] == 1: 
                language.get_localized_text('hoobler30', section='hoobler1', color="#7b7bf4")
                blt.printf(12, 11, '╚══════════════════╝')
            else:
                language.get_localized_text('hoobler15', section='hoobler1', color="#7b7bf4")
                blt.printf(12, 12, '╚══════════════════╝')
        else:
            blt.printf(12, 11, '╚══════════════════╝')

        blt.refresh()

        sair()

        if key == blt.TK_1:
            tela_escrita(True, normal, 1, 18, 0)
            
            if cfg.game_state['current_language'] == 'en': 
                player_type("What is EgoCorp and egOS?", 1, 5)
            else:
                player_type("Quem é EgoCorp e o que é egOS?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            
            if cfg.game_state['current_language'] == 'en': 
                hoobler_type("> EgoCorp it's an technology company founded", 1, 7, 70)
                hoobler_type("in 1990. egOS it's the Operating System that", 1, 8, 70)
                hoobler_type("this machine is running.", 1, 9, 70)
            else:
                hoobler_type("> EgoCorp é uma empresa de tecnologia", 1, 7, 70)
                hoobler_type("fundada em 1990. egOS é o sistema operacional", 1, 8, 70)
                hoobler_type("que essa máquina está usando.", 1, 9, 70)
            
            blt.refresh()
            blt.delay(1000)
            dialogo2()

        elif key == blt.TK_2:
          if cfg.game_state['hoobler_menu'] == 1: 
            dialogo_esfinge()
          else:
            tela_escrita(True, normal, 1, 18, 0)
            
            if cfg.game_state['current_language'] == 'en': 
                player_type("Who is Hubriston?", 1, 5)
            else:
                player_type("Você sabe quem é Hubriston?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            blt.puts(18, 0, " " * 10)
            blt.printf(20, 0, confused)
            
            if cfg.game_state['current_language'] == 'en': 
                hoobler_type("> Isn't that you?", 1, 7, 70)
                hoobler_type("> Who are YOU?", 1, 8, 70)
            else:
                hoobler_type("> Achei que fosse você...", 1, 7, 70)
                hoobler_type("> Quem é você?", 1, 8, 70)
            
            blt.refresh()
            blt.delay(1000)
            dialogo3()

        elif key == blt.TK_3:
          if cfg.game_state['hoobler_menu'] == 1: 
            dialogo_hora()
          else:
            tela_escrita(True, normal, 1, 18, 0)
            
            if cfg.game_state['current_language'] == 'en': 
                player_type("Who is the Sphinx?", 1, 5)
            else:
                player_type("Você sabe quem é aquela Esfinge?", 1, 5)
            
            blt.delay(1000)

            blt.color('#7b7bf4')
            
            if cfg.game_state['current_language'] == 'en':
                hoobler_type("> I don't know. I guess she's fine though.", 1, 7, 70)
                hoobler_type("Probably an anomaly in the system, you know...", 1, 8, 70)
                hoobler_type("But I don't think she's a threat.", 1, 9, 70)
            else:
                hoobler_type("> Não sei dizer com precisão. Eu diria que", 1, 7, 70)
                hoobler_type("ela é uma anomalia dentro do sistema.", 1, 8, 70)
                hoobler_type("Mesmo assim, não a considero uma ameaça.", 1, 9, 70)
                
            blt.refresh()
            blt.delay(1000)
            dialogo2()

        elif key == blt.TK_4:
            tela_escrita(True, normal, 1, 18, 0)
            
            if cfg.game_state['current_language'] == 'en': 
                player_type("Why is the time frozen inside EGOTEXT?", 1, 5)
            else:
                player_type("Por que a hora está parada no EGOTEXT?", 1, 5)
            blt.delay(1000)

            blt.color('#7b7bf4')
            if cfg.game_state['current_language'] == 'en': 
                hoobler_type("> As the EGOTEXT system is no longer functional,", 1, 7, 70)
                hoobler_type("the time shown is the same as the one when the", 1, 8, 70)
                hoobler_type("servers were turned off.", 1, 9, 70)
            else:
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
                manual_changes()
                dialogo2()
            else:
                arruma_manual()

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
    tela_escrita(False, normal, 0, 18, 0)
    
    blt.printf(11, 10, '' + r)
    blt.printf(11, 10, " ")
        
    language.get_localized_text('hoobler6', section='hoobler1', color="#7b7bf4")
    language.get_localized_text('hoobler7', section='hoobler1', color="#7b7bf4")
    
    language.get_localized_text('hoobler8', section='hoobler1', color="#FFB000")

    blt.color('#7b7bf4')

    language.get_localized_text('hoobler9', section='hoobler1', color="#7b7bf4")
    blt.refresh()

    sair()

    if key == blt.TK_1:
        # x, y e largura e altura do retangulo apagador
        blt.clear_area(1, 10, 50, 6)

        language.get_localized_text('hoobler10', section='hoobler1', color="#303047")
        blt.refresh()
        
        if cfg.game_state['current_language'] == 'en': 
            player_type("What kind of 'help'?", 1, 10)
        else:
            player_type("Que tipo de auxílio?", 1, 10)

        blt.color('#7b7bf4')
        blt.delay(1000)
        
        if cfg.game_state['current_language'] == 'en': 
            hoobler_type("> Any type, I guess.", 1, 12, 90)
            blt.delay(500)
            blt.printf(19, 0, happy)
            hoobler_type("> Ask me something!", 1, 13, 70)
        else:
            blt.printf(19, 0, happy)
            hoobler_type("> Qualquer tipo! Se achar melhor, faça", 1, 12, 75)
            hoobler_type("alguma pergunta.", 1, 13, 75)
            
        blt.refresh()
        blt.delay(1500)
        dialogo2()

    else:
        escolha1()

# Função principal 
def hoobler():
    blt.clear()
    blt.set(f"window.title='Hoobler'; window.size=46x15")
    
    cfg.play_music('bgm/hoobler1.ogg', volume=0.9, loop=-1, crossfade_duration=100)

    if cfg.game_state['trato_hoobler'] == 1:
        dialogo2()
    else:
        blt.color('#7b7bf4')
        blt.printf(18, 0, normal) # Mostra o rosto de Hoobler armazenado na emoção dele no momento
        blt.printf(18, 0, " ")
        
        if cfg.game_state['current_language'] == 'en': 
            hoobler_type("> Hello, I'm Hoobler, how can I help you?", 1, 3, 70)
        else:
            hoobler_type("> Olá, eu sou Hoobler, como posso te ajudar?", 1, 3, 70)
        
        blt.printf(11, 6, '' + r)
        blt.printf(11, 6, " ")
        language.get_localized_text('hoobler1', section='hoobler1', color="#7b7bf4")
        language.get_localized_text('hoobler2', section='hoobler1', color="#7b7bf4")
        blt.refresh()

        sair()

        if key == blt.TK_1:
            tela_escrita(True, normal, 1, 18, 0)

            if cfg.game_state['current_language'] == 'en': 
                player_type("Hi... who are you?", 1, 5)
            else:
                player_type("Olá... quem é você?", 1, 5)

            blt.delay(1000)
            blt.color('#7b7bf4')

            if cfg.game_state['current_language'] == 'en': 
                hoobler_type("> I'm an A.I. Assistant and my", 1, 7, 65)
                hoobler_type("duty is to help this machine's owner.", 1, 8, 65)
            else:
                hoobler_type("> Sou uma inteligência artificial e sirvo", 1, 7, 65)
                hoobler_type("para auxiliar o dono desta máquina.", 1, 8, 65)
                
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
        else:
            hoobler()

hoobler()