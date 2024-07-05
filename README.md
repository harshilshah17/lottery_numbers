# Lottery Ticket Matching Script

This is a simple Python script that simulates a lottery ticket matching game. The script generates a random lottery ticket with 7 numbers and prompts the user to input their own 7 numbers. It then compares the user's numbers with the lottery ticket and displays the results, including the total number of matches and a congratulatory message based on the number of matches.

## Features

- Generates a random lottery ticket with 7 numbers from 0 to 9.
- Prompts the user to input 7 numbers from 0 to 9.
- Compares the user's numbers with the lottery ticket.
- Displays the lottery ticket, user's choices, and the results of the comparison.
- Provides a congratulatory message based on the number of matches.

## How to Use

1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using the command: `python lottery_ticket.py`.
5. When prompted, enter 7 numbers from 0 to 9, separated by spaces.
6. The script will display the randomly generated lottery ticket, your chosen numbers, and the results.

## Example

```sh
$ python lottery_ticket.py
Provide 7 numbers from 0 to 9 (one by one- separated by spacebars):
1 3 5 7 9 2 4
Lottery Ticket: 8 3 0 7 2 4 9
User's Choice : 1 3 5 7 9 2 4

 ----------- Results -----------
8 & 1 - no match! ✗
3 & 3 - match! ✓
0 & 5 - no match! ✗
7 & 7 - match! ✓
2 & 9 - no match! ✗
4 & 2 - no match! ✗
9 & 4 - no match! ✗

Total points 2
Congratulations! You got two numbers off the lottery!
