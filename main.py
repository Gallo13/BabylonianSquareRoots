# Created by: Jess Gallo
# Date Created: 07/01/2025
# Last Modified: 07/01/2025
# Description: The Babylonians had their own way of figuring out square roots to a very accurate number

import math as m

# Function to compute square root
def bab_sqrt(num):
    closest = closest_square(num)  # closest whole number to square
    csqrt = closest**2  # the squared closest whole number
    a = num - csqrt  # the number we want to square root - the squared whole number
    b = closest * 2  # closest whole number * 2

    s = closest + (a/b)

    return s


def closest_square(num):
    closest = 1
    min_diff = float('inf')  # use infinity so any real number's difference will be smaller
    for i in range(1, 11):
        square = i ** 2
        diff = abs(num - square)

        if diff < min_diff:
            closest = i
            min_diff = diff
    return closest


def correct_decimal_places(bsqr, msqr):
    bsqr_str = f"{bsqr}"
    msqr_str = f"{msqr}"
    count = 0
    for bs, ms in zip(bsqr_str, msqr_str):
        if bs == ms:
            if bs != '.':
                count += 1
        else:
            break
    return count


while True:
    try:
        # Calling function and using user input
        n = int(input('\nPlease enter a number you would like to find the square root to: '))
        bsqrt = bab_sqrt(n)
        msqrt = m.sqrt(n)
        places = correct_decimal_places(bsqrt, msqrt)

        print('Babylonian square root: ', bsqrt)
        print('True square root: ', m.sqrt(n))
        print(f"The Babylonian approximation was accurate to {places} numbers.")

    except:
        print('Please enter a numbers 0-9.')
