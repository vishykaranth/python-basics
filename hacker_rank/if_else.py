#!/bin/python

# if __name__ == '__main__':
#     n = int(raw_input().strip())

n = 0
while (n < 30):
    if (n % 2 == 1) | ((n >= 6) & (n <= 20)):
        print n
        print('Weird')
    else:
        print n
        print('Not Weird')
    n = n + 1;
    print('\n')
