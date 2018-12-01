frequency = 0
with open('day1-1.txt', 'rt') as input_file:
    while True:
        line = input_file.readline().strip()
        if not line:
            break
        frequency += int(line)
print(frequency)