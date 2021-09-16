tester_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 7, 6, 7, 8]


def filter_by_count(full_list, count_cutoff):

    filtered_list = []
    for i in full_list:
        item_count = full_list.count(i)
        if item_count >= count_cutoff and i not in filtered_list:
            filtered_list.append(i)
    return filtered_list


print(filter_by_count(tester_list, 2))
