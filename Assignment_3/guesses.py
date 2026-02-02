import random
nums= random.randint(1, 10)

def guess_nums(nums):
    
    while True:
        guess= int(input("Enter your guess (1-10): "))

        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
        elif guess == nums:
            print("Congratulations!")
            break
        elif guess > nums:
            print("Too high!")
        else:
            print("Too low!")

guess_nums(nums)