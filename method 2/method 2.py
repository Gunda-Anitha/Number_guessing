import random
def num_to_guess(): 
    num_to_guess=random.randint(1,100)
    attempts=5
    high=100
    low=0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while attempts>0:
        try:
            guess=int(input("Enter a guess : "))
            attempts-=1
            if guess < num_to_guess:
                if guess > low:
                    low=guess
                if attempts>0:
                    print(f"number is in between {low} and {high}, too low ,try again")
            elif guess > num_to_guess:
                if guess < high:
                    high=guess
                if attempts>0:
                    print(f"number is in between {low} and {high}, too high, try again")
            else:
                print(f"congrats you won the number is {guess}")
                break
            if attempts>0:
                print(f"{attempts} attempts left ")
            else:
                print("you fail")
                print(f"The number is {num_to_guess}")
        except ValueError:
            print("enter valid number")
if __name__ == "__main__":
    num_to_guess()

