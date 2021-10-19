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


def output_order_summary():
    print("\norder summary")
    for sandwich in SANDWICHES:
        output_selected_element(f"\nnumber of sandwiches:", sandwich[6])
        output_selected_element("bread:", sandwich[0])
        output_selected_element("meat:", sandwich[1])
        output_selected_element("cheese", sandwich[2])
        output_selected_element("mayo:", sandwich[3])
        output_selected_element("mustard:", sandwich[4])
        output_selected_element("lettuce and tomato:", sandwich[5])


SANDWICHES = []

while True:
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
    WITH_CHEESE = prompt_user_for_yes_or_no("\nWould you like cheese "
                                            "(yes or no?")
    CHEESES = [
        "american",
        "cheddar",
        "provelone",
    ]
    if WITH_CHEESE == "yes":
        CHEESE = prompt_user_to_make_a_choice("\nWhat kind of cheese would you "
                                              "like?", CHEESES)
    else:
        CHEESE = "no"

    WITH_MAYO = prompt_user_for_yes_or_no("\nWould you like mayo (yes or no)?")
    WITH_MUSTARD = prompt_user_for_yes_or_no("\nWould you like mustard "
                                             "(yes or no)?")
    WITH_LETTUCE_AND_TOMATO = prompt_user_for_yes_or_no("\nWould you like "
                                                        "lettuce and tomato "
                                                        "(yes or no)?")

    NUMBER_OF_SANDWICHES = prompt_user_for_number_of_sandwiches("\nHow many "
                                                                "sandwiches "
                                                                "would you "
                                                                "like?")

    print("\nWould you like to order another sandwich?")
    ORDER_ANOTHER = pyip.inputYesNo("> ", blank=True)
    SANDWICH = (BREAD, MEAT, CHEESE, WITH_MAYO, WITH_MUSTARD,
                WITH_LETTUCE_AND_TOMATO, NUMBER_OF_SANDWICHES)
    SANDWICHES.append(SANDWICH)
    if ORDER_ANOTHER == "no":
        break

output_order_summary()
