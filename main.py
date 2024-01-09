def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_list = list(char_count(text).items())
    char_list.sort()

    # Printing Report on Frankenstein
    print(f"--- Start of report on {book_path} ---")
    print(f"{num_words} words found in the text\n")
    for ele in char_list:
        if ele[0].isalpha():
            print(f"the '{ele[0]}' character was found {ele[1]}")
    print("--- End Report ---")

# Break text into list of words using " " then return the count
def word_count(text):
    words = text.split(" ")
    return len(words)

# Retreive Text from a File at the provided path
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Return a list of characters that occur within the text 
def char_count(text):
    count = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
    
main()