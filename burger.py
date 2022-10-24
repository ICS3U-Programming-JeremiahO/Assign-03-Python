#!/usr/bin/env python3
# Created By: Jeremiah Omoike
# Date: October 19 2022
# This program calculates the price of a large or small burger from wendys and displays the total to the user.
#  There are also options to include fries and/or a drink to the order and calculates the total price accordinly

from re import L, M
import constants


def main():

    # input/declaration of variables.Get size of burger, get fries choice, get drink choice.
    print("Welcome to Wendys! ")
    print("")
    print("What size of cheese burger do you want?")
    print("")
    burger_choice_as_string = input(
        "press 1 for medium, 2 for large and 0 for no burger:"
    )
    print()
    fries_choice_as_string = input("press 7 if you want fries and 0 if you dont:")
    print()
    drink_choice_as_string = input("press 8 if you want a drink and 0 if you dont:")
    print()
    user_input_one = 1
    user_input_two = 2
    user_input_seven = 7
    user_input_eight = 8
    user_input_zero = 0
    user_input_three = 3
    user_input_four = 4
    user_input_five = 5
    user_input_six = 6
    user_input_seven = 7
    user_input_eight = 8
    user_input_nine = 9
    # process and output. Calculate cost and display output for different choices

    try:
        # Try to cast the burger choice, fries choice, and drink choice as an integer
        burger_choice_as_string = int(burger_choice_as_string)
        fries_choice_as_string = int(fries_choice_as_string)
        drink_choice_as_string = int(drink_choice_as_string)
        #  This makes sure the  user input for choice of burger is 1,2 or 0. If user inputs any other number other than one, two or 0 then it will say "There is an error in your food selection", and automatically end the program
        if (
            burger_choice_as_string == user_input_three
            or burger_choice_as_string == user_input_four
            or burger_choice_as_string == user_input_five
            or burger_choice_as_string == user_input_six
            or burger_choice_as_string == user_input_seven
            or burger_choice_as_string == user_input_eight
            or burger_choice_as_string == user_input_nine
        ):
            print("Sorry, was an error in your food selection.")
            exit()
        # This makes sure that the user input for choice of fries is 7 or 0. If the user inputs any other number than 7 or zero then then the program will print(" There was an error in your food selection") then end.
        if (
            fries_choice_as_string == user_input_one
            or fries_choice_as_string == user_input_two
            or fries_choice_as_string == user_input_three
            or fries_choice_as_string == user_input_four
            or fries_choice_as_string == user_input_five
            or fries_choice_as_string == user_input_six
            or fries_choice_as_string == user_input_eight
            or fries_choice_as_string == user_input_nine
        ):
            print("Sorry, was an error in your food selection.")
            exit()
        # This makes sure that the user input for choice of drink is 8 or 0. If the user inputs any other number than 8 or zero then then the program will print(" There was an error in your food selection") then end.
        if (
            drink_choice_as_string == user_input_one
            or drink_choice_as_string == user_input_two
            or drink_choice_as_string == user_input_three
            or drink_choice_as_string == user_input_four
            or drink_choice_as_string == user_input_five
            or drink_choice_as_string == user_input_six
            or drink_choice_as_string == user_input_seven
            or drink_choice_as_string == user_input_nine
        ):
            print("Sorry, was an error in your food selection.")
            exit()
        # If statement to calculate the total price for just a Large burger.
        if (
            fries_choice_as_string == user_input_zero
            and burger_choice_as_string == user_input_two
            and drink_choice_as_string == user_input_zero
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_2))
        # if statement to calculate the price for a medium burger + fries
        if (
            fries_choice_as_string == user_input_seven
            and burger_choice_as_string == user_input_one
            and drink_choice_as_string == user_input_zero
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_3))
        # if statement to calculate the price for large burger + fries
        if (
            fries_choice_as_string == user_input_seven
            and burger_choice_as_string == user_input_two
            and drink_choice_as_string == user_input_zero
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_4))
        # if statement to calculate the price for medium burger plus fries and a drink
        if (
            fries_choice_as_string == user_input_seven
            and burger_choice_as_string == user_input_one
            and drink_choice_as_string == user_input_eight
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_5))
        # if statement to calculate the price for large burger + fries and a drink
        if (
            fries_choice_as_string == user_input_seven
            and burger_choice_as_string == user_input_two
            and drink_choice_as_string == user_input_eight
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_6))
        # if statement to calculate the price for just fries
        if (
            fries_choice_as_string == user_input_seven
            and burger_choice_as_string == user_input_zero
            and drink_choice_as_string == user_input_zero
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_7))
        # if statement to calculate the price for just a drink
        if (
            fries_choice_as_string == user_input_zero
            and burger_choice_as_string == user_input_zero
            and drink_choice_as_string == user_input_eight
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_8))
        # if statement to calculate the price for fries + a drink
        if (
            fries_choice_as_string == user_input_seven
            and burger_choice_as_string == user_input_zero
            and drink_choice_as_string == user_input_eight
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_9))
        # if statement to calculate the price for nothing
        if (
            fries_choice_as_string == user_input_zero
            and burger_choice_as_string == user_input_zero
            and drink_choice_as_string == user_input_zero
        ):
            print("")
            print("If you are not going to buy anything then leave!")
            exit()
        # if statement to calculate the price for a medium burger plus a drink
        if (
            fries_choice_as_string == user_input_zero
            and burger_choice_as_string == user_input_one
            and drink_choice_as_string == user_input_eight
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_10))
        # if statement to calculate the price for a large burger plus a drink
        if (
            fries_choice_as_string == user_input_zero
            and burger_choice_as_string == user_input_two
            and drink_choice_as_string == user_input_eight
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_11))
        # if statement to calculate the price for just a medium burger
        if (
            fries_choice_as_string == user_input_zero
            and burger_choice_as_string == user_input_one
            and drink_choice_as_string == user_input_zero
        ):
            print("")
            print("The total cost is = ${:,.2f}".format(constants.TOTAL_1))
    # if integer fails to cast the burger_choice_as_string or fries_choice_as_string or drink_choice_as_string to an int,
    #  then instead of the program crashing, it just says ""error"
    except Exception:
        print("")
        print(" Error, this is not an integer. ")
    finally:
        print("")
        print("Thank you for coming to wendys. Have a nice day!")


if __name__ == "__main__":
    main()
