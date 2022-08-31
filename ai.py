from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        
    def random_gesture(self):
        self.gesture_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.gesture = random.choice(self.gesture_list)
        if self.gesture == 'rock':
            self.gesture = self.gesture_list[0]
            print(self.gesture)
        elif self.gesture == 'paper':
            self.gesture = self.gesture_list[1]
            print(self.gesture)
        elif self.gesture == 'scissors':
            self.gesture = self.gesture_list[2]
            print(self.gesture)
        elif self.gesture == 'lizard':
            self.gesture = self.gesture_list[3]
            print(self.gesture)
        elif self.gesture == 'spock':
            self.gesture == self.gesture_list[4]
        else:
            'Please pick another gesture. '

