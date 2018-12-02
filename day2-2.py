def diff_by_one(box_id1, box_id2):
    ''' Returns true if the two given box ids differ by only one character '''
    differences = 0
    # Go through each character in the box ids
    for i in range(len(box_id1)):
        # Check if the positional character is the same
        if box_id1[i] != box_id2[i]:
            # Add 1 to differences if not
            differences += 1
            # Check if there's more than one difference
            if differences > 1:
                return False
    # Check if differences isn't 1
    if differences != 1:
        return False
    # Return true since there was only one difference
    return True

def find_common_letters(box_id1, box_id2):
    ''' Returns a string of the common letters between two box ids '''
    common_letters = ''
    # Go through each character in the box ids
    for i in range(len(box_id1)):
        # Check if the characters at that position are the same
        if box_id1[i] == box_id2[i]:
            # Add to our string of common letters
            common_letters += box_id1[i]
    return common_letters

if __name__ == '__main__':
    box_ids = []
    with open('day2.txt', 'rt') as box_ids_file:
        # Read each line
        while True:
            # Read a box id
            box_id = box_ids_file.readline().strip()
            # Quit reading if we're no longer receiving box ids
            if not box_id:
                break
            # Add to our list of box ids
            box_ids.append(box_id)
    
    # Create a flag for determining if we've found similar ids
    found_similar_ids = False

    # Go through each comparison
    for i in range(len(box_ids)):
        # Exit if we've found similar ids
        if found_similar_ids:
            break
        for j in range(i, len(box_ids)):
            # Check if the two current ids are different by one
            if diff_by_one(box_ids[i], box_ids[j]):
                # Print the common letters and exit
                print(find_common_letters(box_ids[i], box_ids[j]))
                found_similar_ids = True
                break