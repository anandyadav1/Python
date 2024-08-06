def longestWords(filename):
    with open(filename,"r") as file:
        content=file.read()
        words=content.split()
        longest_words=max(words,key=len)
    return longest_words
filename="ln.txt"
longest_words=longestWords(filename)
print(f"longest words in these '{filename}' is: {longest_words}")