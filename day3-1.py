claims = {}
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

        for w in range(width):
            for h in range(height):
                claim_space = '%s,%s' % (shift_right+w, shift_down+h)
                if claim_space in claims:
                    claims[claim_space] = 'X'
                else:
                    claims[claim_space] = 'C'

print(len([ claims[claim_space] for claim_space in claims if claims[claim_space] == 'X' ]))
        