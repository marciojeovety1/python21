print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()
    
print('Okay! Let\'s play:) ')
score = 0

answer = input('What does CPU stands for? ')

if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect, try again!')



answer = input('What does GPU stands for? ')

if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect, try again!')
    
    

answer = input('What does RAM stands for? ')

if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect, try again!')
    
    
answer = input('What does PSU stands for? ')

if answer.lower() == 'power supply':
    print('Correct!')
    score += 1
else:
    print('Incorrect, try again!')

print('-----------------------------------------------------------------------------------------------------------------')
print(f'You got {score} questions correct')
print(f'You got {(score/4)*100}%')
print('-----------------------------------------------------------------------------------------------------------------')

if score >= 2:
    print('WELCOME TO THE NEXT FASE')
    print('-------------------------------------------------------------------------------------------------------------')
else:
    print('Ohhh sorry buddy, try again and achieve at least 50%')
    
playing2 = input('Type Yes or No, to decide if you advance or you quit the program: ')

if playing2.lower() != 'yes':
    quit()

print('So let\'s play')

score2 = 0
print('---------------------------------------------------------------------------------------')
answer2 = input('Name a Programming Language that starts with P and ends with n: ')

if answer2.lower() == 'python':
    print('Correct')
    score2 += 1
else:
    print('Incorrect!')
    
    
print('---------------------------------------------------------------------------------------')
answer2 = input('Name a Programming Language that starts with J and ends with t: ')

if answer2.lower() == 'javascript':
    print('Correct')
    score2 += 1
else:
    print('Incorrect!')
    
    
print('---------------------------------------------------------------------------------------')
print(f'You got {score2} correct answers in Level 2')
print(f'You Got {(score2/2)*100}%, IN LEVEL 2.')
print('---------------------------------------------------------------------------------------')