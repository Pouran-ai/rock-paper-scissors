import random

def get_user_choice():
    users=input("please choice:rock or paper or scissors: ")
    return users
def get_computer_choice():
    computer=random.choice(['rock','paper','scissors'])
    return computer
def determine_winner(users,computer):
    if users==computer:
        print('drawn game!')
    elif (users=='rock'and computer=='scissors') or \
        (users=='scissors'and computer=='paper') or \
        (users=='paper'and computer=='rock') :
         print(f'you win!{users} beats {computer}.')
    else:
        print(f'computer win! {computer} beats {users}')
def play_game():
    while True:
        print('-----new raund---')
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        determine_winner(user_choice,computer_choice)
        play_again=input('do you want to play again?(yes or no)? ').lower()
        if play_again!= 'yes':
            print('thanks for playing.Good bye')
            break
if __name__=='__main__':
 play_game()
            
            
               
            
            
            
            
        
            
        