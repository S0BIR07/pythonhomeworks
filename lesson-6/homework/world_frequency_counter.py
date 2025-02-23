import string
try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        text = "".join(lines)
except FileNotFoundError:
    print(f"The file sample.txt does not exist. Creating it now.")
    input_text = input("Input text to save to the file: ")
    with open("sample.txt", "w") as file:
        file.write(input_text)
text = text.lower().translate(str.maketrans('', '', string.punctuation))
words = text.split()
words.sort(key=lambda word: words.count(word))
words_set = set(words)
dct = {word:words.count(word) for word in words_set}
n = int(input("How many top words: "))
top_words = sorted(dct.items(), key=lambda x: x[1], reverse=True)[:n]
print(f"Total words: {len(words)}")
output=f"Top {str(n)} most common words:\n"
for word, number in top_words:
    output+=(f"{word} - {str(number)} times\n")
print(output)
with open("word_count_report.txt", "w") as file:
    file.write(output)