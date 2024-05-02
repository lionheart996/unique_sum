def sum_unique(input):
    my_dict = {}
    total_sum = 0

    # Count occurrences of each number
    for num in input:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] += 1

    # Remove keys with values greater than 1
    for key in list(
            my_dict.keys()):  # Use list() to create a copy of keys to avoid modifying dictionary size during iteration
        if my_dict[key] > 1:
            del my_dict[key]

    # Calculate sum of unique numbers
    for key, value in my_dict.items():
        total_sum += key

    return total_sum

print(sum_unique([1,1,2,3]))