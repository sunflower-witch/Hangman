import msvcrt

def keyword(prompt="Enter the word: \n"):
    print(prompt, end='', flush=True)
    word = ''
    while True:
        ch = msvcrt.getch()
        if ch in {b'\r', b'\n'}:
            print()
            break
        elif ch == b'\x08':  # Handle backspace
            if len(word) > 0:
                word = word[:-1]
                print('\b \b', end='', flush=True)
        else:
            word += ch.decode('utf-8')
            print('*', end='', flush=True)
    return word.upper()
