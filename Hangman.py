import time


def graphic(health):
    print(f"{YELLOW}Your current health is:{health}{RESET}")
    if health == 6:
        print("   ")
    elif health == 5:
        print("🐱")
    elif health == 4:
        print(f"{YELLOW}🐱\n|{RESET}")
    elif health == 3:
        print(f"{YELLOW}🐱\n❬|{RESET}")
    elif health == 2:
        print(f"{YELLOW}🐱\n❬|❭{RESET}")
    elif health == 1:
        print(f"{YELLOW}🐱\n❬|❭\n❲ {RESET}")
    elif health == 0:
        print(f"{YELLOW}🐱\n❲|❳\n❲ ❳{RESET}")


def check_word(letter, word_list, empty_list, health):
    if letter in word_list:
        for index, value in enumerate(word_list):
            if value == letter:
                empty_list[index] = letter
        print(f"✨{YELLOW}You guessed a letter✨{RESET}")
        graphic(health)
        print(*empty_list)
        return health, empty_list
    print(f"Wrong! this letter is not in the word! You loose 1 health.")
    health -= 1
    graphic(health)
    return health, empty_list


def play(word, word_empty):
    play_again = True
    while play_again:
        print()
        print(f"Let's play!")
        print(f"The word you're searching for has the length of {len(word)}.\n")
        health = 6
        print(*word_empty)
        graphic(health)
        while health != 0:
            letter = input(f"Guess a letter:\n")
            while len(letter) != 1 and letter.isdigit():
                print(f"Please type only 1 letter.")
                letter = input("Guess a letter:\n")
                continue
            health, word_empty = check_word(letter, word_list, word_empty,health)
            if health == 0:
                print(f"{RED_COLOR}You lost! The word was: {word}{RESET}")
                print(f"{WINNER_COLOR}Do you want to play again?{RESET} {FIRST_COLOR}Y{RESET}/{RED_COLOR}N{RESET}")
                pick = input().strip().upper()
                if pick != "Y":
                    play_again = False
                    break
                else:
                    word_empty = ["🔳" for _ in word]
                    health = 6
                    continue
            if word_empty == word_list:
                print(f"✨You're the winner! Congrats!✨")
                print(f"{WINNER_COLOR}Do you want to play again?{RESET} {FIRST_COLOR}Y{RESET}/{RED_COLOR}N{RESET}")
                pick = input().strip().upper()
                if pick != "Y":
                    play_again = False
                    break
                else:
                    word_empty = ["🔳" for _ in word]
                    health = 6
                    break


def rgb_escape_code(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


# Colors for text
WINNER_COLOR = rgb_escape_code(171, 157, 255)  # lilac for winner
RED_COLOR = rgb_escape_code(255, 139, 104)  # red
FIRST_COLOR = rgb_escape_code(157, 255, 179)  # green
SECOND_COLOR = rgb_escape_code(157, 226, 255)  # teal
YELLOW = rgb_escape_code(255, 222, 106)  # yellow

RESET = "\033[0m"  # Reset color

print("\n🐙🐙🐙🐙🐙🐙🐙")
print(f"🐙🐙{WINNER_COLOR}Hangman{RESET}🐙🐙")
print("🐙🐙🐙🐙🐙🐙🐙\n")
print(f"{RED_COLOR}Welcome to Hangman! Guess the word before your health runs out!")
print(f"Ready? Let's go!{RESET}")
word = input("Please enter your password:\n")
print(f"The word has been set. It is {len(word)} letters long.")
print(f"{YELLOW}Now, let's hide it!{RESET}")
print(f"Hiding in progress...")
time.sleep(2)
print('🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙\n' * 40)

print(f"Done! They will never be able to find it...")
word_list = [i for i in word]
equivalent = ["🔳" for i in word]

play(word_list, equivalent)
print(f"{WINNER_COLOR}Thanks for playing!💜{RESET}")
