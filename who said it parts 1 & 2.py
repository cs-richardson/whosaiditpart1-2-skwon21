"""
Who Said It Part 1 & 2
San Kwon IB CS HL Y1

This algorithm generates dictionaries for Hamlet by William Shakespeare
and Pride and Prejudice by Jane Austen, and prints the words and the number
of times each word was repeated in both texts.

Resources:
https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
"""

# This function returns the same given word but with
# no capitals and no extra non-letters
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# This function returns a dictionary with each of the words in a given text
# along with the number of times the word appeared in the text
def get_counts(filename):
    text = open(filename)
    result_dict = {}
    word_count = 0
    for line in text:
        words = line.split()
        for word in words:
            word = normalize(word)
            if word != "":
                if word in result_dict:
                    result_dict[word] = result_dict[word] + 1
                else:
                    result_dict[word] = 1
                word_count = word_count + 1
    result_dict["_total"] = word_count
    text.close()
    return result_dict

shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride-and-prejudice.txt")

# This part prints out all the words along with how many times
# the word was repeated for both Hamlet and Pride and Prejudice.
# The dashes separate Hamlet from Pride and Prejudice.

for key in shakespeare_counts:
    print(key + ": " + str(shakespeare_counts[key]))

print("-----")

for key in austen_counts:
    print(key + ": " + str(austen_counts[key]))
