def build_char_counts(box_id):
    ''' Builds a dict containing a count of each character in a given box id '''
    char_counts = {}
    for char in box_id:
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1
    return char_counts

def contains_duplicate_char(box_id):
    ''' Checks to see if a given box id has exactly two of any character '''
    # Count the occurances of each char in the box id
    char_counts = build_char_counts(box_id)
    # Check if any character appears in the box id exactly twice
    for char in char_counts:
        if char_counts[char] == 2:
            return True
    # A duplicate character was not found
    return False

def contains_triplicate_char(box_id):
    ''' Checks to see if a given box id has exactly three of any character '''
    # Count the occurances of each character in the box id
    char_counts = build_char_counts(box_id)
    # Check if any character appears in the box id exactly three times
    for char in char_counts:
        if char_counts[char] == 3:
            return True
    # A triplicate character was not found
    return False

if __name__ == '__main__':
    # Create a count for duplicates and triplicates
    duplicate_count = 0
    triplicate_count = 0
    # Go through each box id and count up the ones which are duplicates and triplicates
    with open('day2.txt', 'rt') as candidate_box_ids_file:
        while True:
            # Read in a candidate box id from the candidate box ids file
            box_id = candidate_box_ids_file.readline().strip()
            # Check to make sure a line was read
            if not box_id:
                break
            # Check for exact duplicate or triplicate characters in the id, increase respectively if found
            if contains_duplicate_char(box_id):
                duplicate_count += 1
            if contains_triplicate_char(box_id):
                triplicate_count += 1
    # Create the checksum
    print(duplicate_count * triplicate_count)