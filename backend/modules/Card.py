
class Card():
    def __init__(self,number = None,symbol = None,name = None):
        self.number = number
        self.symbol = symbol
        self.name = name

    def __str__(self):
        return f"{self.number}-{self.name}-{self.symbol}"
    
if __name__ == "__main__":
    print(Card())