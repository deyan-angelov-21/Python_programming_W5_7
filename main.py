DELIMITER = ","

def collectWords():
    words = []
    while True:
        word = input("insert-word (empty-stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)

def analyseWords(PWords):
    if PWords == "":
        word_list = []
    else:
        word_list = PWords.split(DELIMITER)
    
    word_count = len(word_list)
    char_count = sum(len(word) for word in word_list)
    avg_length = char_count / word_count if word_count > 0 else 0
    
    print(f"- {word_count} words")
    print(f"- {char_count} characters")
    print("- {:.2f} Average word length".format(avg_length))

def main():
    print("program starting.")
    collected_words = collectWords()
    analyseWords(collected_words)
    print("program ending.")

if __name__ == "__main__":
    main()
