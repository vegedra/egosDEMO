from bearlibterminal import terminal as blt
import config as cfg

def clear_and_execute(function):
    blt.clear()
    cfg.clear_input_queue()
    function()

def match_pages():
    blt.color('#d6945e')

    # Area que o jogador pode inserir a página que deseja ir
    blt.print(1, 34, "> ")
    rc, pag = blt.read_str(2, 34, "", 3)
    blt.refresh()

    pages = {
        "007": lambda: clear_and_execute(__import__('pages.bond', fromlist=['']).jamesbond),
        "42": lambda: clear_and_execute(__import__('pages.Hitchhiker', fromlist=['']).resposta),
        "69": lambda: clear_and_execute(__import__('pages.sixtynine', fromlist=['']).meianove),
        "98": lambda: clear_and_execute(__import__('pages.gflex', fromlist=['']).gflex),
        "99": lambda: clear_and_execute(__import__('pages.unlock_B', fromlist=['']).erroo),
        "100": lambda: (blt.color('white'), blt.bkcolor('black'), blt.refresh(), clear_and_execute(__import__('pages.welcome', fromlist=['']).saudacao)),
        "101": lambda: (blt.color('white'), blt.bkcolor('black'), blt.refresh(), clear_and_execute(__import__('pages.weather', fromlist=['']).clima)),
        "102": lambda: (blt.color('white'), blt.bkcolor('black'), blt.refresh(), clear_and_execute(__import__('pages.ad_filme', fromlist=['']).olho)),
        "103": lambda: (blt.color('white'), blt.bkcolor('black'), blt.refresh(), clear_and_execute(__import__('pages.ad_porn', fromlist=['']).porn)),
        "104": lambda: (blt.color('white'), blt.bkcolor('black'), blt.refresh(), clear_and_execute(__import__('pages.art_face', fromlist=['']).art)),
        "105": lambda: (blt.color('white'), blt.bkcolor('black'), blt.refresh(), clear_and_execute(__import__('pages.esfinge_A', fromlist=['']).esfinge_A)),
        "106": lambda: (
            blt.color('white'), blt.bkcolor('black'), blt.refresh(), 
            clear_and_execute(__import__('pages.esfinge_C', fromlist=['']).esfinge_C) if cfg.game_state['finaldemo'] == 1 else clear_and_execute(__import__('pages.error', fromlist=['']).erro)
        ),
        "505": lambda: clear_and_execute(__import__('pages.a_monkeys', fromlist=['']).arctic),
        "666": lambda: clear_and_execute(__import__('pages.djabo', fromlist=['']).djabo),
        "777": lambda: (
            clear_and_execute(__import__('pages.troll', fromlist=['']).troll) if cfg.game_state['finaldemo'] == 1 else clear_and_execute(__import__('pages.error', fromlist=['']).erro)
        ),
        "999": lambda: clear_and_execute(__import__('pages.unknown', fromlist=['']).espaco)
    }

    # Get the handler function from the dictionary, default to an error handler
    handler = pages.get(pag, lambda: clear_and_execute(__import__('pages.error', fromlist=['']).erro))
    try:
        handler()
    except Exception as e:
        lambda: clear_and_execute(__import__('pages.error', fromlist=['']).erro)

match_pages()
