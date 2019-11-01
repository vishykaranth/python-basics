def fib(n):
    if n <= 0:
        print("Invalid Number")
    # First Number
    elif n == 1:
        return 0
    # Second Number
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
if __name__ == "__main__":
    n = 19
    print("{}th fibonacci number is: {}".format(n, fib(n)))