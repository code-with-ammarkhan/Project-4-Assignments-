def list_practice():
    print("=== List Practice ===")
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Length of fruit list:", len(fruit_list))
    fruit_list.append('mango')
    print("Updated fruit list:")
    for fruit in fruit_list:
        print(fruit)
    print()


def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."


def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."


def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."


def index_game():
    print("=== Index Game ===")
    lst = [1, 2, 3, 4, 5]
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        print("Result:", access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print("Updated list:", modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced list:", slice_list(lst, start, end))
    else:
        print("Invalid operation.")
    print()


def main():
    list_practice()
    index_game()


if __name__ == "__main__":
    main()
