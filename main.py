DELIMITER = ","

def collectWords():
    Words = ""
    while True:
        Word = input("Insert word(empty stops): ")
        if Word == "":
            break
        if Words == "":
            Words = Word
        else:
            Words += DELIMITER + Word
    return Words

def analyseWords(Words):
    if Words == "":
        word_list = []
    else:
        word_list = Words.split(DELIMITER)
    Amount = len(word_list)
    Characters = 0
    for Word in word_list:
        Characters += len(Word)
    if Amount > 0:
        Avg = Characters / Amount
    else:
        Avg = 0
    print("- {} Words".format(Amount))
    print("- {} Characters".format(Characters))
    print("- {:.2f} Average word length".format(Avg))
    return None

def main():
    print("Program starting.")
    Words = collectWords()
    analyseWords(Words)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
