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
    # change = 0
    

    #1. Check if amount_paid >= item_cost

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
        print('dollar function', dollar)

        while (dollar != 0):
            if (dollar >= 100):
                hundred += (dollar // 100)
                print('hundred:', hundred)
                dollar = dollar - 100 * hundred
                print('amount total:', dollar)
            elif (dollar >= 50):
                fifty += (dollar // 50)
                print('fifty:', fifty)
                dollar = dollar - 50 * fifty
                print('amount total:', dollar)
            elif (dollar >= 20):
                twenty += (dollar // 20)
                print('twenty:', twenty)
                dollar = dollar - 20 * twenty
                print('amount total:', dollar)
            elif (dollar >= 10):
                ten += (dollar // 10)
                print('tens:', ten)
                dollar = dollar - 10 * ten
                print('amount total:', dollar)
            elif (dollar >= 5):
                five += (dollar // 5)
                print('five:', five)
                dollar = dollar - 5 * five
                print('amount total:', dollar)
            elif (dollar >= 1):
                one += (dollar // 1)
                print('one:', one)
                dollar = dollar - 1 * one
                print('amount total:', dollar)
        print('final: ', dollar)      

    #3. function calculate coins
    def find_coin(cent):
        coin_str = ''

        # number of coins
        quarter = 0
        dime    = 0
        nickel  = 0
        penny   = 0 
        print('coin function', cent)
        while (cent != 0):
            if (cent >= 0.25):
                quarter += (cent // 0.25)
                print('quarter:', quarter)
                cent = cent - 0.25 * quarter
                print('amount total:', cent)
            elif (cent >= 0.10):
                dime += (cent // 0.10)
                print('dime:', dime)
                cent = cent - 0.10 * dime
                print('amount total:', cent)
            elif (cent >= 0.05):
                nickel += (cent // 0.05)
                print('nickel:', nickel)
                cent = cent - 0.10 * nickel
                print('amount total:', cent)
            elif (cent >= 0.01):
                penny += (cent // 0.01)
                print('penny:', penny)
                cent = cent - 0.10 * penny
                print('amount total:', cent)
        print('final coin: ', cent)  

    if amount_paid >= item_cost:
        change = amount_paid - item_cost

        # string manipulation seperate dollars and cents
        dollar = float(f'{change:.0f}')
        cent   = float(f'{change:.2f}') - dollar
        # print(dollar)
        # print(cent)

        # calling dollar and coin function to find number optimal amount
        # find_coin(cent)
        find_dollar(dollar)

    else:
        return 'Insufficient amount.'

    return (f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is')


print(optimal_change(1.5,5))