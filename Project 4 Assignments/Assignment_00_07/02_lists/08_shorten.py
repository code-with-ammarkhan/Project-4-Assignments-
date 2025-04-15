MAX_LENGTH: int = 3

def shorten(lst):
    """
    Agar list MAX_LENGTH se lambi ho, to last wale items hata do aur unko print karo.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

def get_lst():
    """
    User se ek ek item le kar list banata hai. Enter dabaane par ruk jaata hai.
    """
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()
