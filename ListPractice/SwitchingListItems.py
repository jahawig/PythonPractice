# Switching first and last elements in a list
def switch_items(example_list):
    size = len(example_list)
    first_value = example_list[0]
    # Replacing first value with the last
    example_list[0] = example_list[size-1]
    example_list[size-1] = first_value
    return example_list


tester_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
switch_items(tester_list)
