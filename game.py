from ai import Ai
from player import Player

class Game:
    def __init__(self):
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



    
    def run_game(self):
        
        user_input = input('1 or 2? ')
        if user_input == '1':
   
            
            while True:
                user_choice_wins = 0
                ai_choice_wins = 0
                import random
                while True:
                    
                    if user_choice_wins == 2 or ai_choice_wins == 2:
                        break
                    user_choice = input('Please enter a choice (rock, paper, scissors, lizard, spock): ')
                    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
                    ai_choice = random.choice(choices)

                    if user_choice == ai_choice:
                        print('tie')

                    elif user_choice == 'rock':
                        if ai_choice == 'scissors':
                            print('user won rock beats scissors')
                            user_choice_wins += 1
                        elif ai_choice == 'lizard':
                            print('user won rock beats lizard')
                            user_choice_wins += 1
                        elif ai_choice == 'spock':
                            print('you lost spock beats rock')
                            ai_choice_wins += 1
                        else:
                            print('you lost paper beats rock')
                            ai_choice_wins += 1
                    

                    elif user_choice == 'paper':
                        if ai_choice == 'rock':
                            print('user won, paper beats rock')
                            user_choice_wins += 1
                        elif ai_choice == 'spock':
                            print('user won, paper beats spock')
                            user_choice_wins += 1
                        elif ai_choice == 'scissors':
                            print('you lost, scissors beats paper')
                            ai_choice_wins += 1
                        elif ai_choice == 'lizard':
                            print('you lost, lizard beats paper')
                            ai_choice_wins += 1

                    elif user_choice == 'scissors':
                        if ai_choice == 'paper':
                            print('user won scissors beats paper')
                            user_choice_wins += 1
                        elif ai_choice == 'lizard':
                            print('user won scissors beats lizard')
                            user_choice_wins += 1
                        elif ai_choice == 'rock':
                            print('you lost rock beats scissors')
                            ai_choice_wins += 1
                        elif ai_choice == 'spock':
                            print('you lost spock beats scissors')
                            ai_choice_wins += 1

                    elif user_choice == 'lizard':
                        if ai_choice == 'paper':
                            print('user won lizard beats paper')
                            user_choice_wins += 1
                        elif ai_choice == 'spock':
                            print('user won lizard beats spock')
                            user_choice_wins += 1
                        elif ai_choice == 'rock':
                            print('you lost rock beats lizard')
                            ai_choice_wins += 1
                        elif ai_choice == 'scissors':
                            print('you lost scissors beats lizard')
                            ai_choice_wins += 1

                    elif user_choice == 'spock':
                        if ai_choice == 'rock':
                            print('user won spock beats rock')
                            user_choice_wins += 1
                        elif ai_choice == 'scissors':
                            print('user won spock beats scissors')
                            user_choice_wins += 1
                        elif ai_choice == 'paper':
                            print('you lost paper beats spock')
                            ai_choice_wins += 1
                        elif ai_choice == 'lizard':
                            print('you lost lizard beats spock')
                            ai_choice_wins += 1
                        
                    else:
                            print('Pick another another name')

                if user_choice_wins > ai_choice_wins:
                    print('you won the best of three match')
                else:
                    print('you lost the ai computer won the best of three match')

                self.play_again = input('Do you want to play again, yes or no? ')
                if self.play_again != 'yes':
                    break
    

        if user_input == '2':
            while True:
                    p1_choice_wins = 0
                    p2_choice_wins = 0
                    import random
                    while True:
                        
                        if p1_choice_wins == 2 or p2_choice_wins == 2:
                            break
                        p1_choice = input('Please enter a choice (rock, paper, scissors, lizard, spock): ')
                        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
                        p2_choice = input('Please enter a choice (rock, paper, scissors, lizard, spock):')

                        if p1_choice == p2_choice:
                            print('tie')

                        elif p1_choice == 'rock':
                            if p2_choice == 'scissors':
                                print('p1 won rock beats scissors')
                                p1_choice_wins += 1
                            elif p2_choice == 'lizard':
                                print('p1 won rock beats lizard')
                                p1_choice_wins += 1
                            elif p2_choice == 'spock':
                                print('p2 won spock beats rock')
                                p2_choice_wins += 1
                            elif p2_choice == 'paper':
                                print('p2 won paper beats rock')
                                p2_choice_wins += 1
                        

                        elif p1_choice == 'paper':
                            if p2_choice == 'rock':
                                print('p1 won, paper beats rock')
                                p1_choice_wins += 1
                            elif p2_choice == 'spock':
                                print('p1 won, paper beats spock')
                                p1_choice_wins += 1
                            elif p2_choice == 'scissors':
                                print('p2 won, scissors beats paper')
                                p2_choice_wins += 1
                            elif p2_choice == 'lizard':
                                print('p2 won, lizard beats paper')
                                p2_choice_wins += 1

                        elif p1_choice == 'scissors':
                            if p2_choice == 'paper':
                                print('p1 won scissors beats paper')
                                p1_choice_wins += 1
                            elif p2_choice == 'lizard':
                                print('p1 won scissors beats lizard')
                                p1_choice_wins += 1
                            elif p2_choice == 'rock':
                                print('p2 won rock beats scissors')
                                p2_choice_wins += 1
                            elif p2_choice == 'spock':
                                print('p2 won spock beats scissors')
                                p2_choice_wins += 1

                        elif p1_choice == 'lizard':
                            if p2_choice == 'paper':
                                print('p1 won lizard beats paper')
                                p1_choice_wins += 1
                            elif p2_choice == 'spock':
                                print('p1 won lizard beats spock')
                                p1_choice_wins += 1
                            elif p2_choice == 'rock':
                                print('p2 won rock beats lizard')
                                p2_choice_wins += 1
                            elif p2_choice == 'scissors':
                                print('p2 won scissors beats lizard')
                                p2_choice_wins += 1

                        elif p1_choice == 'spock':
                            if p2_choice == 'rock':
                                print('p1 won spock beats rock')
                                p1_choice_wins += 1
                            elif p2_choice == 'scissors':
                                print('p1 won won spock beats scissors')
                                p1_choice_wins += 1
                            elif p2_choice == 'paper':
                                print('p2 won paper beats spock')
                                p2_choice_wins += 1
                            elif p2_choice == 'lizard':
                                print('p2 won lizard beats spock')
                                p2_choice_wins += 1
                            
                        else:
                                print('Pick another another name')

                    if p1_choice_wins > p2_choice_wins:
                        print('P1 won the best of three match')
                    else:
                        print('P2 won the best of three match')

                    self.play_again = input('Do you want to play again, yes or no? ')
                    if self.play_again != 'yes':
                        break
        