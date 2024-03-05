from bearlibterminal import terminal as blt
from pygame import mixer
import language

def message(delay_time=2000):
    blt.refresh()
    blt.delay(delay_time)
    blt.puts(2, 32, " " * 70)
    blt.refresh()

def ego_code():
        # Exibe a área na qual o jogador pode digitar
        blt.puts(1, 33, " " * 70)
        blt.printf(3, 33, 'C:\>')
        rc, code = blt.read_str(7, 33, "", 74)
        code = code.lower()
        blt.refresh()

        # Comandos
        match code:
            case "open":
                language.get_localized_text('terminal1', section='terminal', color="#FFB000")
                message(delay_time=1000)
                ego_code()

            case 'open egotext.exe' | 'open egotext':
                language.get_localized_text('terminal2', section='terminal', color="#FFB000")
                message(delay_time=500)
                mixer.music.fadeout(200)
                from pages.welcome import saudacao
                blt.clear()
                saudacao()

            case "open pesquisa.txt" | 'open pesquisa' | 'open thera' | 'open research' | 'open probing' | 'open probing.txt':
                language.get_localized_text('terminal2', section='terminal', color="#FFB000")
                message(delay_time=500)
                mixer.music.fadeout(200)
                from desktop.thera import pesquisa
                blt.clear()
                pesquisa()

            case "open manual" | 'open manual' | 'help':
                language.get_localized_text('terminal2', section='terminal', color="#FFB000")
                message(delay_time=500)
                mixer.music.fadeout(200)
                from desktop.manual import manual
                blt.clear()
                manual()

            case "open hoobler.exe" | 'open hoobler':
                language.get_localized_text('terminal2', section='terminal', color="#FFB000")
                message(delay_time=500)
                import config as cfg
                if cfg.game_state['enigma_esfingeA'] == 1:
                    from hoobler.intro_hoobler import first_time
                    mixer.music.fadeout(200)
                    if first_time:
                        # Primeira vez que o jogador for abrir o Hoobler
                        from hoobler.intro_hoobler import intro
                    else:
                        # Segunda vez que o jogador abrir o Hoobler
                        from hoobler.hoobler1 import hoobler
                        hoobler()
                else:
                    language.get_localized_text('terminal4', section='terminal', color="#FFB000")
                    message(delay_time=800)
                    ego_code()
                    
            case "open password.txt" | 'open password':
                import config as cfg
                if cfg.game_state['find_password'] == 1:
                    language.get_localized_text('terminal2', section='terminal', color="#FFB000")
                    message(delay_time=500)
                    mixer.music.fadeout(200)
                    from desktop.password import password
                    blt.clear()
                    password()
                else:
                    language.get_localized_text('terminal4', section='terminal', color="#FFB000")
                    message(delay_time=800)
                    ego_code()

            case "system":
                import config as cfg
                if cfg.game_state['finaldemo'] == 1:
                    language.get_localized_text('terminal3', section='terminal', color="#FFB000")
                    message(delay_time=1000)
                    ego_code()

                elif cfg.game_state['666'] == 1:
                    language.get_localized_text('terminal5', section='terminal', color="red")
                    message(delay_time=1000)
                    from pages.djabo import djabo
                    blt.clear()
                    djabo()

                elif cfg.game_state['666'] == 0:
                    language.get_localized_text('terminal6', section='terminal', color="#FFB000")
                    message(delay_time=1000)
                    ego_code()

            case "find" | "overwrite":
                language.get_localized_text('terminal7', section='terminal', color="#FFB000")
                message(delay_time=800)
                ego_code()

            case "find password.txt":
                import config as cfg
                cfg.game_state['find_password']  = 1
                language.get_localized_text('terminal8', section='terminal', color="#FFB000")
                message(delay_time=500)
                mixer.music.fadeout(200)
                from desktop.password import password
                blt.clear()
                password()

            case "ILQG":
                language.get_localized_text('terminal9', section='terminal', color="#FFB000")
                message(delay_time=800)
                ego_code()
                
            case "overwrite pesquisa.txt password.txt" | 'overwrite pesquisa password' | "overwrite probing.txt password.txt" | 'overwrite probing password':
                language.get_localized_text('terminal10', section='terminal', color="#FFB000")
                message(delay_time=1000)
                mixer.music.fadeout(200)
                from desktop.thera2 import pesquisa
                blt.clear()
                pesquisa()

            case "close":  
                language.get_localized_text('terminal11', section='terminal', color="#FFB000")
                message(delay_time=500)
            
            case _:
                language.get_localized_text('terminal12', section='terminal', color="#FFB000")
                message(delay_time=800)