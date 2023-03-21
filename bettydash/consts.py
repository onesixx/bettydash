import os
import sys

MENU_ITEMS = None


def get_menu_items(folder_path):
    global MENU_ITEMS
    if MENU_ITEMS is None:
        menu_item_global = []
        for entry in os.listdir(folder_path):
            if os.path.isdir(os.path.join(folder_path, entry)) and entry[0] != '_':
                menu_item_global.append(entry)
        MENU_ITEMS = menu_item_global
    return MENU_ITEMS


folder_path = os.path.join(
    os.path.dirname(os.path.abspath(os.path.dirname(__file__))),
    'bettyboard', 'pages')
MENU_ITEMS = get_menu_items(folder_path)
print(f'print MENU_ITEMS from bettydash.consts ==> {MENU_ITEMS}')
