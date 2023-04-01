#!/usr/bin/env python

def is_acceptable(password, output):
    has_vowel = False
    three_consecutive = False
    two_occurences = False

    # 1: Check for at least one vowel.
    vowels = set('aeiou')
    for char in password:
        if char in vowels:
            has_vowel = True
            break

    # 2: Check for three consecutive vowels or three consecutive consonants. (Sliding Window)
    char_window = password[:3]
    for i in range(3, len(password)):
        if all(c in vowels for c in char_window) or all(c not in vowels for c in char_window):
            three_consecutive = True
        char_window = char_window[1:] + password[i]

    # 3: Check for two consecutive occurrences of the same letter, except for 'ee' or 'oo'.
    prev_char = ''
    for char in password:
        if char == prev_char and char not in 'eo':
            two_occurences = True
        prev_char = char

    # Do nothing if word == 'end'
    if password == 'end':
        return
    # Acceptable conditions
    elif has_vowel and not three_consecutive and not two_occurences:
        output.write('<' + password[:-1] + '> is acceptable.\n')
    else:
        output.write('<' + password[:-1] + '> is not acceptable.\n')

if __name__ == "__main__":
    out = open('test.out', 'w')
    with open('./say.in') as f:
        lines = f.readlines()

        for line in lines:
            is_acceptable(line, out)
