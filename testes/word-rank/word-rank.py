# Open file in read mode
TxtFile = open("texto.txt", "r")
# Read data(string) and split into a list of words
Text = TxtFile.read().split()
# Sort for better processing
Text.sort();

# Set variables
LastWord =  ""
WordsList = []
# Make a list of words and their occurance in tuples
for Word in Text:
    if(Word != LastWord):
        LastWord = Word
        WordsList.append((Word,Text.count(Word)))
# Sort by occurance
WordsList.sort(key=lambda word: word[1], reverse=True)

# Spread the word! At least 20 of them
for place in range(20):
    Word = WordsList[place]
    print(str(place + 1) + "st: " + Word[0] + "   Count: " + str(Word[1]))
