def count_letters(filename):
    freq = {}
    with open(filename, 'r') as file:
        text = file.read()
        for char in text:
            if 'A' <= char <= 'Z':
                char = chr(ord(char) + 32)  # Convert to lowercase
            if 'a' <= char <= 'z':
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
    return freq

# File names to analyze
files = ['file1.txt']

# Analyze and print results
for file in files:
    freq = count_letters(file)
    print(f"\nLetter Frequency in {file}:")
    for letter in sorted(freq.keys()):
        print(f"{letter}: {freq[letter]}")
