# This program displays an upside-down triangle pattern.
BASE_SIZE = 1

for r in range(BASE_SIZE + 6):
    for c in range(r + 1):
        print('*', end='')
    print()
