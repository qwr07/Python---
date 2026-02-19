words = ["python" , "cod", "ia"]
words_lengths ={word:len(word) for word in words if word.count("o")}
print(words_lengths)