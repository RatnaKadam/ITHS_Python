#Project : Memory Game

import random
import string
import sys
import time

random_list = []

def blink_string(passed_string):
    sys.stdout.write('\033[5m' + passed_string + '\033[0m')
    sys.stdout.flush()
    time.sleep(4)
    sys.stdout.write('\r' + ' ' * len(passed_string) + '\r')
    sys.stdout.flush()
    time.sleep(2)


class MemoryGame:
    level: string
    normal_string: string

    def __init__(self, level):
        self.level = level

    ''' Load the game and show user correct answer and shuffled string'''
    def initialize(self):
        if self.level == "EASY":
            for i in range(0, 6):
                random_num = random.randint(0, 9)
                random_list.append(random_num)

        elif self.level == "MEDIUM":
            for i in range(0,6):
                random_letter = random.choice(string.ascii_letters).lower()
                random_list.append(random_letter)

        elif self.level == "HARD":
            for i in range(0,3):
                random_num = random.randint(0,9)
                random_letter = random.choice(string.ascii_letters).lower()
                random_list.append(random_num)
                random_list.append(random_letter)

        else:
            print("You chose the wrong option.\n")
            level_input = input("Select difficulty level: easy, medium or hard :  ").upper()

      #This is the required answer
        self.normal_string = ''.join(map(str, random_list))
       # shuffled answer
        random.shuffle(random_list)
        shuffled_string = ''.join(map(str,random_list))

       #Computer answer and shuffled list should be different
        while shuffled_string == self.normal_string:
            random.shuffle(random_list)
            shuffled_string = ''.join(map(str,random_list))


        #define a blink function to blink both strings
        print(f'Displaying normal string for 3 seconds: ')
        blink_string(self.normal_string)
        print(f'Shuffled string is {shuffled_string}')


    '''get input from user and check the answer against the correct one '''
    def play_game(self):
        game_on = True
        user_input_string = 'Enter your answer: '
        while game_on:
                user_guess = input(f"{user_input_string}").lower()
                if user_guess == self.normal_string:
                    print(f"You have guessed correct value :{self.normal_string}")
                    print(f"Congratulations, You won!!")
                    game_on = False
                else:
                    user_input_string = 'You answer is incorrect. Try again. : '
                    continue


'''creating main function and calling methods from class using object'''

def main():
    print("****** Welcome to the Memory Game ******")
    has_user_provided_input = False
    while not has_user_provided_input:
        level_input = input("Select difficulty level: easy, medium or hard :  ").upper()
        if level_input == 'EASY' or level_input == 'MEDIUM' or level_input == 'HARD':
            has_user_provided_input = True
    game = MemoryGame(level_input)
    game.initialize()
    game.play_game()

if __name__ == '__main__':
    main()