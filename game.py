from ai import Ai
from human import Human
from player import Player

print(f'Welcome to rock, paper, scissors, lizard, spock')
print(f'The winner of each match is the best of three')
        
print(f'rock crushes scissors')
print(f'scissors cuts paper')
print(f'paper covers rock')
print(f'rock crushes lizard')
print(f'lizard poisons spock')
print(f'spock smashes scissors')
print(f'scissors decapitates lizard')
print(f'lizard eats paper')
print(f'Do you want to play single or multi-player? Type 1 for single player, 2 for multi-player. ')



class Game:
    def __init__(self):
        pass


    
    def run_game(self):
        
        user_input = input('Type 1 or 2? ')
        if user_input == '1':
            while True:
                p1 = Human()
                p2 = Ai()

                while True:
                    if p1.score == 2 or p2.score == 2:
                        break
                    p1.choose_gesture()
                    p2.random_gesture()  
                
                        
                    if p1.gesture == p2.gesture:
                        print('tie')

                    elif p1.gesture == 'rock':
                        if p2.gesture == 'scissors':
                            print(f'ai picked {p2.gesture}, user won rock beats scissors')
                            p1.score += 1
                        elif p2.gesture == 'lizard':
                            print(f'ai picked {p2.gesture}, user won rock beats lizard')
                            p1.score += 1
                        elif p2.gesture == 'spock':
                            print(f'you lost, ai picked {p2.gesture} spock beats rock')
                            p2.score += 1
                        elif p2.gesture == 'paper':
                            print(f'you lost, ai picked {p2.gesture} paper beats rock')
                            p2.score += 1
                        

                    elif p1.gesture == 'paper':
                        if p2.gesture == 'rock':
                            print(f'ai picked {p2.gesture} user won, paper beats rock')
                            p1.score += 1
                        elif p2.gesture == 'spock':
                            print(f' ai picked {p2.gesture} user won, paper beats spock')
                            p1.score += 1
                        elif p2.gesture == 'scissors':
                            print(f'you lost, ai picked {p2.gesture}, scissors beats paper')
                            p2.score += 1
                        elif p2.gesture == 'lizard':
                            print(f'you lost, {p2.gesture}, lizard beats paper')
                            p2.score += 1

                    elif p1.gesture == 'scissors':
                        if p2.gesture == 'paper':
                            print(f'ai picked {p2.gesture}, user won scissors beats paper')
                            p1.score += 1
                        elif p2.gesture == 'lizard':
                            print(f'ai picked {p2.gesture}, user won scissors beats lizard')
                            p1.score += 1
                        elif p2.gesture == 'rock':
                            print(f'you lost, ai picked {p2.gesture} rock beats scissors')
                            p2.score += 1
                        elif p2.gesture == 'spock':
                            print(f'you lost, ai picked {p2.gesture} spock beats scissors')
                            p2.score += 1

                    elif p1.gesture == 'lizard':
                        if p2.gesture == 'paper':
                            print(f'ai picked {p2.gesture}, user won lizard beats paper')
                            p1.score += 1
                        elif p2.gesture == 'spock':
                            print(f'ai picked {p2.gesture}, user won lizard beats spock')
                            p1.score += 1
                        elif p2.gesture == 'rock':
                            print(f'you lost, ai picked {p2.gesture}, rock beats lizard')
                            p2.score += 1
                        elif p2.gesture == 'scissors':
                            print(f'you lost, ai picked {p2.gesture}, scissors beats lizard')
                            p2.score += 1

                    elif p1.gesture == 'spock':
                        if p2.gesture == 'rock':
                            print(f'ai picked {p2.gesture}, user won spock beats rock')
                            p1.score += 1
                        elif p2.gesture == 'scissors':
                            print(f'ai picked {p2.gesture}, user won spock beats scissors')
                            p1.score += 1
                        elif p2.gesture == 'paper':
                            print(f'you lost, ai picked {p2.gesture}, paper beats spock')
                            p2.score += 1
                        elif p2.gesture == 'lizard':
                            print(f'you lost, ai picked{p2.gesture}, lizard beats spock')
                            p2.score += 1
                            
                        else:
                                print('Pick another another name')

                if p1.score > p2.score:
                    print('p1 won the best of three match')
                else:
                    print('p2 the ai computer won the best of three match')
                while True:
                    self.play_again = input('Do you want to play again, yes or no? ')
                    if self.play_again != 'no':
                        break
    

        if user_input == '2':
            while True:
                p1 = Human()
                p2 = Human()
                while True:
                    if p1.score == 2 or p2.score == 2:
                        break
                    p1.choose_gesture()
                    p2.choose_gesture()
                    
                    if p1.gesture == p2.gesture:
                        print('tie')

                    if p1.gesture == 'rock':
                        if p2.gesture == 'scissors':
                            print('p1 won rock beats scissors')
                            p1.score += 1
                        elif p2.gesture == 'lizard':
                            print('p1 won rock beats lizard')
                            p1.score += 1
                        elif p2.gesture == 'spock':
                            print('p2 won spock beats rock')
                            p2.score += 1
                        elif p2.gesture == 'paper':
                            print('p2 won paper beats rock')
                            p2.score += 1
                                

                    elif p1.gesture == 'paper':
                        if p2.gesture == 'rock':
                            print('p1 won, paper beats rock')
                            p1.score += 1
                        elif p2.gesture == 'spock':
                            print('p1 won, paper beats spock')
                            p1.score += 1
                        elif p2.gesture == 'scissors':
                            print('p2 won, scissors beats paper')
                            p2.score += 1
                        elif p2.gesture == 'lizard':
                            print('p2 won, lizard beats paper')
                            p2.score += 1

                    elif p1.gesture == 'scissors':
                        if p2.gesture == 'paper':
                            print('p1 won scissors beats paper')
                            p1.score += 1
                        elif p2.gesture == 'lizard':
                            print('p1 won scissors beats lizard')
                            p1.score += 1
                        elif p2.gesture == 'rock':
                            print('p2 won rock beats scissors')
                            p2.score += 1
                        elif p2.gesture == 'spock':
                            print('p2 won spock beats scissors')
                            p2.score += 1

                    elif p1.gesture == 'lizard':
                        if p2.gesture == 'paper':
                            print('p1 won lizard beats paper')
                            p1.score += 1
                        elif p2.gesture == 'spock':
                            print('p1 won lizard beats spock')
                            p1.score += 1
                        elif p2.gesture == 'rock':
                            print('p2 won rock beats lizard')
                            p2.score += 1
                        elif p2.gesture == 'scissors':
                            print('p2 won scissors beats lizard')
                            p2.score += 1

                    elif p1.gesture == 'spock':
                        if p2.gesture == 'rock':
                            print('p1 won spock beats rock')
                            p1.score += 1
                        elif p2.gesture == 'scissors':
                            print('p1 won won spock beats scissors')
                            p1.score += 1
                        elif p2.gesture == 'paper':
                            print('p2 won paper beats spock')
                            p2.score += 1
                        elif p2.gesture == 'lizard':
                            print('p2 won lizard beats spock')
                            p2.score += 1
                                    
                        else:
                            print('Pick another another name')

                if p1.score > p2.score:
                    print('P1 won the best of three match')
                else:
                    print('P2 won the best of three match')
                while True:
                    self.play_again = input('Do you want to play again, yes or no? ')
                    if self.play_again != 'no':
                        break
                            
        