import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
     
    def addMoney(self,amt):
        self.prizeMoney += amt
        
    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
    
    
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    
    def getMove(self, category, obscuredPhrase, guessed):
        st = input("""
        {} has ${}
        
        Category: {}
        Phrase:  {}
        Guessed: {}
        
        Guess a letter, phrase, or type 'exit' or 'pass':
            """.format(self.name, self.prizeMoney, category, obscuredPhrase, guessed))
        return st
        

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty
        
    def smartCoinFlip(self):
        if self.difficulty < random.randint(1, 10):
            return True
        return False
    
    def getPossibleLetters(self, guessed):
        lst = []
        LET_S = ""
        if self.prizeMoney >= VOWEL_COST:
            LET_S = LETTERS + VOWELS
        else:
            LET_S = LETTERS
        for c in LET_S:
            if c not in guessed:
                lst.append(c)
        return lst
        
    def getMove(self, category, obscuredPhrase, guessed):
        lst = self.getPossibleLetters(guessed)
        if len(lst) == 0:
            return 'pass'
        else:
            bool1 = self.smartCoinFlip()
            if bool1 == True:
                i = -1
                for _ in range(len(self.SORTED_FREQUENCIES)):
                    if self.SORTED_FREQUENCIES[i] in lst:
                        if self.SORTED_FREQUENCIES[i] in VOWELS:
                            self.prizeMoney -= VOWEL_COST
                        return self.SORTED_FREQUENCIES[i]
                    i=i-1
            else:
                while():
                    char = random.choice(LETTERS)
                    if char in lst:
                        if char in VOWELS:
                            self.prizeMoney -= VOWEL_COST
                        return char
                
    
    
