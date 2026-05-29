# Word Count Tool

from collections import Counter

print("===================================")
print("         WORD COUNT TOOL")
print("===================================")

filename = "sample.txt"

try:
    # Open and read file
    with open(filename, "r") as file:
        content = file.read()

    # Count characters
    characters = len(content)

    # Count lines
    lines = len(content.splitlines())

    # Count words
    words = content.split()
    word_count = len(words)

    # Convert words to lowercase for frequency analysis
    cleaned_words = [word.lower().strip(".,!?") for word in words]

    # Count frequency
    frequency = Counter(cleaned_words)

    # Display results
    print("\n===== ANALYSIS RESULT =====")
    print(f"Total Lines      : {lines}")
    print(f"Total Words      : {word_count}")
    print(f"Total Characters : {characters}")

    print("\n===== TOP 5 MOST COMMON WORDS =====")

    for word, count in frequency.most_common(5):
        print(f"{word} : {count}")

# File not found exception
except FileNotFoundError:
    print("\n❌ Error: File does not exist.")

# General exception
except Exception as e:
    print("\n❌ Error:", e)
