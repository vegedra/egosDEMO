from bearlibterminal import terminal as blt
import config as cfg
import json

# Carrega as traduções no JSON
with open('game_text.json', 'r', encoding='utf-8') as file:
    translations_data = json.load(file)

def get_localized_text(key, section=None, color="white"):
    current_language = cfg.game_state['current_language']
    current_language = current_language or 'en'

    # Pega o texto localizado ou dá uma mensagem de erro
    text_entry = translations_data.get('sections', {}).get(current_language, {}).get(section, {}).get(key, {'text': f'Sem tradução: {key}', 'x': 0, 'y': 0, 'color': color})

    # Pega a cor escolhida ou uma padrão caso não seja especificado
    entry_color = text_entry.get('color', color)
    # Coloca a cor
    blt.color(entry_color)
    # Coloca o texto nas coordenadas dadas
    blt.puts(text_entry['x'], text_entry['y'], text_entry['text'])