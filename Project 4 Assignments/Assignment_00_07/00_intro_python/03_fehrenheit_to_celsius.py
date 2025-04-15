def main():
    fehrenheit = float(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m"))
    celsius = (fehrenheit - 32) * 5.0 / 9.0
    print(f"Temperature: {fehrenheit}°F = {celsius:.2f}°C")

if __name__ == "__main__":
    main()
