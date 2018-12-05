import string

polymer = ''
with open('day5.txt') as polymer_file:
    polymer = polymer_file.readline().strip()

low_alpha = list(string.ascii_lowercase)
up_alpha = list(string.ascii_uppercase)

def react(poly):
    l_alpha = list(string.ascii_lowercase)
    u_alpha = list(string.ascii_uppercase)
    while True:
        poly_len = len(poly)
        edit_made = False
        for i in range(len(l_alpha)):
            poly = poly.replace(l_alpha[i]+u_alpha[i], '')
            poly = poly.replace(u_alpha[i]+l_alpha[i], '')
            if(len(poly) < poly_len):
                edit_made = True
        if not edit_made:
            break
    return poly

    

shortest_poly = None
for i in range(len(low_alpha)):
    temp_poly = polymer.replace(low_alpha[i], '')
    temp_poly = temp_poly.replace(up_alpha[i], '')
    temp_poly = react(temp_poly)
    if i == 0:
        shortest_poly = len(temp_poly)
    if len(temp_poly) < shortest_poly:
        shortest_poly = len(temp_poly)
print(shortest_poly)

