# Write your solution here!
# create Bills and Coins Dictionary
# TODO
# Correct execution (i.e. runs without any errors)
# Correct computation of monetary values in output
# Correct punctuation and grammar in output (commas, "and", etc...)
# Correct pluralization in output ("bills", "dimes", "pennies", etc..)
# Correct handling of edge cases / special cases (single denomination, exact payment, under payment)

# optimal_change(62.13, 100)
# "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

# optimal_change(31.51, 50)
# "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."

import math

BILL = {
    100: '$100 ',
    50:  '$50 ',
    20:  '$20 ',
    10:  '$10 ',
    5:   '$5 ',
    1:   '$1 '
}

COIN = {
    25: 'quarter, ',
    10: 'dime, ',
    5: 'nickel, ',
    1: 'penny. '
}

def optimal_change(item_cost, amount_paid):
    # return string text
    change_str = f'The optimal change for an item that costs ' + f'${item_cost:.2f}' ' with an amount paid of $' f'{amount_paid} ' + 'is '

    # check to see if amount on hand is greater than item cost
    if amount_paid >= item_cost:
        change = amount_paid - item_cost
        # check to see if it is exact change
        if change == 0:
            return change_str + 'no change.'

        # string manipulation seperate dollars and cents
        dollar = float(f'{change:.0f}')
        cent   = float(f'{change:.2f}') - dollar 
        cent = round(cent * 100)   # Convert to integer

    else:
        return 'Insufficient amount.'
    # Calling dollar and coin function print out string.
    return (change_str + find_dollar(dollar) + find_coin(cent))

#2. function calculate dollars
def find_dollar(dollar):
    dollar_str = ''

    # number of bills
    hundred = 0
    fifty   = 0
    twenty  = 0
    ten     = 0
    five    = 0
    one     = 0

    while (dollar > 0):
        if (dollar >= 100):
            hundred += (dollar // 100)
            dollar = dollar - 100 * hundred
            if hundred >1 :
                dollar_str += str(f'{hundred:.0f} ') + BILL[100] + 'bills, '
            else:
                dollar_str += str(f'{hundred:.0f} ') + BILL[100] + 'bill, '

        elif (dollar >= 50):
            fifty += (dollar // 50)
            dollar = dollar - 50 * fifty
            if fifty > 1:
                dollar_str += str(f'{fifty:.0f} ') + BILL[50] + 'bills, '
            else:
                dollar_str += str(f'{fifty:.0f} ') + BILL[50] + 'bill, '

        elif (dollar >= 20):
            twenty += (dollar // 20)
            dollar = dollar - 20 * twenty
            if twenty > 1:
                dollar_str += str(f'{twenty:.0f} ') + BILL[20] + 'bills, '
            else:
                dollar_str += str(f'{twenty:.0f} ') + BILL[20] + 'bill, '

        elif (dollar >= 10):
            ten += (dollar // 10)
            dollar = dollar - 10 * ten
            if ten > 1:
                dollar_str += str(f'{ten:.0f} ') + BILL[10] + 'bills, '
            else:
                dollar_str += str(f'{ten:.0f} ') + BILL[10] + 'bill, '

        elif (dollar >= 5):
            five += (dollar // 5)
            dollar = dollar - 5 * five
            if five > 1:
                dollar_str += str(f'{five:.0f} ') + BILL[5] + 'bills, '
            else:
                dollar_str += str(f'{five:.0f} ') + BILL[5] + 'bill, '

        elif (dollar >= 1):
            one += (dollar // 1)
            dollar = dollar - 1 * one
            if one > 1:
                dollar_str += str(f'{one:.0f} ') + BILL[1] + 'bills, '
            else:
                dollar_str += str(f'{one:.0f} ') + BILL[1] + 'bill, '

    return dollar_str

#3. function calculate coins
def find_coin(cent):
    coin_str = ''
    # number of coins
    quarter = 0
    dime    = 0
    nickel  = 0
    penny   = 0 

    while (cent > 0):
        if (cent >= 25):
            quarter += (cent // 25)
            cent = cent - 25 * quarter
            if quarter > 1:
                coin_str += str(f"{quarter:.0f} ") + 'quarters, '
            else:
                coin_str += str(f"{quarter:.0f} ") + COIN[25]
            
        elif (cent >= 10):
            dime += (cent // 10)
            cent = cent - 10 * dime
            if dime > 1:
                coin_str += str(f"{dime:.0f} ") + 'dimes, '
            else:
                coin_str += str(f"{dime:.0f} ") + COIN[10]
            
        elif (cent >= 5):
            nickel += (cent // 5)
            cent = cent - 5 * nickel
            if nickel > 1:
                coin_str += str(f"{nickel:.0f} ") + 'nickels, '
            else:
                coin_str += str(f"{nickel:.0f} ") + COIN[5]
            
        elif (cent >= 1):
            penny += (cent // 1)
            cent = cent - 1 * penny
            if penny > 1:
                coin_str += str(f"and {penny:.0f} ") + 'pennies.'
            else:
                coin_str += str(f"and {penny:.0f} ") + COIN[1]

    return coin_str