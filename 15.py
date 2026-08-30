#Project 15: Rock-Paper-Scissors Game 🎮

import random
def  game():

    while True:
        user_choice=input("Enter your choice:")
        computer_choice=random.choice(['rock','paper','scissors'])

        if user_choice=='rock' and computer_choice=='paper':
                     print("computer win")
        elif user_choice=='rock' and computer_choice=='scissors':  
                     print("you  win")
        elif user_choice=='rock' and computer_choice=='rock':  
                     print("game draw")    
        elif user_choice=='paper' and computer_choice=='rock':  
                     print("you win")   
        elif user_choice=='paper' and computer_choice=='scissors':  
                    print("computer win")      
        elif user_choice=='paper' and computer_choice=='paper':  
                    print("game draw")  
        elif user_choice=='scissors' and computer_choice=='rock':  
                    print("computer win")   
        elif user_choice=='scissors' and computer_choice=='paper':  
                     print("you win")  
        elif user_choice=='scissors' and computer_choice=='scissors':  
                    print("game draw")  
        else:
         print("incorrect input")   

        if (input("Do you want to play again? (yes/no)"))=="yes":
            continue
        else:
          print("END GAME")
        break

game()            

                                     

