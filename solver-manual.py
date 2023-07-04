# Variables
possible_words = []
letter = 'a'
position = 1
word_list = []

# Dictionary of possible words - 5 letters words
with open("words_list.txt") as w:
    possible_words = w.readlines()
# Print introduction
print("=== Welcome to Wordle Solver by Koushik Mallik! ===\n")
print("* THIS PROGRAM WILL NOT SOLVE THE WORDLE FOR YOU! *")
print("Instead it will help you make a better guess by eliminating words that do not work.\n")
print("Follow these steps:")
print("\t1. Make your first guess in wordle")
print("\t2. Provide each letter, color, and position when asked to do so in the program")
print("\t\ty = yellow")
print("\t\tg = green")
print("\t\tb = black")
print("\t3. Make the next guess using the possible word list")
print("\t4. Repeat until you find the word of the day\n")

print("Press CONTROL + C or CONTROL + Z to quit the program\n")
print("========== Good luck! ==========\n")


# Main part of the program
while letter != '':
    del word_list[:]

    # Input
    letter = input("What letter do you know: ")
    color = input("What color is the letter (y, g, b): ")

    # If we got a green letter or yellow letter
    if color == 'g' or color == 'y':
        position = int(input("What position is the letter in (1 - 5): "))
        position -= 1

    # Go through all possible words
    for word in possible_words:
        # Green
        if color == 'g':
            if word[position] == letter:
                word_list.append(word)
        # Black
        elif color == 'b':
            if letter not in word:
                word_list.append(word)

        # Yellow
        elif color == 'y':
            if letter in word:
                if word[position] != letter:
                    word_list.append(word)

    # Print out possible words

    possible_words = word_list.copy()
    print(*word_list)
