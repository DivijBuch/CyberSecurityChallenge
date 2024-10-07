from collections import Counter

def count_top_letters(string, top_n=5):
    # Convert to lowercase and filter out non-letter characters
    letters_only = [char.lower() for char in string if char.isalpha()]
    letter_counts = Counter(letters_only)
    # Get the top 'n' most common letters
    top_letters = letter_counts.most_common(top_n)
    return top_letters

# Example usage
input_string = input("Enter your string: ")
top_5_letters = count_top_letters(input_string)
print("Top 5 most repeated letters:")
for letter, count in top_5_letters:
    print(f"{letter}: {count}")
