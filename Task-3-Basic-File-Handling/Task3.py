# Basic File Handling Program

print("===================================")
print("     BASIC FILE HANDLING")
print("===================================")

filename = "sample.txt"

try:
    # Open and read file
    with open(filename, "r") as file:
        content = file.read()

    print("\nCurrent File Content:\n")
    print(content)

    # User input for find and replace
    old_word = input("\nEnter the word to find: ")
    new_word = input("Enter the replacement word: ")

    # Check if word exists
    if old_word in content:
        updated_content = content.replace(old_word, new_word)

        # Write updated content back to file
        with open(filename, "w") as file:
            file.write(updated_content)

        print("\n✅ Word replaced successfully!")
        print("\nUpdated File Content:\n")
        print(updated_content)

    else:
        print(f"\n❌ The word '{old_word}' was not found in the file.")

# File not found exception
except FileNotFoundError:
    print("\n❌ Error: File does not exist.")

# Permission error exception
except PermissionError:
    print("\n❌ Error: Permission denied.")

# General exception
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")
