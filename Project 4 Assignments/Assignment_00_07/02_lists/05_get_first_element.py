def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])

# Function to get list from user input
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

# Main function
def main():
    lst = get_lst()
    get_first_element(lst)

# Boilerplate to run main
if __name__ == '__main__':
    main()
