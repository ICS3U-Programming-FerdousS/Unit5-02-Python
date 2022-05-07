#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: May, 4, 2022
# This program asks the user for base and height of triangle
# then calcuate the area of triangle using calculate_area function.

def calculate_area(base, height):

    # doing calculation
    area = base * height / 2

    # display answer
    print("The area of the Triangle is {:.2f} cm²".format(area))


def main():

    try:
        # Get user inputs and convert it to float
        base_string = input("Enter the base of the triangle (cm): ")
        height_string = input("Enter the height of the triangle (cm): ")
        base_float = float(base_string)
        height_float = float(height_string)
        print("")
        
        # check user input is 0 or less
        if (height_float <= 0 or base_float <= 0):
            print("Input cannot be 0 or less.")
        else:
            # calling the function
            calculate_area(base_float, height_float)

    # invalid input
    except Exception:
        print("")
        print("Invalid input. Input was not a number.")


if __name__ == "__main__":
    main()
