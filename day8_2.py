with open('day8.txt') as f:
    lic = [int(component) for component in f.readline().strip().split(' ')]

def parse_license(lic):
    children = lic[0]
    meta_count = lic[1]

    # Base Case
    if children == 0:
        return sum(lic[2:2+meta_count]), 2+meta_count

    # Recursive Case
    start = 2
    # Get children metadata
    child_values = {}
    for i in range(children):
        temp_val, temp_start = parse_license(lic[start:])
        child_values[i] = temp_val
        start += temp_start
    # Get sum of children indicated by indicies
    indicies = lic[start:start+meta_count]    
    root_sum = sum([child_values[i-1] for i in indicies if i-1 in child_values])
    # Recursive return
    return root_sum, start+meta_count

print(parse_license(lic)[0])