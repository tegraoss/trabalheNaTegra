# Open file in read mode
try:
    TxtFile = open("texto.txt", "r")
except:
    print("Não foi possivel abrir o arquivo!")
    exit()
# Read data(string) and split into a list of words
Text = TxtFile.read()
Text = str(Text)

# Normalize word in lower case and remove
for Character in [',','.',';',':']:
    Text = Text.replace(Character, ' ')
Text = Text.lower()
# Sort for better processing
Text = Text.split()
Text.sort()
# Set variables
LastWord = ""
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
    print(Word[0] + " " + str(Word[1]))

# Print entire list
# for word in WordsList:
#     print(word[0] + "   Count: " + str(word[1]))
