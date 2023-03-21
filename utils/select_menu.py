"""
The selection module
"""
import keyboard
import os
import time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def onkey_pressed (key):
    print(key)

def index_select (index, i):
    if index == i:
        return '>'
    else: return ' '

def select (options:list):
    """
    The selection menu, where 0 is Exit
    """
    index = 0
    options_all = ["Exit"] + options
    options_count = len(options_all) - 1

    while True:
        time.sleep(0.2)
        clear()
        print("Escolha uma opção:\n")
        option_values = [f'{index_select(ind, index)} {ind}: {x}' for ind, x in enumerate(options_all)]
        options_text = '\n'.join(map(str, option_values))
        print(options_text)
        key = None

        while True:
            try:
                if keyboard.is_pressed("up"):
                    key = 'up'
                    break
                if keyboard.is_pressed("down"):
                    key = 'down'
                    break
                if keyboard.is_pressed("enter"):
                    key = ''
                    break
            except:
                key = ''
                break

        if key is 'up':
            index -= 1
            if index < 0:
                index = options_count
        elif key is 'down':
            index += 1
            if index > options_count:
                index = 0
        elif key is '':
            input()
            break

    return index
