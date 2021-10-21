class Player():
    def __init__(self,name) -> None:
        self.cards = []
        self.name = name

    def __str__(self):
        return f"{self.name} -> {str(self.cards)} "
    
        