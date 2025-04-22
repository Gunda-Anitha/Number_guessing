import random
def num_to_guess(): 
    num_to_guess=random.randint(1,100)
    attempts=0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while True:
        try:
            guess=int(input("Enter a guess : "))
            attempts+=1
            
            if guess < num_to_guess:
                print("too low, try again")
            elif guess > num_to_guess:
                print("too high , try again")
            else:
                print(f'Congrats you guessed in {attempts} attempts')
                break
        except ValueError:
            print("enter valid number")
if __name__ == "__main__":
    num_to_guess()