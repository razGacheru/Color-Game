import time
import random

BUDGET = 10
COLORS = ['BLUE', 'RED', 'GREEN', 'YELLOW', 'WHITE', 'BLACK']
print(f'\nYOUR STARTING BUDGET IS ${BUDGET}. GOOD LUCK!\n')

while BUDGET > 0:
    playerColorBet = input("PICK A COLOR: ").upper()
    while True:
        if playerColorBet in COLORS:
            break
        print("INVALID BET. PLEASE TRY AGAIN")
        playerColorBet = input("\nPICK A COLOR: ").upper()

    playerMoneyBet = int(input("\nHOW MUCH DO YOU WANT TO BET?: "))
    while True:
        if playerMoneyBet > 0 and playerMoneyBet <= BUDGET:
            break
        print("INVALID BET. PLEASE TRY AGAIN")
        playerMoneyBet = int(input("\nHOW MUCH DO YOU WANT TO BET?: "))

    # Show winning color
    print('\nWinning color is ..')
    time.sleep(1.5)
    winningColor = random.choice(COLORS)
    print(f'{winningColor}\n')

    # Result
    if playerColorBet == winningColor:
        print(f'Congratulations, you won!')
        BUDGET += playerMoneyBet
    else:
        print(f'Better luck next time!')
        BUDGET -= playerMoneyBet
        if BUDGET == 0:
            print(f'You now have 0 balance. Thank you for playing.')
            exit()

    print(f'Current BUDGET: {BUDGET}\n')
    print('===================\n')
    playAgain = input("PLAY AGAIN? Y or N: ").upper()
    if playAgain == "Y":
        continue
    else:
        print('THANK YOU FOR PLAYING!\n')
        break
