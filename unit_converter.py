#!/usr/bin/env python3
"""
Unit Converter - A simple command-line tool for converting between different units.
Initial version supports temperature conversions between Celsius and Fahrenheit.
"""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


# Conversion function for celsius to kelvin
def CelsiusToKelvin(c):
    # adds 273.15 to convert
    k = c + 273.15
    return k


# Fahrenheit to Kelvin conversion
def f_to_K(f):
    # First convert to C
    c = fahrenheit_to_celsius(f)
    # Now convert C to K
    return c + 273.15


# Conversion from K to C
def kelvinToCelsius(kelvin):
    """This converts from K to C"""
    return kelvin - 273.15


# K -> F conversion function
def KelvinToFahrenheit(K):
    # Two-step process
    c = kelvinToCelsius(K)
    f = celsius_to_fahrenheit(c)
    return f


def get_numeric_input(prompt):
    """Get and validate numeric input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    """Main function to handle the unit conversion program."""
    print("Welcome to the Unit Converter!")

    while True:
        # Display available conversion types
        print("\nAvailable conversion types:")
        print("1. Temperature")
        print("0. Exit")

        # Get user's choice for conversion type
        conversion_type = input("\nSelect conversion type (0-1): ")

        if conversion_type == "0":
            print("Thank you for using the Unit Converter. Goodbye!")
            break

        elif conversion_type == "1":
            # Display temperature conversion options
            print("\nTemperature conversion options:")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            print("5. Fahrenheit to Kelvin")
            print("6. Kelvin to Fahrenheit")
            print("0. Back to main menu")

            # Get user's choice for temperature conversion
            temp_choice = input("\nSelect temperature conversion (0-6): ")

            if temp_choice == "0":
                continue

            elif temp_choice == "1":
                value = get_numeric_input("\nEnter temperature in Celsius: ")
                result = celsius_to_fahrenheit(value)
                print(f"\n{value} °C = {result:.2f} °F")

            elif temp_choice == "2":
                value = get_numeric_input("\nEnter temperature in Fahrenheit: ")
                result = fahrenheit_to_celsius(value)
                print(f"\n{value} °F = {result:.2f} °C")

            elif temp_choice == "3":
                value = get_numeric_input("\nEnter temperature in Celsius: ")
                result = CelsiusToKelvin(value)
                print(f"\n{value} °C = {result:.2f} K")

            elif temp_choice == "4":
                value = get_numeric_input("\nEnter temperature in Kelvin: ")
                # Check if temperature is below absolute zero
                if value < 0:
                    print("\nWarning: Temperature below absolute zero!")
                result = kelvinToCelsius(value)
                print(f"\n{value} K = {result:.2f} °C")

            elif temp_choice == "5":
                value = get_numeric_input("\nEnter temperature in Fahrenheit: ")
                result = f_to_K(value)
                print(f"\n{value} °F = {result:.2f} K")

            elif temp_choice == "6":
                val = get_numeric_input("\nEnter temperature in Kelvin: ")
                if val < 0: print("\nWarning: Temperature cannot be below absolute zero!")
                res = KelvinToFahrenheit(val)
                print(f"\n{val} K = {res:.2f} °F")

            else:
                print("\nInvalid choice. Please try again.")

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()