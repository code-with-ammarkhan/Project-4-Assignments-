def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    # Example usage:
    n = int(input("Enter a number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    result = in_range(n, low, high)
    print("Is the number in range?", result)

if __name__ == '__main__':
    main()
