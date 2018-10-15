key = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def sort():
    indexes = []
    output = [None] * len(key)
    for i, junk in enumerate(key):
        indexes.append(i)
    under = input('How many cards will you put under after each flipped up?\n')

    for next_card in key:
        x = indexes.pop(0)
        output[x] = next_card
        if indexes:
            for i in range(0, under):
                x = indexes.pop(0)
                indexes.append(x)
    print output

sort()
