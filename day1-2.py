# Read in each line
lines = []
with open('day1.txt', 'rt') as input_file:
    while True:
        line = input_file.readline().strip()
        if not line:
            break
        lines.append(line)

# Convert each line to an integer
frequency_shifts = [int(line) for line in lines]

# Initialize flag for telling if duplicate is found
duplicate_frequency_found = False
# Initialize current frequency holder
current_fequency = 0
# Initialize set to hold past frequencies
previous_frequencies = set()
previous_frequencies.add(current_fequency)

# Search through frequency shifts repeatedly until duplicate is found
while not duplicate_frequency_found:
    for shift in frequency_shifts:
        # Update current frequency
        current_fequency += shift
        # Check if current frequency has been seen
        if current_fequency in previous_frequencies:
            # Exit
            duplicate_frequency_found = True
            break
        # Add current frequency to the set of past frequencies
        previous_frequencies.add(current_fequency)

# Print the first frequency reached twice
print(current_fequency)