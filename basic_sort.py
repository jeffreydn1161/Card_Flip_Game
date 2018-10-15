class Sort_Cards2():
    key = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def sort(self):
        indexes = []
        output = [None] * len(self.key)
        for i, junk in enumerate(self.key):
            indexes.append(i)
        under = input('How many cards will you put under after each flipped up?\n')

        for next_card in self.key:
            x = indexes.pop(0)
            output[x] = next_card
            if indexes:
                for i in range(0, under):
                    x = indexes.pop(0)
                    indexes.append(x)
        print output
        # self.continue_key()

    def continue_key(self, new_key):
        question = 'Would you like to contiue with this new key?'
        reply = str(raw_input(question + '\n(y or n): ')).lower().strip()
        if reply[0] == 'y':
            self.key = new_key
            return
        if reply[0] == 'n':
            print 'Thanks for playing'
            return
        else:
            print 'Not a valid input.'
            return self.continue_key(new_key)

card_game = Sort_Cards2()

card_game.sort()
