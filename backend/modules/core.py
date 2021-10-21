from Deck import Deck
from Player import Player
import json


class Game():

    def __init__(self,game_type = 'classic',players = []):
        self.config = None
        self.game_type =   game_type 
        self.Deck = None
        self.Players = players
        

    def deliver_card_to_player(self,player,card):
        try:
            [x.cards.append(card) for x in self.Players if x.name is player.name]                                    
            # the cards needs to be removed from the deck once is delivered
        except IndexError as e:
            #TODO: log errors
            pass

            
        
    
                        

    def init_game(self):
        # create the game with the current settings

        with open('games_config.json', 'r') as f:
            self.config = json.load(f)   
        try:
            config = self.config[self.game_type]            
            self.Deck = Deck(symbols=config['symbols'],cards_per_symbol=config['cards_per_symbol'])
        except IndexError as e:   
            #TODO: log errors         
            self.Deck = None
        
    def init_deliver_to_players(self):
        # cards per pleyers depends on the type of game
        for p in self.Players:
            for cards_per_player in range(self.config[self.game_type]['init_cards_per_player']):
                self.deliver_card_to_player(p,self.Deck.cards.pop())
            

    def __str__(self):
        # default method will be showing game stats
        output = ""
        for p in self.Players:
            for cards in p.cards:
                output += f"{p.name} -> {str(cards)} \n"
        output+= "\n -------Deck---------\n"
        output+=str(self.Deck)
        output+= "\n -------Cards Left---------\n"
        output+= f"{len(self.Deck.cards)}"
        return output

    

    def main():
        pass

if __name__ == "__main__":

    game_on = Game(game_type='classic',players = [Player("Mario"),Player("Luigi")])
    game_on.init_game()
    game_on.Deck.suffle()

    game_on.init_deliver_to_players()


    # add another card to a new payer just for testing
    peach = Player("Peach")
    game_on.Players.append(peach)
    game_on.deliver_card_to_player(peach,game_on.Deck.cards.pop())
    game_on.deliver_card_to_player(peach,game_on.Deck.cards.pop())
    game_on.deliver_card_to_player(peach,game_on.Deck.cards.pop())
    game_on.deliver_card_to_player(peach,game_on.Deck.cards.pop())

    print(game_on)
    
