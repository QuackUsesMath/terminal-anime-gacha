#src.py
import random
import msvcrt
from banners import tiers
from terminalUI import resetScreen, cursorTUI_list
from style import pull_banner, detail_view, multi_summary


inv = {}
global inv_open_flag
inv_open_flag = False

def pull(pull_tier=None, pulls=1):
    chances = [tiers[i]['chance'] for i in tiers]
    results = []
    for _ in range(pulls):
        if pull_tier is None:
            pulled_tier = random.choices(list(tiers), weights=chances)[0]
        elif pull_tier in tiers:
            pulled_tier = pull_tier
        else:
            raise ValueError(f'unknown tier {pull_tier}')

        pulled_char = random.choice(list(tiers[pulled_tier]['chars']))
        inv[pulled_char] = inv.get(pulled_char, 0) + 1
        results.append((pulled_tier, pulled_char))
    return results
                
                
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

        def find_rarity(name):
            for tier, data in tiers.items():
                if name in data['chars']:
                    return tier
                
        desc = find_desc(owned_chars[choice])
        frame=detail_view(find_rarity(owned_chars[choice]),owned_chars[choice],inv[owned_chars[choice]],desc=desc)
        resetScreen(frame)
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

            parts = user_input.lower().split()          # 'p 10' -> ['p', '10']
            if not parts:
                continue                                # empty input, ignore it

            cmd = parts[0]
            if cmd in valid_key_pull:
                n = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
                n = min(n, 1000000000)
                results = pull(pulls=n)

                if n == 1:
                    resetScreen(pull_banner(*results[0]))
                else:
                    resetScreen(multi_summary(results))
                print('\n\nPress any key...')
                msvcrt.getch()
                resetScreen()

            elif cmd in valid_key_inv:
                print('\033[?25l', end='')
                inv_cmd()
                print('\033[?25h', end='')
                resetScreen()
                
    finally:
        print('\033[?1049l\033[?25h', end='')   # l = leave alt screen, h = show cursor

    
main()