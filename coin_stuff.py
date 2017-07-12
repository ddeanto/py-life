import random 

class CoinSession():
    def __init__(self, name):
        self.name = name
        self.num_of_flips = 0
        self.flip_history = []
        
    def flip_coin(self):
        self.num_of_flips += 1
        
        result = random.randint(0,1)
        if result == 1:
            self.flip_history.append('tails')
        else:
            self.flip_history.append('heads')
    
    def human_print(self):
        print(self.name + "'s coin ---")
        
        for ind in range(self.num_of_flips):
            print("flip " + str(ind+1) + ": " + self.flip_history[ind])
        
        print("number of flips: " + str(self.num_of_flips))
        print("")

coin1 = CoinSession("Danny")
coin1.flip_coin()
coin1.flip_coin()
coin1.flip_coin()
coin1.flip_coin()
coin1.human_print()

coin2 = CoinSession("Ryan")
coin2.flip_coin()
coin2.flip_coin()
coin2.human_print()
