import os

def part1():
    cwd = os.getcwd()
    file = open(cwd + "\D2_data")
    horizontal = 0
    depth = 0
    for line in file:
        line = line.replace("\n","")
        line = line.split(" ")
        if line[0] == "forward":
            horizontal += int(line[1])
        elif line[0] == "down":
            depth += int(line[1])
        else:
            depth -= int(line[1])
    return horizontal * depth

def part2():
    cwd = os.getcwd()
    file = open(cwd + "\D2_data")
    horizontal = 0
    depth = 0
    aim = 0
    for line in file:
        line = line.replace("\n","")
        line = line.split(" ")
        if line[0] == "forward":
            horizontal += int(line[1])
            depth += (aim * int(line[1]))
        elif line[0] == "down":
            aim += int(line[1])
        else:
            aim -= int(line[1])
    return horizontal * depth

print(part1())
print(part2())