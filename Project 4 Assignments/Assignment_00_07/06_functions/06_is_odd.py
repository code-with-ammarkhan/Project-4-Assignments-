def main():
    for i in range(10, 20):  # Loop from 10 to 19 inclusive
        if is_odd(i):
            print(i, "odd")
        else:
            print(i, "even")

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    remainder = value % 2
    return remainder == 1

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
