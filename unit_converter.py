#!/usr/bin/env python3
"""
Unit Converter - A simple command-line tool for converting between different units.
Initial version supports temperature conversions between Celsius and Fahrenheit.
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

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
            print("0. Back to main menu")
            
            # Get user's choice for temperature conversion
            temp_choice = input("\nSelect temperature conversion (0-2): ")
            
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
            
            else:
                print("\nInvalid choice. Please try again.")
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()