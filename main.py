import pyfiglet
import termcolor
import random


def initiate_random_number():
    random_number = random.randint(1,10)
    return random_number

def get_user_input():

    while True:
        user_guess= (input("guess a number from 1 to 10: "))
        if user_guess.isnumeric():
            break
        print("Please input a number")
        continue
    user_guess=int(user_guess)
    return user_guess


def play_game_again():
    play_again = input("Do you want to play again?(yes/no) ").lower()
    play_again_options = {"y", "yes", "yah", "yup", "ye", "obviously"}
    if play_again in play_again_options:
        main()
    else:
        print("Thanks for Playing!!! \n Come back soon!!!")


def main():
    random_number = initiate_random_number()
    while True:
        user_guess = get_user_input()
        if random_number == user_guess:
            break
        elif user_guess > random_number:
            print("too high, try again")
            continue
        else:
            print("too low, try again")
            continue
    print("You win!!!")
    play_game_again()


if __name__ == "__main__":
    header = pyfiglet.figlet_format("Guess That Number!!")
    header = termcolor.colored(header, color="magenta")
    print(header)
    main()
