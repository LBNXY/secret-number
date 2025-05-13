import random

def guessing_game():
    sc_num = random.randint(1, 99)
    print("Welcome to the guessing game!")
    print("I have selected a number between 1 and 99.")
    print("Try to guess it in as few attempts as possible.")

    guess = None  # 初始化 guess 變數
    while guess != sc_num:
        guess = int(input("Enter your guess: "))
        if guess < sc_num:
            print("Too low!")
        elif guess > sc_num:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {sc_num} correctly.")
            break

# 主程式邏輯
while True:
    guessing_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break