def is_save_step(lower, higher):
    return 1 <= higher - lower <= 3


def is_save(report):
    report[0] = int(report[0])
    increasing = int(report[1]) > report[0]
    level_removed = False
    for i in range(1, len(report)):
        report[i] = int(report[i])
        if increasing:
            save_step = is_save_step(report[i-1], report[i])
        else:
            save_step = is_save_step(report[i], report[i-1])
        if not save_step:
            if not level_removed:
                level_removed = True
                report[i] = report[i-1]
                continue
            return False
    return True


if __name__ == "__main__":
    number_of_save = 0
    with open("02.txt", "r") as input_file:
        for report in input_file.readlines():
            if is_save(report.strip().split(" ")):
                number_of_save += 1
    print(f"Number of save reports: {number_of_save}")