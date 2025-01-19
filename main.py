def main():
    book_path = "books/frankenstein.txt" # This is the file path where Frankenstein is stored
    text = get_book_text(book_path) # Read the entire book into a string
    num_words = get_num_words(text) # Count the words in that string
    char_counts = count_character(text) # NEW: Counts all characters
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document") # Display the result
    sort_and_print_chars(char_counts) # Prints the character counts 
    print("--- End Report ---")


def get_num_words(text):
    words = text.split() # Split the text into a list of words using whitespace
    return len(words) # Count how many words are in the list


def get_book_text(path):
    with open(path) as f: # Open the file (and automatically close it when done)
        return f.read() # Read the entire file contents into a string


def count_character(text):
    # Convert everything to lowercase so 'A' and 'a' count as the same
    lowered_string = text.lower() 
    char_count = {} # Create empty dictionary to store our counts
    for char in lowered_string: # Look at each character one at a time
        if char.isalpha():
            # If we've seen this character before, add 1 to its count
            if char in char_count:
                char_count[char] += 1
            else:
            # If this is a new character, start its count at 1
                char_count[char] = 1
    return char_count # Return the completed dictionary

def sort_and_print_chars(char_counts):
    # Convert dictionary to list of dictionaries
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
     # Print each character count
    for item in chars_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

main()
    