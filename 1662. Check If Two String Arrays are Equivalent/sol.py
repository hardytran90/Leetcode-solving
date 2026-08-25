
word1 = ["ab", "c"]
word2 = ["a", "bc"]

string1 = ''
string2 = ''
for i in range(len(word1)):
    string1 = string1 + word1[i]

for i in range(len(word2)):
    string2 = string2 + word2[i]

if string1 != string2:
    print(False)
else:
    print(True)
