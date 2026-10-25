DELIMITER = ","

def collectWords():
    words = []
    while True:
        word = input("Insert-word(empty-stops): ")
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
    Avg = char_count / word_count if word_count > 0 else 0
    
    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(Avg))

def main():
    print("Program-starting.")
    collected_words = collectWords()
    analyseWords(collected_words)
    print("Program-ending.")

if __name__ == "__main__":
    main()
