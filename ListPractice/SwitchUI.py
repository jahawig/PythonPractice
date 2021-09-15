tester_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_position = int(input("Enter position (index = 0) of first number you want to switch: "))
while first_position > len(tester_list) - 1 or first_position < 0:
    print("That position is outside of the list.")
    first_position = int(input("Please put in an acceptable value: "))
second_position = int(input("Enter position (index = 0) of second number you want to switch: "))
while second_position > len(tester_list) - 1 or second_position < 0:
    print("That position is outside of the list.")
    second_position = int(input("Please put in an acceptable value: "))


# Switching first and last elements in a list
def switch_items_ui(example_list, pos_1, pos_2):
    # size = len(example_list)
    first = example_list[pos_1]
    # Replacing
    example_list[pos_1] = example_list[pos_2]
    example_list[pos_2] = first
    return example_list


print(switch_items_ui(tester_list, first_position, second_position))
