import random
from replit import clear
import art
from game_data import data

def compare_followers(a, b, guess):
    followers_a = a["follower_count"]
    followers_b = b["follower_count"]

    if followers_a > followers_b:
        return guess == "a"
    else:
        return guess == "b"

def display_message(person):
    return f"{person['name']}, the {person['description']} from {person['country']}"

# Set initial person A
person_a = random.choice(data)
score = 0

print(art.logo)

is_playing = True
while is_playing:
    # Set person B
    person_b = random.choice(data)
    
    print(f"Compare A: {display_message(person_a)}")
    print(art.vs)
    print(f"Against B: {display_message(person_b)}")
    
    # Collect player's guess
    player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    clear()
    print(art.logo)
    if compare_followers(person_a, person_b, player_guess):
        score += 1
        # Set next person A to previous person B
        person_a = person_b
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_playing = False