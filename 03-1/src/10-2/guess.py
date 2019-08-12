class Guess:

    def __init__(self, word):
        self.numOfWord = len(word)
        self.secretWord = word
        self.guessedChars = ""
        self.currentStatus = ""
        for i in range(self.numOfWord):
            self.guessedChars = self.guessedChars + "_"
        self.numTries = 0


    def display(self):
        print("Current: %s\n", self.guessedChars)
        print("Tries: %d\n", self.numTries)


    def guess(self, character):
        self.numTries = self.numTries + 1
        #self.guessedChars = self.guessedChars + character
        for i in range(self.numOfWord):
            if self.secretWord[i] == character:
                #self.guessedChars[i].replace("_",character)
                self.guessedChars = self.guessedChars[:i] + character + self.guessedChars[i:]
        #guessedChars = guessedChars.append(self.character)
        self.currentStatus = self.guessedChars
        if self.secretWord == self.currentStatus :
            return True
        else :
            return False
