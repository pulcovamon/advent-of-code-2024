def binary_search(item, array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return 0 if item <= array[0] else 1
    middle_index = (len(array) - 1) // 2
    if item == array[middle_index]:
        return middle_index
    if item < array[middle_index]:
        return binary_search(item, array[:middle_index])
    return middle_index + binary_search(item, array[middle_index + 1:]) + 1


def insert(item, array):
    item = int(item)
    if array:
        array.insert(binary_search(item, array), item)
    else:
        array.append(item)
    return array


def read_lists(file_name):
    left_list = []
    right_list = []
    with open(file_name, "r") as input_file:
        for line in input_file.readlines():
            left, right = line.split("   ")
            left_list = insert(left, left_list)
            right_list = insert(right, right_list)
    return left_list, right_list


def pair_lists(left_list, right_list):
    distance = 0
    for left, right in zip(left_list, right_list):
        distance += abs(left - right)
    return distance


def calculate_similarity(left_list, right_list):
    score = 0
    current_index = 0
    for left in left_list:
        number_in_right = 0
        for right in right_list[current_index:]:
            current_index += 1
            if right > left:
                break
            if left == right:
                number_in_right += 1
        score += left * number_in_right
    return score
        

if __name__ == "__main__":
    left_list, right_list = read_lists("01.txt")
    distance = pair_lists(left_list, right_list)
    print(f"Distance: {distance}")
    score = calculate_similarity(left_list, right_list)
    print(f"Similarity score: {score}")

