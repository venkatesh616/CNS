from collections import Counter
import string

def letter_freq(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text=file.read()

        filtered_text=[char.lower() for char in text if char in string.ascii_letters]

        total_letters=len(filtered_text)

        freq=Counter(filtered_text)

        for letter in sorted(freq):
            percent=(freq[letter]/total_letters)*100
            print(f"{letter}: {freq[letter]} ({percent:.2f}%)")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

fie_path= input("Enter path: ")
letter_freq(fie_path)

    
