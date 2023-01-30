from py_d14_game_images import logo,vs
import py_d14_game_data as game_data
import random

score = 0
right_guess = True

def display_details(option,name,description,country):
    '''Displays the details of different options.'''

    #Vowel checker
    if description[0].lower() in ['a','e','i','o','u']:
        suffix = 'an'
    else:
        suffix = 'a'

    return f"Compare {option.upper()}: {name}, {suffix} {description}, from {country}."

def compare(user,computer,score):
    if user > computer:
        score += 1
        print(f"You're right! Your score: {score}\n")
        return score
    elif user < computer:
        print(f"Game Over. Final score: {score}")
        exit()


print(logo)
while right_guess == True:
    option_a = random.choice(game_data.data)
    option_b = random.choice(game_data.data)
    while option_a == option_b:
        option_b = random.choice(game_data.data)
    print(display_details('a',option_a['name'],option_a['description'],option_a['country']))
    print(vs)
    print(display_details('b',option_b['name'],option_b['description'],option_b['country']))
    selected_option = input("Who has more followers? Type 'A' or 'B': ").lower()
    if selected_option == 'a':
        score = compare(int(option_a['follower_count']),int(option_b['follower_count']),score)
    elif selected_option == 'b':
        score = compare(int(option_b['follower_count']),int(option_a['follower_count']),score)
