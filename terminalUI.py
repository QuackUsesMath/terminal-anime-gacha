#terminalUI.py
import msvcrt
import os

num = [*range(0,10)]
bull=0
#print(*l, sep='\n')

def resetScreen(print_text='Enter Command (h for help): '):
    
    frame = '\033[H' #wipe everything

    frame+=print_text

    frame+='\033[J'     #wipe leftovers
    print(frame,end='',flush=True)      #update

    


def cursorTUI_list(l,cursor_position=0):
    cursor = '•>'
    initPos = cursor_position
    length = len(l)

    def draw(selected=0):
        frame = '\033[H'
        for i,item in enumerate(l):
            prefix = cursor if i == selected else '  '
            frame+=f'{prefix}{item}\033[K\n'
        frame+='\033[J'
        #frame+=f'\ncount = {initPos}\nselected = {selected}'
        print(frame,end='',flush=True)
        #print(f's = {s}')

    #print('\033[?1049h\033[?25l', end='')      NOT REQUIRED HERE  
    draw(cursor_position)
    while True:
        if length!=0:
            initPos%=length
        key = msvcrt.getch()

        if key == b'\x03':
            break
        elif key == b'\xe0':
            key = msvcrt.getch()
            match(key):
                case b'P':
                    initPos+=1
                    if length!=0:
                        initPos%=length
                    draw(initPos)
                case b'H':
                    initPos-=1
                    if length!=0:
                        initPos%=length
                    draw(initPos)
        elif key == b'\r':
            return initPos
        elif key==b'\x03' or b'q':
            return None
    #return initPos
       # print('\033[?1049l\033[?25h', end='')   # l = leave alt screen, h = show cursor

if __name__ == '__main__':
    cursorTUI_list(num, bull)