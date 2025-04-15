def count_even(lst):
    """
    Prints the number of even numbers in the list.
    """
    count = 0  # Counter for even numbers
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)

def get_list_of_ints():
    """
    Prompts user to enter integers until they press enter.
    Returns a list of the entered integers.
    """
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()
