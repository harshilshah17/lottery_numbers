import random

ticket_lottery = random.sample(range(0, 9), k=7)

print("Provide 7 numbers from 0 to 9 (one by one- separated by spacebars):")
ticket_input: list = list(map(int, input().split()))

# Combine ticket_lottery, and ticket_input with zip
result = list(zip(ticket_lottery, ticket_input))

# Display lottery ticket and User's choice 
print(f'Lottery Ticket: {" ".join([str(i) for i in ticket_lottery])}')
print(f'User\'s Choice : {" ".join([str(i) for i in ticket_input])}')

# Display results:
print(' \n ----------- Results ----------- ')
points = 0
# Iterate over both lists:
for lottery, user_choice in result:
    if lottery == user_choice:
        print(f'{lottery} & {user_choice} - match! {chr(10004)}')
        # If a match, gain a point
        points += 1
    else:
        print(f'{lottery} & {user_choice} - no match! {chr(10060)}')

# Display total points:
print('\nTotal points', points)