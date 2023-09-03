sentence = "This is a test sentence with some repeated words and some repeated words"
words = []
current_word = ""
for char in sentence:
    if char == " ":
        if current_word != "":
            words.append(current_word)
            current_word = ""
    else:
        current_word += char
if current_word != "":
    words.append(current_word)
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
for word in word_counts:
    print(word," => ",word_counts[word])