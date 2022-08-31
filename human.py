from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
        self.score = self.score
        
    
    def choose_gesture(self):
        user_input = input('which gesture do yo want to pick? rock, paper, scissors, lizard, or spock? ')
        self.gesture = user_input
        if user_input == 'rock':
            self.gesture = self.gesture_list[0]
            print(self.gesture)
        elif user_input == 'paper':
            self.gesture = self.gesture_list[1]
            print(self.gesture)
        elif user_input == 'scissors':
            self.gesture = self.gesture_list[2]
            print(self.gesture)
        elif user_input == 'lizard':
            self.gesture = self.gesture_list[3]
            print(self.gesture)
        elif user_input == 'spock':
            self.gesture == self.gesture_list[4]
        else:
            'Please pick another gesture. '
            
  
