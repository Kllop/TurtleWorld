import os

word = input("Press text: ")
text = list(word)
removeSumbol = []
for i in range(0, len(word)):
    letter = word[i]
    if(letter in removeSumbol):
        text[i] = ")"
        continue
    for j in range(i + 1, len(word)):
        if(word[j] == letter):
            text[i] = ")"
            removeSumbol.append(letter)
            break;
    else:
        text[i] = "("
text = "".join(text)
print(text)
os.system("pause")
