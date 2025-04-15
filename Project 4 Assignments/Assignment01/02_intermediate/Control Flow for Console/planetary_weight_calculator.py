"""
Planetary Weight Calculator
Prompts the user for a weight on Earth and a planet (in separate inputs). 
Then prints the equivalent weight on that planet.

Note: User should type in a planet with the first letter as uppercase. 
No need to handle invalid planet names.
"""

# Gravitational constants relative to Earth's gravity
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14


def main():
    # Prompt user for Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt user for planet name
    planet = input("Enter a planet: ")

    # Determine gravity multiplier
    if planet == "Mercury":
        gravity = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity = VENUS_GRAVITY
    elif planet == "Mars":
        gravity = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity = URANUS_GRAVITY
    else:  # Neptune
        gravity = NEPTUNE_GRAVITY

    # Calculate planetary weight
    planetary_weight = earth_weight * gravity
    rounded_weight = round(planetary_weight, 2)

    # Print result
    print("The equivalent weight on " + planet + ": " + str(rounded_weight))


if __name__ == "__main__":
    main()
