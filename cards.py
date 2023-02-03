from random import shuffle


def create_deck():
    deck = []
    face_values = ['A', 'J', 'K', 'Q']
    for i in range(4):
        for card in range(2, 11):
            deck.append(str(card))
        for card in face_values:
            deck.append(card)
    shuffle(deck)
    return deck


# decks = create_deck()
# # shuffle(decks)
# print(decks)


class Player:
    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.setscore()
        self.money = money
        self.bet = 0

    def __str__(self):
        current_hand = ''
        for card in self.hand:
            current_hand += str(card) + ' '
        final_status = f'{current_hand}, Score: {self.score}'
        return final_status

    def setscore(self):
        self.score = 0
        score_dict = {'A': 11, 'J': 10, 'Q': 10, 'K': 10,
                      "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                      "7": 7, "8": 8, "9": 9, "10": 10}
        counter = 0
        for card in self.hand:
            # if int(card) in range(2, 11):
            #     self.score += int(card)
            # elif card in score_dict:
            self.score += score_dict[card]
            if card == 'A':
                counter += 1
            if self.score > 21 and counter != 0:
                self.score -= 10
                counter -= 1
        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.setscore()

    def play(self, new):
        self.hand = new
        self.score = self.setscore()

    def bet_money(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, results):
        if results:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5 * self.bet
            else:
                self.money += 2*self.bet
            self.bet = 0
        else:
            self.bet = 0

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def blackjack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False


def print_house(hand):
    for card in range(len(hand.hand)):
        if card == 0:
            print('X', end=' ')
        elif card == len(hand.hand) - 1:
            print(hand.hand[card])
        else:
            print(hand.hand[card], end=' ')


decks = create_deck()
first = [decks.pop(), decks.pop()]
second = [decks.pop(), decks.pop()]
player1 = Player(first)
house = Player(second)
decks = create_deck()
while True:
    if len(decks) < 20:
        decks = create_deck()
    first = [decks.pop(), decks.pop()]
    second = [decks.pop(), decks.pop()]
    player1 = Player(first)
    house = Player(second)
    bet = int(input('Please put your bet amount: '))
    player1.bet_money(bet)
    print(decks)
    print_house(house)
    print(player1)
    if player1.blackjack():
        if house.blackjack():
            player1.draw()
        else:
            player1.win(True)
    else:
        while player1.score < 21:
            action = input('Do you want another card? (y/n): ')
            if action.lower() == 'y':
                player1.hit(decks.pop())
                print(player1)
                print_house(house)
            else:
                break

        while house.score < 16:
            print(house)
            house.hit(decks.pop())
        if player1.score > 21:
            if house.score > 21:
                player1.draw()
            else:
                player1.win(False)
        elif player1.score > house.score:
            player1.win(True)
        elif player1.score == house.score:
            player1.draw()
        else:
            if house.score > 21:
                player1.win(True)
            else:
                player1.win(False)
    print(player1.money)
    print(house)
