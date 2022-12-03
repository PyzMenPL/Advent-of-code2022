with open('03input.txt', 'r') as oFile:
    # List of items that appear in both lists
    both = []

    # List of items, in one group
    group = []

    for line in oFile:
        # We add each line
        group.append(set(line[:-1]))

        # If we have 3 elves in a group
        if len(group) == 3:
            # For each character in the smallest set
            for letter in min(group):
                # Check if it occurs in the rest
                if letter in group[group.index(min(group)) - 1] and letter in group[group.index(min(group)) - 2]:
                    # Assign to a list
                    both.append(letter)

            # After finding a group of 3 elves, clear group
            group = []

    # No worries! I generated this :D
    values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
              'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34,
              'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
              'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

    # Total results
    suma = 0

    for letter in both:
        suma += values[letter]

    print(suma)
