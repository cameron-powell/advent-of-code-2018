polymer = ''
with open('day5.txt') as polymer_file:
    polymer = polymer_file.readline().strip()

while True:
    caps_polymer = polymer.upper()
    edit_made = False
    for i in range(0, len(polymer)-2):
        if caps_polymer[i] == caps_polymer[i+1]:
            if polymer[i] != polymer[i+1]:
                polymer = polymer[:i] + polymer[i+2:]
                edit_made = True
                break
    if not edit_made:
        break
print(len(polymer))

