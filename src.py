#src.py
import random
import msvcrt
from banners import tiers
from terminalUI import resetScreen, cursorTUI_list
from style import pull_banner


inv = {}
global inv_open_flag
inv_open_flag = False

def pull(pull_tier=None,pulls=1):
    def pull_randomization_char(pulled_tier_local='1s'):
            pulled_char = random.choice(list(tiers[pulled_tier_local]['chars']))
            print(pull_banner(pulled_tier_local, pulled_char))

            inv[pulled_char] = inv.get(pulled_char, 0)+1

    chances = [tiers[i]['chance'] for i in tiers]
    for j in range(pulls):
        if pull_tier is None:
            pulled_tier = random.choices(list(tiers), weights=chances)[0]
        elif pull_tier in tiers:
            pulled_tier = pull_tier
        else:
            raise ValueError(f'unknown tier {pull_tier}')
        pull_randomization_char(pulled_tier)
                
                
#I used claude here to tidy up this function.
def inv_cmd():
    choice=None
    while True:
        owned_chars = list(inv)
        if not owned_chars:
            resetScreen('Inventory is empty. Press any key.')
            msvcrt.getch()
            return
    
        if choice!=None:
            choice=cursorTUI_list(owned_chars,choice)
        else:
            choice = cursorTUI_list(owned_chars)
        
        if choice is None:          # user quit the list
            return

        def find_desc(name):
            for data in tiers.values():
                if name in data['chars']:
                    return data['chars'][name]['desc']

        desc = find_desc(owned_chars[choice])
        resetScreen(desc)
        msvcrt.getch()              # wait for a key, then loop back to the list


valid_key_pull = ('p', 'pull', 'get', 'roll', 'fetch')
valid_key_inv = ('i', 'e', 'inv')

def main():
    inv_open_flag = False
    print('\033[?1049h\033[?25h', end='')   #ENTERING ALT SCREEN AND HIDING THE CURSOR 
    try:
        resetScreen()
        while True:
            user_input=input()
            if user_input == 'end':
                break

            if user_input.lower() in valid_key_pull:
                pull()

            elif user_input.lower() in valid_key_inv:
                inv_open_flag = True
                print('\033[?25l')  #hides the cursor
                inv_cmd()
                resetScreen()   #show default screen
                
        resetScreen()
    finally:
        print('\033[?1049l\033[?25h', end='')   # l = leave alt screen, h = show cursor

    
main()