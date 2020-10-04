import sys
from nano import search

print('Type :x to exit.')

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        for sol in search(f.read()):
            print()
            print(sol)

while True:
    try:
        source = input('> ')
        if source == ':x':
            break
        else:
            for sol in search(source):
                print()
                print(sol)
                ans = input('continue? ')
                if ans == '.':
                    break
    except EOFError:
        break
