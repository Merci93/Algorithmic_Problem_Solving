def shortest_words(text: str|list):
    """
    Print the shortest word(s) in a string/list of words.

    :param text: String\list
    """
    def find_words(words: list):
        shortest_words = []
        shortest_word_length = float("inf")
        
        for word in words:
            word_length = len(word)
            
            if word_length < shortest_word_length:
                shortest_word_length = word_length
                shortest_words = [word]
                
            elif word_length == shortest_word_length:
                shortest_words.append(word)
                
        print(f"Shortest words are {shortest_words} with length {shortest_word_length}")
    
    if isinstance(text, str):
        words = text.replace(".", "").split(" ")
        find_words(words)
        
    if isinstance(text, list):
        find_words(text)


if __name__ == "__main__":
    shortest_words("The quick brown fox jumps over the lazy dog")
    shortest_words(["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"])
