filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()

   
    lines = text.splitlines()
    line_count = len(lines)

    
    words = text.split()
    word_count = len(words)

    
    character_count = len(text)

    print("\n===== FILE DETAILS =====")
    print("Number of Lines     :", line_count)
    print("Number of Words     :", word_count)
    print("Number of Characters:", character_count)

except FileNotFoundError:
    print("File not found!")