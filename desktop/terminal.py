from bearlibterminal import terminal as blt
from pygame import mixer
import language
import importlib

def message(delay_time=2000):
    blt.refresh()
    blt.delay(delay_time)
    blt.puts(2, 32, " " * 70)
    blt.refresh()

def parse_command(input_code):
    """Parse the command from the user input and return the command and arguments."""
    parts = input_code.lower().strip().split(maxsplit=1)
    if parts:  # Check if parts is not empty
        command = parts[0]
        arguments = parts[1] if len(parts) > 1 else ""
    else:
        command = ""
        arguments = ""
    return command, arguments

def execute_command(command, arguments):
    """Execute the given command with its arguments."""
    if command == "open":
        handle_open(arguments)
    elif command == "system":
        handle_system()
    elif command == "find":
        handle_find(arguments)
    elif command == "overwrite":
        handle_overwrite(arguments)
    elif command == "close":
        handle_close()
    elif command == "ilqg":
        handle_ilqg()
    elif command in ["desktop", "home"]:
        handle_desktop()
    elif command == "help":
        handle_help()
    else:
        handle_unknown()

def handle_open(arg):
    """Handle the 'open' command with various arguments."""
    if arg in ["egotext.exe", "egotext"]:
        language.get_localized_text('terminal2', section='terminal', color="#FFB000")
        message(delay_time=500)
        mixer.music.fadeout(200)
        from pages.welcome import saudacao
        blt.clear()
        saudacao()
    elif arg in ["pesquisa.txt", "pesquisa", "thera", "research", "probing", "probing.txt"]:
        language.get_localized_text('terminal2', section='terminal', color="#FFB000")
        message(delay_time=500)
        mixer.music.fadeout(200)
        from desktop.thera import pesquisa
        blt.clear()
        pesquisa()
    elif arg in ["manual", "help"]:
        language.get_localized_text('terminal2', section='terminal', color="#FFB000")
        message(delay_time=500)
        mixer.music.fadeout(200)
        from desktop.manual import manual
        blt.clear()
        manual()
    elif arg in ["hoobler.exe", "hoobler"]:
        handle_hoobler()
    elif arg in ["password.txt", "password"]:
        handle_password()
    else:
        handle_unknown()

def handle_system():
    """Handle the 'system' command."""
    import config as cfg
    if cfg.game_state['finaldemo'] == 1:
        language.get_localized_text('terminal3', section='terminal', color="#FFB000")
        message(delay_time=1000)
    elif cfg.game_state['666'] == 1:
        language.get_localized_text('terminal5', section='terminal', color="red")
        message(delay_time=1000)
        # Jogador tem que procurar uma página benzedeira para tirar isso
        from pages.djabo import djabo
        blt.clear()
        djabo() 
    else:
        language.get_localized_text('terminal6', section='terminal', color="#FFB000")
        message(delay_time=1000)

def handle_find(arg):
    """Handle the 'find' command with various arguments."""
    if arg == "password.txt":
        import config as cfg
        cfg.game_state['find_password'] = 1
        language.get_localized_text('terminal8', section='terminal', color="#FFB000")
        message(delay_time=500)
        mixer.music.fadeout(200)
        from desktop.password import password
        blt.clear()
        password()
    else:
        language.get_localized_text('terminal7', section='terminal', color="#FFB000")
        message(delay_time=800)

def handle_overwrite(arg):
    """Handle the 'overwrite' command with various arguments."""
    if arg in ["pesquisa.txt password.txt", "pesquisa password", "probing.txt password.txt", "probing password"]:
        language.get_localized_text('terminal10', section='terminal', color="#FFB000")
        message(delay_time=1000)
        mixer.music.fadeout(200)
        from desktop.thera2 import pesquisa
        blt.clear()
        pesquisa()
    else:
        language.get_localized_text('terminal7', section='terminal', color="#FFB000")
        message(delay_time=800)

def handle_close():
    """Handle the 'close' command."""
    language.get_localized_text('terminal11', section='terminal', color="#FFB000")
    message(delay_time=500)

def handle_ilqg():
    """Handle the 'ilqg' command."""
    language.get_localized_text('terminal9', section='terminal', color="#FFB000")
    message(delay_time=1000)

def handle_desktop():
    """Handle the 'desktop' or 'home' command."""
    language.get_localized_text('terminal2', section='terminal', color="#FFB000")
    message(delay_time=500)
    mixer.music.fadeout(200)
    from desktop.desktop import terminal
    blt.clear()
    terminal()

def handle_help():
    """Handle the 'help' command."""
    language.get_localized_text('terminal2', section='terminal', color="#FFB000")
    message(delay_time=500)
    mixer.music.fadeout(200)
    from desktop.manual import manual
    blt.clear()
    manual()

def handle_hoobler():
    """Handle the 'hoobler' command."""
    import config as cfg
    language.get_localized_text('terminal2', section='terminal', color="#FFB000")
    message(delay_time=500)
    if cfg.game_state['enigma_esfingeA'] == 1:
        from hoobler.intro_hoobler import first_time
        mixer.music.fadeout(200)
        if first_time:
            from hoobler.intro_hoobler import intro
            intro()
        else:
            from hoobler.hoobler1 import hoobler
            hoobler()
    else:
        language.get_localized_text('terminal4', section='terminal', color="#FFB000")
        message(delay_time=1000)

def handle_password():
    """Handle the 'password' command."""
    import config as cfg
    if cfg.game_state['find_password'] == 1:
        from desktop.password import password
        blt.clear()
        password()
    else:
        handle_unknown()

def handle_unknown():
    """Handle unknown commands."""
    language.get_localized_text('terminal12', section='terminal', color="#FFB000")
    message(delay_time=800)

def ego_code():
    """Main function to read user input and execute commands."""
    # Display the area where the player can type
    blt.puts(1, 33, " " * 70)
    blt.printf(3, 33, 'C:\>')
    rc, input_code = blt.read_str(7, 33, "", 74)
    
    # Check for special keys or invalid input
    if rc == blt.TK_ESCAPE and input_code == blt.TK_ESCAPE:
        #return  # Handle ESC key press if needed, or just exit
        handle_unknown()
        return

    if not input_code.strip():
        handle_unknown()
        return

    # Parse and execute the command
    command, arguments = parse_command(input_code)
    execute_command(command, arguments)
