class Sort_Cards():
    key = []
    output = []
    stop = False
    def __init__(self):
        self.yes_or_no('Would you like Ace-King?', self.ace_to_king, self.create_a_key)

    def yes_or_no(self, question, yes_outcome, no_outcome):
        reply = str(raw_input(question + '\n(y or n): ')).lower().strip()
        if reply[0] == 'y':
            return yes_outcome()
        if reply[0] == 'n':
            return no_outcome()
        else:
            return self.yes_or_no("Uhhhh... please enter (y or n", yes_outcome, no_outcome)

    def ace_to_king(self):
        self.key = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def create_a_key(self):
        inp = raw_input('Please enter a comma seperated list:\n')
        list = []
        for each in inp.split(', '):
            list.append(each)
        self.key = list

    def repeat_list(self):
        self.sort(self.output)

    def stop():
        return False

    def sort(key):
        indexes = []
        output = [None] * len(key)
        for i, junk in enumerate(key):
            indexes.append(i)
        under = input ('How many cards will you put under after each flipped up?\n')

        for next_card in key:
            x = indexes.pop(0)
            output[x] = next_card
            if indexes:
                for i in range(0, under):
                    x = indexes.pop(0)
                    indexes.append(x)
        print output
        return output

key = yes_or_no('Would you like Ace-King?', ace_to_king, create_a_key)
output = sort(key)
