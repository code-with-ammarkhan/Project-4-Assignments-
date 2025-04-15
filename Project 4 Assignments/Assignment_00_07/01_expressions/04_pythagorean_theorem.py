import math

def main():
    ab = float(input("Enter the length of the side AB: "))
    bc = float(input("Enter the length of the side BC: "))

    ac = math.sqrt(ab**2 + bc**2)

    print(f"The length of the hypotenuse is {ac}")

if __name__ == "__main__":
    main()
