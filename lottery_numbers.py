import random

# Generate a random lottery ticket with 7 numbers from 0 to 9
ticket_lottery = random.sample(range(0, 10), k=7)

print("Provide 7 numbers from 0 to 9 (one by one- separated by spacebars):")
ticket_input = list(map(int, input().split()))

# Combine ticket_lottery and ticket_input with zip
result = list(zip(ticket_lottery, ticket_input))

# Display lottery ticket and user's choice
print(f'Lottery Ticket: {" ".join([str(i) for i in ticket_lottery])}')
print(f'User\'s Choice : {" ".join([str(i) for i in ticket_input])}')

# Display results
print(' \n ----------- Results ----------- ')
points = 0
# Iterate over both lists
for lottery, user_choice in result:
    if lottery == user_choice:
        print(f'{lottery} & {user_choice} - match! {chr(10004)}')
        # If a match, gain a point
        points += 1
    else:
        print(f'{lottery} & {user_choice} - no match! {chr(10060)}')

# Display total points
print('\nTotal points', points)

# Congratulatory messages based on the number of points
if points == 1:
    print('Congratulations! You got one number off the lottery!')
elif points == 2:
    print('Congratulations! You got two numbers off the lottery!')
elif points == 3:
    print('Congratulations! You got three numbers off the lottery!')
elif points == 4:
    print('Congratulations! You got four numbers off the lottery!')
elif points == 5:
    print('Congratulations! You got five numbers off the lottery!')
elif points == 6:
    print('Congratulations! You got six numbers off the lottery!')
elif points == 7:
    print('Congratulations! You got all numbers off the lottery!')
else:
    print('Sorry! You did not get any numbers off the lottery!')
