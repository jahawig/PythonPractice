example_list = [1, 2, 3, 4, "test", "test", "test", "test", "testing", "list", "lists", "list"]


def unique_count(raw_list):
    unique_values = []
    for i in raw_list:
        if i not in unique_values:
            unique_values.append(i)
    return len(unique_values)


print(unique_count(example_list))
