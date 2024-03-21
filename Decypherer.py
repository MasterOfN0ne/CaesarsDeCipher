letters_numbers_og = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
    8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
    15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
    22: 'w', 23: 'x', 24: 'y', 25: 'z'
}
# ceaser's cipher originally involves shifting the value X times forward or backwards.
cipher = input("Enter your cyphered string: ")
X = int(input("How much would you like to shift by?: "))
list = [*cipher]
print(list)
for char in list:
    for key, value in letters_numbers_og.items():
        if value == char:
            # For this challenge, the shift is 15.
            C = (key + X) % 26
            print(letters_numbers_og[C], end="")
