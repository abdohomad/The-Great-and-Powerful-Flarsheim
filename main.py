

#Define var
end_game="Y"
remainder1 = 0
remainder2 = 0
remainder3 = 0

print("Welcome to the Flarsheim Guesser!\n")
print("Please think of a number between and including 1 and 100.\n")
#Loop till user enter N.
while(end_game != "N"):
    
    remainder1 = int(input("What is the remainder when your number is divided by 3 ?"))
    while not( remainder1 >-1 and remainder1 < 3): # While loop validating the user input and keep asking agin until the input not in range 0,1,2.
        print("The value entered must be 0 or greater")
        remainder1 = int(input(f"What is the remainder when your number is divided by 3?"))
    print()    
    
    remainder2 = int(input("What is the remainder when your number is divided by 5 ?"))
    while not( remainder2 >=0 and remainder2 <= 4): # While loop validating the user input and keep asking agin until the input not in range 0,1,2,4.
        print("The value entered must be 0 or greater")
        remainder2 = int(input(f"What is the remainder when your number is divided by 5?"))
    print() 
        
    remainder3 = int(input("What is the remainder when your number is divided by 7 ?"))
    while not( remainder3 >=0 and remainder3 <= 6):# While loop validating the user input and keep asking agin until the input not in range 0,1,2,3,4,5.
        print("The value entered must be 0 or greater")
        remainder3 = int(input(f"What is the remainder when your number is divided by 7?"))
    print() 

    for number in range(1,101):# The user number is range 1 to 100
        if((number %3 == remainder1)and (number % 5 == remainder2)and(number % 7 == remainder3)): # Only if all cases match then print that number.
            print(f"Your number was {number}")
            print("How amazing is that?")

    
    end_game = input("Do you want to play again? Y to continue, N to quit ==>") #Asking the users if they want to quit or play
    print() 
    while not(end_game == "Y" or end_game == "N"):
        end_game = input("Do you want to play again? Y to continue, N to quit ==>")
        print() 
    
    
    



     
    
    
