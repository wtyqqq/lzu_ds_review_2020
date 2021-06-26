def order(sentence):
    # creates a tuple of (int, word) for each word in the sentence
    # we need a nested listed comprehension to iterate each letter in the word
    # [... for w in sentence.split() ...] -> for each word in the sentence
    # [... for l in w ...] -> for each letter in each word
    # [... if l.isdigit()] -> if the letter is a digit
    # [(int(l), w) ...] -> add a tuple of (int(letter), word) to the final list
    words = [(int(l), w) for w in sentence.split() for l in w if l.isdigit()]
    words.sort(key=lambda t: t[0])
    return " ".join(t[1] for t in words)

if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a"))
    print(order("4of Fo1r pe6ople g3ood th5e the2"))
    print(order(""))