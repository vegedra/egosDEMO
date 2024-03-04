from bearlibterminal import terminal as blt
import config as cfg

def match_pages():
    blt.color('#d6945e')

    # Area que o jogador pode inserir a página que deseja ir
    blt.print(1, 34, "> ")
    rc, pag = blt.read_str(2, 34, "", 3)
    blt.refresh()

    match pag:
        case "007":
            from pages.bond import jamesbond
            blt.clear()
            cfg.clear_input_queue()
            jamesbond()

        case "42":
            from pages.Hitchhiker import resposta
            blt.clear()
            cfg.clear_input_queue()
            resposta()
            
        case "69":
            from pages.sixtynine import meianove
            blt.clear()
            cfg.clear_input_queue()
            meianove()
            
        case "98":
            from pages.gflex import gflex
            blt.clear()
            cfg.clear_input_queue()
            gflex()
            
        case "99":
            from pages.unlock_B import erroo
            blt.clear()
            cfg.clear_input_queue()
            erroo()

        case "100":
            blt.color('white')
            blt.bkcolor('black')
            blt.refresh()
            from pages.welcome import saudacao
            blt.clear()
            cfg.clear_input_queue()
            saudacao()

        case "101":
            blt.color('white')
            blt.bkcolor('black')
            blt.refresh()
            from pages.weather import clima
            blt.clear()
            cfg.clear_input_queue()
            clima()

        case "102":
            blt.color('white')
            blt.bkcolor('black')
            blt.refresh()
            from pages.ad_filme import olho
            blt.clear()
            cfg.clear_input_queue()
            olho()

        case "103":
            blt.color('white')
            blt.bkcolor('black')
            blt.refresh()
            from pages.ad_porn import porn
            blt.clear()
            cfg.clear_input_queue()
            porn()

        case "104":
            blt.color('white')
            blt.bkcolor('black')
            blt.refresh()
            from pages.art_face import art
            blt.clear()
            cfg.clear_input_queue()
            art()

        case "105":
            blt.color('white')
            blt.bkcolor('black')
            blt.refresh()
            from pages.esfinge_A import esfinge_A
            blt.clear()
            cfg.clear_input_queue()
            esfinge_A()           
                
               
        case "106":
            import config as cfg
            if cfg.game_state['finaldemo'] == 1:
                blt.color('white')
                blt.bkcolor('black')
                blt.refresh()
                from pages.esfinge_C import esfinge_C
                blt.clear()
                cfg.clear_input_queue()
                esfinge_C()  
            else:
                from pages.error import erro
                blt.clear()
                cfg.clear_input_queue()
                erro()

        case "505":
            from pages.a_monkeys import arctic
            blt.clear()
            cfg.clear_input_queue()
            arctic() 

        case "666":
            from pages.djabo import djabo
            blt.clear()
            cfg.clear_input_queue()
            djabo() 
            
        case "777":
            import config as cfg
            if cfg.game_state['finaldemo'] == 1:
                from pages.troll import troll
                blt.clear()
                cfg.clear_input_queue()
                troll() 
            else:
                from pages.error import erro
                blt.clear()
                cfg.clear_input_queue()
                erro()
            
        case "999":
            from pages.unknown import espaco
            blt.clear()
            cfg.clear_input_queue()
            espaco() 

        case _:
            from pages.error import erro
            blt.clear()
            cfg.clear_input_queue()
            erro()

match_pages()