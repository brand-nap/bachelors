"""
Author: Brandon Perez
Class: CSCI 1411-006
Due Date: 10/20/23
Description: flips a coin 1000 times and checks for heads. Logic error: didn't increment flips.
Status: Works as Expected

"""
def main():
    import random
    print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
    input()
    flips = 0
    heads = 0
    while flips < 1000:
        flips=flips+1;
        if random.randint(0, 1) == 1:
            heads = heads + 1
            print ('Number of heads', heads)
        if flips == 900:
            print('900 flips and there have been ' + str(heads) + ' heads.')
        if flips == 100:
            print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
        if flips == 500:
            print('Half way done, and heads has come up ' + str(heads) + ' times.')

    print()
    print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
    print('Were you close?')
