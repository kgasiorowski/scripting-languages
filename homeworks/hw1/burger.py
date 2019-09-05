# Kuba Gasiorowski
# 109776237
# kgasiorowski
#
# CSE 337 (Fall 2019)
# Minor Homework 1, Problem 1


def burger(order):

    proteins = {
        'B': 2.00,
        'T': 2.5,
        'V': 2.25
    }

    toppings = 'ltopjcbsmf'
    condiments = 'kuyaq'

    num_proteins = 0
    num_toppings = 0
    num_condiments = 0
    cost = 0

    for letter in order:
        if letter in proteins:
            cost += proteins[letter]
            num_proteins += 1
        elif letter in toppings:
            cost += 0.5
            num_toppings += 1
        elif letter in condiments:
            num_condiments += 1
        else:
            return 'unrecognized order code'

    if num_proteins != 1 or num_toppings > 5 or num_condiments > 2:
        return 'invalid order'
    else:
        return cost


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('burger("Bck"):', burger("Bck")) # simple cheeseburger
    print()
    print('burger("Tpmlmy"):', burger("Tpmlmy")) # turkey burger w/ stuff
    print()
    print('burger("altop"):', burger("altop")) # error: no protein
    print()
    print('burger("VtojsT"):', burger("VtojsT")) # error: too many protein choices
    print()
    print('burger("lsucjV"):', burger("lsucjV")) # okay; protein at end
    print()
    print('burger("Bqcbksmfy"):', burger("Bqcbksmfy")) # error: too many condiments
    print()
    print('burger("Toxpk"):', burger("Toxpk")) # error: invalid character (x)
    print()
    print('burger("Vqltopjm"):', burger("Vqltopjm")) # error: too many toppings
    print()

