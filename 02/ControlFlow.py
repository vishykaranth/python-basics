# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

# x = int(input("Please enter an integer: "))
x = 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print words

for i in range(5):
    print i

print range(5, 10)

print list(range(5))
print "------------------------------"
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print range(0, 10, 3)

print range(-10, -100, -30)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(range(10))

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b
    print()


fib(2000)




print "------------------------------ End 1"

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

print "------------------------------ End 2"

