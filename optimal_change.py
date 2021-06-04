# Write your solution here!

# create Bills and Coins Dictionary
# TODO
# Correct execution (i.e. runs without any errors)
# Correct computation of monetary values in output
# Correct punctuation and grammar in output (commas, "and", etc...)
# Correct pluralization in output ("bills", "dimes", "pennies", etc..)
# Correct handling of edge cases / special cases (single denomination, exact payment, under payment)

# "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

BILL = {
    100: '$100 bill',
    50:  '$50 bill',
    20:  '$20 bill',
    10:  '$10 bill',
    5:   '$5 bill',
    1:   '$1 bill'
}

COIN = {
    0.25: 'quarter',
    0.10: 'dime',
    0.05: 'nickel',
    0.01: 'penny'
}

# str_msg = 'The optimal change for an item that costs '

def optimal_change(item_cost, amount_paid):
    change = 0

    #1. Check if amount_paid >= item_cost

    #2. function calculate dollars

    #3. function calculate coins



    if amount_paid >= item_cost:
        change = amount_paid - item_cost
        # string manipulation seperate dollars and cents
        dollar = float(f'{change:.0f}')
        cent   = float(f'{change:.2f}') - dollar
        # cent   = cent - dollar
        print(dollar)
        print(cent)

        # Start with dollars and take the highest difference with given denomination
        # while (change != 0):
        #     if (change >= 1000)

    else:
        return 'Insufficient amount.'

    return (f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is')


print(optimal_change(5.50,10))