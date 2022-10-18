SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
ACCIDENTAL = {'#': 1, 'b': -1}

while True:
    sheet = input()
    if sheet.find('***') > -1:
        break
    move = int(input())

    for scale in sheet.split():
        if scale in SCALE:
            print(SCALE[(SCALE.index(scale) + move) % len(SCALE)], end= ' ')
        else :
            print(SCALE[(SCALE.index(scale[0]) + ACCIDENTAL[scale[-1]] + move) % len(SCALE)], end= ' ')
    print()