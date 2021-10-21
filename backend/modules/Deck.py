from Card import Card
import random
class Deck():
    def __init__(self,symbols,cards_per_symbol):
        self.cards = []
        # TODO: nested list comprehension  to make it faster        
        for name,symbol in symbols.items():            
            for card_number in range(1,cards_per_symbol+1):
                self.cards.append(Card(card_number,symbol,name))
                
            
            
    def suffle(self):
        random.shuffle(self.cards)
                
    def __str__(self):
        return str([f"{''.join(str(x.number))}-{''.join(x.name)}" for x in self.cards])

if __name__ == "__main__":
    print(Deck())
