claims = [] # tuple (shift right, shift down, width, height, id)
claimed_spaces = {}
with open('day3.txt', 'rt') as claims_file:
    while True:
        claim = claims_file.readline()
        if not claim:
            break
        claim = claim.strip()
        claim = claim.replace('#', '')
        claim = claim.replace(' @ ', ':')
        claim = claim.replace(' ', '')

        claim_split = claim.split(':')
        shift_split = claim_split[1].split(',')
        area_split = claim_split[2].split('x')

        shift_right, shift_down = int(shift_split[0]), int(shift_split[1])
        width, height = int(area_split[0]), int(area_split[1])

        claims.append((shift_right, shift_down, width, height, claim_split[0]))

        for w in range(width):
            for h in range(height):
                claim_space = '%s,%s' % (shift_right+w, shift_down+h)
                if claim_space in claimed_spaces:
                    claimed_spaces[claim_space] = 'X'
                else:
                    claimed_spaces[claim_space] = 'C'

def overlaps(claim, claimed_spaces):
    for w in range(claim[2]):
        for h in range(claim[3]):
            claim_space = '%s,%s' % (claim[0]+w, claim[1]+h)
            if claimed_spaces[claim_space] == 'X':
                return True
    return False

for claim in claims:
    if not overlaps(claim, claimed_spaces):
        print(claim[4])
        break