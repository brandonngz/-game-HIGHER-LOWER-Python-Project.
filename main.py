import random
import art
from replit import clear
from game_data import data


# Initial List with string = blank at index 0, then change it for the real data.
first_competitor = ['blank']
second_competitor = ['blank']

def random_number():
    """Generate a random number"""
    number = random.randint(1, 49)
    return number

def competitor_selection(index):
    """A function picking which competitor is going to be selected"""
    competitors = {
        1: first_competitor,
        2: second_competitor,
    }
    return competitors[index]

def adding_competitor(random_index, position):
    """pick a character by lifting to assign it to a list"""
    # Name, follower_count, description, country
    name = data[random_index]['name']
    follow = data[random_index]['follower_count']
    description = data[random_index]['description']
    country = data[random_index]['country']

    competitor_selection(position)[0] = {
        'name': name,
        'follower_count': follow,
        'description': description,
        'country': country,
    }

# Assignment for random competitors this case:[TWO]
def assignment():
    adding_competitor(random_number(), 1)
    adding_competitor(random_number(), 2)

def change_second_to_first_position(change):
    first_competitor[0] = {
        'name': change[0]['name'],
        'follower_count': change[0]['follower_count'],
        'description':change[0]['description'],
        'country': change[0]['country'],
    }

# if the user lost the game, ask if he/she want to play again.
def lost():
    again = input("Play again: 'y' or 'n' ")
    clear()
    if again == 'y':
        return True
    else:
        return False

# START THE GAME.
def game():
    string = ''
    score = 0
    _keep_going = True
    while _keep_going:
        print(art.logo)
        print(string)
        print(f"Compare A: {first_competitor[0]['name']}, a {first_competitor[0]['description']}, from {first_competitor[0]['country']}, has {first_competitor[0]['follower_count']} million followers")
        print(art.vs)
        print(f"Compare B: {second_competitor[0]['name']}, a {second_competitor[0]['description']}, from {second_competitor[0]['country']}, has {second_competitor[0]['follower_count']} million followers")

        compare_one = first_competitor[0]['follower_count']
        compare_two = second_competitor[0]['follower_count']
        
        compare = input("Who has more Instagram followers: 'A' or 'B' \n").upper()
        
        if 'A' in compare:
            if compare_one > compare_two:
                clear()
                score += 1
                string = f"You're right! Current score: {score}"
                
                change_second_to_first_position(second_competitor)
                adding_competitor(random_number(), 2)
            # 1  🡻
            elif compare_one == compare_two:
                clear()
                adding_competitor(random_number(), 2)
            # 2 🡻
            else:
                clear()
                print(f"You lost, Your score is: {score}")
                # 5
                if not lost():
                    break
                else:
                    assignment()

        elif 'B' in compare:
            if compare_two > compare_one:
                clear()
                score += 1
                string = f"You're right! Current score: {score}"
                # 4
                change_second_to_first_position(second_competitor)
                adding_competitor(random_number(), 2)
            # 1  🡻
            elif compare_one == compare_two:
                clear()
                adding_competitor(random_number(), 2)
             # 2 🡻
            else:
                clear()
                print(f"You lost, Your score is: {score}")
                # 5
                if not lost():
                    break
                else:
                    assignment()
assignment()
game()


# Documentation.

# 1
# elif statement It is made like this, in case the two are the same 

# 2
# example: you chose A, and this is < than B, then you lose.

# 3
# keep the first competitor and change the second one to another.

# 4
# Calling a function and passing the value.
# If the second comparison was right and is higher than A, is necessary to pass the info to A and pick another competitor for B.

# 5
# Ask if the user want to play again. if not just break.