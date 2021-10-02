"""
Command line sandwich ordering app.
"""

import pyinputplus as pyip


def prompt_user_to_make_a_choice(header, lst):
    print(header)
    return pyip.inputMenu(lst, numbered=True)


def prompt_user_for_yes_or_no(header):
    print(header)
    return pyip.inputYesNo("> ")


def prompt_user_for_number_of_sandwiches(header):
    print(header)
    return pyip.inputInt("> ")


def output_selected_cheese():
    if WITH_CHEESE == "yes":
        print(f"- cheese: {CHEESE}")
    else:
        print("- no cheese")


def output_selected_element(label, element):
    print("{} {}".format(label, element))


BREADS = [
    'rye',
    'sourdough',
    'white',
]
BREAD = prompt_user_to_make_a_choice("\nWhat kind of bread would you like?",
                                     BREADS)
MEATS = [
    'ham',
    'roast beef',
    'turkey',
]
MEAT = prompt_user_to_make_a_choice("\nWhat kind of meat would you like?",
                                    MEATS)
WITH_CHEESE = prompt_user_for_yes_or_no("\nWould you like cheese?")
CHEESES = [
    "american",
    "cheddar",
    "provelone",
]
if WITH_CHEESE == "yes":
    CHEESE = prompt_user_to_make_a_choice("\nWhat kind of cheese would you "
                                          "like?", CHEESES)

WITH_MAYO = prompt_user_for_yes_or_no("\nWould you like mayo (yes or no)?")
WITH_MUSTARD = prompt_user_for_yes_or_no("\nWould you like mustard "
                                         "(yes or no)?")
WITH_LETTUCE_AND_TOMATO = prompt_user_for_yes_or_no("\nWould you like lettuce "
                                                    "and tomato (yes or no)?")

NUMBER_OF_SANDWICHES = prompt_user_for_number_of_sandwiches("\nHow many "
                                                            "sandwiches would "
                                                            "you like?")

print("\nyour sandiwch order")
output_selected_element("number of sandwiches:", NUMBER_OF_SANDWICHES)
output_selected_element("- bread:", BREAD)
output_selected_element("- meat:", MEAT)
output_selected_cheese()
output_selected_element("- mayo:", WITH_MAYO)
output_selected_element("- mustard:", WITH_MUSTARD)
output_selected_element("- lettuce and tomato:", WITH_LETTUCE_AND_TOMATO)
