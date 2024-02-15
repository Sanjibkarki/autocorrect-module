f = open("word.txt","r")
alphabet = "abcdefghijklmnopqrstuvwxyz"
c = f.readlines()
f.close()
wordsall = [word.strip() for word in c]

def editDistance1(word):
    word = list(word.lower())
    results = []
    transpose = []
    # Adding any one character (from the alphabet) anywhere in the word.
    for i in range(len(word)):
        for j in range(len(alphabet)):
            newword = list(word)
            newword.insert(i,alphabet[j])
            results.append(''.join(newword))
    # Removing any one character from the word.
    if len(word) > 1:
        for i in word:
            newword = list(word)
            newword.remove(i)
            results.append(''.join(newword))
    # Transposing (switching) the order of any two adjacent characters in a word.
    if len(word) > 1:
        for i in range(len(word)):
            newword = list(word)
            c = newword.pop(i)
            newword.insert(i+1,c)
            results.append(''.join(newword))
    # Substituting any character in the word with another character.
    for i in range(len(word)):
        for j in range(len(alphabet)):
            newword = list(word)
            newword.remove(word[i])
            newword.insert(i,alphabet[j])
            results.append(''.join(newword))
    return results

def correct(word):
    if word in wordsall:
        return word
    editDistance1word = editDistance1(word)
    editDistance2word = []
    for i in range(len(editDistance1word)):
        if editDistance1word[i] in wordsall:
            return editDistance1word[i]
        
    return None

  