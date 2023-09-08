# # import random


# # def guess_number(attempts, start, end):
# #     number = random.randint(start, end)

# #     print("Guess the number between", start, "and", end)
# #     print("You have", attempts, "attempts.")

# #     for attempt in range(1, attempts + 1):
# #         guess = int(input("Attempt #" + str(attempt) + ": Enter your guess: "))

# #         if guess < number:
# #             print("Too low!")
# #         elif guess > number:
# #             print("Too high!")
# #         else:
# #             print("Congratulations! You guessed the correct number in",
# #                   attempt, "attempts.")
# #             return

# #     print("Sorry, you ran out of attempts. The correct number was", number)


# # def main():
# #     attempts = 5  # Number of attempts allowed
# #     start = 1  # Start of the number range
# #     end = 100  # End of the number range

# #     guess_number(attempts, start, end)


# # # if __name__ == "__main__":
# # #     main()


# # import random
# # from nltk.corpus import wordnet


# # def get_random_word():
# #     """Returns a random word from the WordNet lexical database."""
# #     synsets = list(wordnet.all_synsets())
# #     return random.choice(synsets).lemmas()[0].name()


# # def play_game():
# #     current_word = get_random_word()
# #     print("Welcome to the Word Chain Challenge!")
# #     print("I will start with a random word. You need to provide a word that starts with the last letter of my word.")
# #     print("Let's begin!")

# #     while True:
# #         print("Current word:", current_word)
# #         player_word = input("Enter your word: ").lower()

# #         if player_word[0] != current_word[-1]:
# #             print(
# #                 "Oops! The word should start with the last letter of the previous word. You lose!")
# #             break

# #         if player_word in ["quit", "exit"]:
# #             print("You chose to quit. Thanks for playing!")
# #             break

# #         if not wordnet.synsets(player_word):
# #             print("Invalid word. You lose!")
# #             break

# #         current_word = player_word


# # play_game()

# # Snake water gun

# import random
# lst = ['s', 'w', 'g']

# chance = 10
# no_of_chance = 0
# computer_point = 0
# human_point = 0

# print(" \t \t \t \t Snake,Water,Gun Game\n \n")
# print("s for snake \nw for water \ng for gun \n")

# # making the game in while
# while no_of_chance < chance:
#     _input = input('Snake,Water,Gun:')
#     _random = random.choice(lst)

#     if _input == _random:
#         print("Tie Both 0 point to each \n ")

#     # if user enter s
#     elif _input == "s" and _random == "g":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(
#             f"computer_point is {computer_point} and your point is {human_point} \n ")

#     elif _input == "s" and _random == "w":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(
#             f"computer_point is {computer_point} and your point is {human_point} \n")

#     # if user enter w
#     elif _input == "w" and _random == "s":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(
#             f"computer_point is {computer_point} and your point is {human_point} \n ")

#     elif _input == "w" and _random == "g":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(
#             f"computer_point is {computer_point} and your point is {human_point} \n")

#     # if user enter g

#     elif _input == "g" and _random == "s":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(
#             f"computer_point is {computer_point} and your point is {human_point} \n")

#     elif _input == "g" and _random == "w":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(
#             f"computer_point is {computer_point} and your point is {human_point} \n ")

#     else:
#         print("you have input wrong \n")

#     no_of_chance = no_of_chance + 1
#     print(f"{chance - no_of_chance} is left out of {chance} \n")

# print("Game over")

# if computer_point == human_point:
#     print("Tie")

# elif computer_point > human_point:
#     print("Computer wins and you loose")

# else:
#     print("you win and computer loose")

# print(f"your point is {human_point} and computer point is {computer_point}")

# #
# # Snake Water Gun Game in Python
# # The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
# #


def calculate_bill(items):
    total_cost = 0

    for item in items:
        name = item['name']
        price = item['price']
        quantity = item['quantity']

        item_cost = price * quantity
        total_cost += item_cost

        print(f"{name}: {quantity} x ${price} = ${item_cost}")

    print("------------------------------")
    print(f"Total: ${total_cost}")


# Example usage
shopping_list = [
    {"name": "Apple", "price": 0.5, "quantity": 5},
    {"name": "Banana", "price": 0.25, "quantity": 10},
    {"name": "Orange", "price": 0.3, "quantity": 7},
]

calculate_bill(shopping_list)
