def get_rules(lines):
    rules = {}
    for i, line in enumerate(lines):
        line = line.strip()
        if line:
            first, second = line.split("|")
            if second not in rules.keys():
                rules[second] = set()
            rules[second].add(first)
        else:
            updates = lines[i + 1 :]
            break
    return rules, updates


def get_correct_and_incorrect_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []
    for update in updates:
        pages = update.strip().split(",")
        visited_pages = set()
        correct = True
        for page in pages:
            visited_pages.add(page)
            if page in rules.keys():
                applied_rules = rules[page].intersection(set(pages))
                if not applied_rules.issubset(visited_pages):
                    incorrect_updates.append(pages)
                    correct = False
                    break
        if correct:
            correct_updates.append(pages)
    return correct_updates, incorrect_updates


def find_next_page(rules, update, visited):
    return next(
        key
        for key in rules.keys()
        if key in update
        and key not in visited
        and update.isdisjoint(rules[key] - set(visited))
    )


def get_first_page(rules, update_set):
    keys_set = set(rules.keys())
    next_page = update_set.difference(keys_set)
    if next_page:
        next_page = next_page.pop()
    if not next_page:
        next_page = next(
            key
            for key in rules.keys()
            if key in update_set and update_set.isdisjoint(rules[key])
        )
    return next_page


def make_incorrect_updates_corrected(incorrect_updates, rules):
    keys_set = set(rules.keys())
    corrected = []
    for update in incorrect_updates:
        visited = []
        update_set = set(update)
        visited.append(get_first_page(rules, update_set))
        for _ in range(1, len(update)):
            next_page = find_next_page(rules, update_set, visited)
            visited.append(next_page)
        corrected.append(visited)
    return corrected


def calculate_sum_of_middle_pages(updates):
    result = 0
    for update in updates:
        middle_index = len(update) // 2
        result += int(update[middle_index])
    return result


if __name__ == "__main__":
    with open("05.txt", "r") as input_file:
        lines = input_file.readlines()

    rules, updates = get_rules(lines)
    correct, incorrect = get_correct_and_incorrect_updates(rules, updates)
    result = calculate_sum_of_middle_pages(correct)
    print(f"Correct: {result}")
    corrected = make_incorrect_updates_corrected(incorrect, rules)
    result = calculate_sum_of_middle_pages(corrected)
    print(f"Corrected: {result}")
