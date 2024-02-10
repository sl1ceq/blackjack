import random

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        if self.rank in "ТВДК":
            return 10
        else:
            return " А23456789".index(self.rank)

    def get_rank(self):
        return f"{git self.suit}{self.rank}"
    

class DeskCard:
    def __init__(self):
        _rank = "А23456789ТВДК"
        _suit = "ПБЧК"
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self):
        return self.__cards.pop()


class Player:
    def __init__(self, name: str):
        self._hand = []
        self.count = 0
        self.name = name

    @property
    def hand(self):
        return f"Карты в руке {self.name}: {self._hand}; Очков: {self.count}"

    @hand.setter
    def hand(self, card: Card):
        self.count += card.get_value()
        self._hand.append(card.get_rank())


class Dealer(Player):
    def get_card(self, cards):
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value() + self.count <= 21:
                self.hand = _card
            else:
                break


class Game:
    def __init__(self, player_name: str):
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name="Dealer")

    def print(self):
        return f"\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}"
    
    def check_count(self):
        if self.player.count > 21:
            print(f"You lost", self.print())
        elif self.dealer.count > 21 and self.player.count < 22:
            print(f"You won", self.print())
        elif self.player.count == self.dealer.count:
            print(f"Draw", self.print())
        elif self.player.count < self.dealer.count:
            print(f"You lost", self.print())
        elif self.player.count > self.dealer.count:
            print(f"You won", self.print())

    def start(self):
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        print(self.player.hand)
        while self.player.count < 21:
            answer = input('Хотите взять карту? y/n? ')
            if answer == 'y':
                new_card = self.cards.get_card()
                self.player.hand = new_card
                print(self.player.hand)
            elif answer == 'n':
                self.dealer.get_card(self.cards)
                break
        self.check_count()


def main():
    name = input('Ваше имя:')
    game = Game(name)
    game.start()

main()
