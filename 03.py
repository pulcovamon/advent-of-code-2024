import re

def mul(function):
    number1, number2 = function.replace("mul(", "").replace(")", "").split(",")
    return int(number1) * int(number2)

def process_memory(memory):
    result = 0
    for block in memory.split("do()"):
        block = block.split("don't()")[0]
        for function in re.findall(r"mul\(\d+,\d+\)", block):
            result += mul(function)
    return result
    
if __name__ == "__main__":
    with open("03.txt", "r") as input_file:
        memory = input_file.read()
    result = process_memory(memory)
    print(f"Result: {result}")
        