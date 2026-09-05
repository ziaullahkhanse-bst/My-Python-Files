def order(sentence):
    """
    Sort words in a sentence based on the number they contain.
    
    Parameters:
    sentence (str): String with words containing numbers 1-9
    
    Returns:
    str: Sorted sentence
    """
    # If empty, return empty string
    if not sentence:
        return ""
    
    # Split into words
    words = sentence.split()
    
    # Create list to store sorted words
    sorted_words = [""] * len(words)
    
    # Place each word in its correct position
    for word in words:
        for char in word:
            if char.isdigit():
                position = int(char) - 1
                sorted_words[position] = word
                break
    
    # Join back into a sentence
    return " ".join(sorted_words)


# ========== TEST CASES ==========
if __name__ == "__main__":
    # Test 1: Basic example
    print(order("is2 Thi1s T4est 3a"))
    # Expected: "Thi1s is2 3a T4est"
    
    # Test 2: Longer example
    print(order("4of Fo1r pe6ople g3ood th5e the2"))
    # Expected: "Fo1r the2 g3ood 4of th5e pe6ople"
    
    # Test 3: Empty string
    print(order(""))
    # Expected: ""
    
    # Test 4: Simple numbers
    print(order("1one 3three 2two"))
    # Expected: "1one 2two 3three"
    
    # Test 5: Single word
    print(order("1hello"))
    # Expected: "1hello"