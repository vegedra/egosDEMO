from bearlibterminal import terminal as blt
import random
import language
from pygame import mixer
import config as cfg
from howtoplay import sair as sair

def os():
    blt.set(f"window.title='egOS - Login'; window.size=85x35")
    blt.clear()
     
    # Som de computador antigo
    cfg.play_sound('bgm/computer_noise_loop.ogg', volume=0.4, loop=-1)
    
    # Resetando o valor das variavel no config pra um new game
    cfg.game_state['enigma_esfingeA'] = 0
    cfg.game_state['manualEGO'] = 0
    cfg.game_state['viu_99'] = 0
    cfg.game_state['fun_factor'] = 0
    cfg.game_state['enigma_pesquisa'] = 0
    cfg.game_state['manual_2'] = 0
    cfg.game_state['telehill'] = 0
    cfg.game_state['finaldemo'] = 0
    cfg.game_state['666'] = 0
    cfg.game_state['find_password'] = 0
    cfg.game_state['trato_hoobler'] = 0
    cfg.game_state['options_toDesktop'] = 0

    # Código que gera o valor Fun Factor
    fun_factor_random = random.randint(1, 5)
    cfg.game_state['fun_factor'] = fun_factor_random
    print(f"Fun Factor Gerado: {cfg.game_state['fun_factor']}")

    language.get_localized_text('desk1', section='desktop', color="#ffb000")
    language.get_localized_text('desk2', section='desktop', color="#ffb000")
    blt.refresh()
    sair()
    blt.delay(1500)
    language.get_localized_text('login9', section='login', color="#ffb000")
    blt.refresh()
    sair()
    blt.delay(1500)
    language.get_localized_text('login10', section='login', color="#ffb000")
    blt.refresh()
    sair()
    blt.delay(500)
    cfg.play_sound('sfx/sound_menu_open.ogg', volume=0.5, loop = 0)
    cfg.ascii_art('res/logo_egocorp.txt', 22, 8)
    blt.printf(62, 8, '®️')
    blt.printf(63, 8, " ")
    blt.refresh()
    sair()
    blt.delay(2500)
    cfg.clear_input_queue()

    login()

def login():
    while True:
        blt.clear()
        language.get_localized_text('login1', section='login', color="#FFB000")

        # Define as variaveis para mostrar a hora em tempo real
        if cfg.game_state['current_language'] == 'pt_BR':
            cfg.relogio(38, 1)
        else:
           cfg.relogio(37, 1)
        
        blt.printf(0, 5, """

                     __gggrgM**M#mggg__
                __wgNN@"B*P""mp""@d#"@N#Nw__
              _g#@0F_a*F#  _*F9m_ ,F9*__9NG#g_
           _mN#F  aM"    #p"    !q@    9NL "9#Qu_
          g#MF _pP"L  _g@"9L_  _g""#__  g"9w_ 0N#p
        _0F jL*"   7_wF     #_gF     9gjF   "bJ  9h_
       j#  gAF    _@NL     _g@#_      J@u_    2#_  #_
      ,FF_#" 9_ _#"  "b_  g@   "hg  _#"  !q_ jF "*_09_
      F N"    #p"      Ng@       `#g"      "w@    "# t
     j p#    g"9_     g@"9_      gP"#_     gF"q    Pb L
     0J  k _@   9g_ j#"   "b_  j#"   "b_ _d"   q_ g  ##
     #F  `NF     "#g"       "Md"       5N#      9W"  j#
     #k  jFb_    g@"q_     _*"9m_     _*"R_    _#Np  J#
     tApjF  9g  J"   9M_ _m"    9%_ _*"   "#  gF  9_jNF
      k`N    "q#       9g@        #gF       ##"    #"j
      `_0q_   #"q_    _&"9p_    _g"`L_    _*"#   jAF,'
       9# "b_j   "b_ g"    *g _gF    9_ g#"  "L_*"qNF
        "b_ "#_    "NL      _B#      _I@     j#" _#"
          NM_0"*g_ j""9u_  gP  q_  _w@ ]_ _g*"F_g@
           "NNh_ !w#_   9#g"    "m*"   _#*" _dN@"
              9##g_0@q__ #"4_  j*"k __*NF_g#@P"
                "9NN#gIPNL_ "b@" _2M"Lg#N@F"
                    ""P@*NN#gEZgNN@#@P""
""")
        language.get_localized_text('login2', section='login', color="#FFB000")
        blt.refresh()

        if blt.has_input():
           logic() 
    
def logic():
    while True:
        blt.color('#FFB000')
        key = blt.read()

        if key == blt.TK_ENTER:
            language.get_localized_text('login3', section='login', color="#FFB000")
            language.get_localized_text('login4', section='login', color="#FFB000")
            language.get_localized_text('login5', section='login', color="#FFB000")

            # Jogador deve colocar o login e senha certa
            rc, username = blt.read_str(69, 13, "", 9)
            blt.printf(69, 13, "" + username)
            username = username.lower()

            if cfg.game_state['current_language'] == 'pt_BR':
                rc, password = blt.read_str(69, 14, "", 4)
                blt.printf(69, 14, "" + password)
        
            if cfg.game_state['current_language'] == 'en': 
                rc, password = blt.read_str(72, 14, "", 4)
                blt.printf(72, 14, "" + password)

            # Se acertou: 
            if username == "hubriston" and (password == "1104" or password == "0411"):
                language.get_localized_text('login6', section='login', color="#FFB000")
                blt.refresh()
                blt.delay(1000)
                blt.clear()
                blt.refresh()
                blt.delay(800)
                blt.clear()
                blt.refresh()
                blt.delay(500)
                cfg.clear_input_queue()
                from desktop.desktop import terminal
                terminal()

            # Se errou:
            else:
                language.get_localized_text('login7', section='login', color="#FFB000")
                language.get_localized_text('login8', section='login', color="#FFB000")
                blt.refresh()
                blt.delay(2000)
                login()

        elif key == blt.TK_F4:
            cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
            from config import toggle_fullscreen
            toggle_fullscreen()

        elif key in (blt.TK_CLOSE, blt.TK_ESCAPE):  
            mixer.stop()
            cfg.play_music('bgm/menu.ogg', volume=0.6, loop=-1, crossfade_duration=2000)
            from main import main_menu
            main_menu()

        cfg.clear_input_queue()

if __name__ == "__main__": 
    login() 