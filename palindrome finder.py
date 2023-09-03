#Harshi Chalamani

def is_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word = ''.join(word.split()).lower()
    return cleaned_word == cleaned_word[::-1]

def find_palindromes(word_list):
    palindromes = [word for word in word_list if is_palindrome(word)]
    return palindromes

if __name__ == "__main__":
    words = ["radar", "hello", "level", "deified", "world", "python", "madam"]
    
    palindrome_list = find_palindromes(words)
    
    if palindrome_list:
        print("Palindromes found in the list:")
        for word in palindrome_list:
            print(word)
    else:
        print("No palindromes found in the list.")
