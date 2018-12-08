with open('day8.txt') as f:
    lic = [int(component) for component in f.readline().strip().split(' ')]

def parse_license(lic):
    children = lic[0]
    meta_count = lic[1]

    # Base Case
    if children == 0:
        return sum(lic[2:2+meta_count]), 2+meta_count

    # Recursive Case
    meta_sum = 0
    start = 2
    # Sum of children
    for _ in range(children):
        temp_sum, temp_start = parse_license(lic[start:])
        meta_sum += temp_sum
        start += temp_start
    # Sum of own
    meta_sum += sum(lic[start:start+meta_count])
    return meta_sum, start+meta_count

print(parse_license(lic)[0])