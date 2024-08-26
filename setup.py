from cx_Freeze import setup, Executable
import os

# Adicione seus caminhos para incluir arquivos necessários
include_files = [
    ('sfx', 'sfx'),
    ('res', 'res'),
    ('bgm', 'bgm'),
    ('game_text.json', '.')
] 

# Opções adicionais para cx_Freeze
build_exe_options = {
    'packages': ['pygame', 'bearlibterminal'],
    'excludes': ['tkinter'],
    'include_files': include_files,
}

exe = Executable(
    # O que construir
    script="main.py",  # o nome do seu script principal vai aqui
    base="Win32GUI",  # se estiver criando um app GUI ao invés de console, use "Win32GUI"
    target_name="egOS-Cybercrime.exe",  # este é o nome do arquivo executável
    icon="icon.ico"  # se quiser usar um arquivo de ícone, especifique o nome do arquivo aqui
)

setup(
    name="egOS-Cybercrime DEMO",
    version="1.0",
    description="Text based game",
    author="Pedro Ivo",
    options={'build_exe': build_exe_options},  # vírgula ausente corrigida aqui
    executables=[exe]
)
