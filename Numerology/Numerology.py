
#class file

# sName = input("ENter Name:")
# sBirthday = input("ENter birthdate:")

# Numerology(sName, sBirthday)
#Numerology.NUmerology

class Numerology:
    def __init__(self, sName, sDOB):

        self.name = sName
        self.birthdate = sDOB

        self.lifePath = 0
        for letter in self.birthdate.replace("-", "").replace("/", ""): #"03/10/1995"
            #print(letter)
            self.lifePath += int(letter)
        self.lifePath = self.reduceNumber(self.lifePath)
        #print(f"Life Path: {self.lifePath}")

        self.birthday = 0
        iBirthdayDay = int(self.birthdate[3:5])
        #print(iBirthdayDay)
        self.birthday = self.reduceNumber(iBirthdayDay)
        #print(f"Birthday: {self.birthday}")

        self.iAttitude = 0
        for strNumber in self.birthdate.replace("-", "").replace("/", "")[:4]:
            #print(strNumber)
            self.iAttitude += int(strNumber)
        #print(self.iAttitude)
        self.iAttitude = self.reduceNumber(self.iAttitude)
        #print(f"Attitude: {self.iAttitude}")

        #----------------------------------------------------

        """
        A, J, S 1 
        B, K, T 2 
        C, L, U 3 
        D, M, V 4 
        E, N, W 5 
        F, O, X 6 
        G, P, Y 7 
        H, Q, Z 8 
        I, R 9 
        """

        # self.dictCharacters =   {("A", "J", "S"):1,
        #                          ("B", "K", "T"):2,
        #                          ("C", "L", "U"):3,
        #                          ("D", "M", "V"):4,
        #                          ("E", "N", "W"):5,
        #                          ("F", "O", "X"):6,
        #                          ("G", "P", "Y"):7,
        #                          ("H", "Q", "Z"):8,
        #                          ("I", "R")     :9}


        self.dictCharacters = { "A":1, "J":1, "S": 1,
                                "B":2, "K":2, "T": 2, 
                                "C":3, "L":3, "U": 3, 
                                "D":4, "M":4, "V": 4, 
                                "E":5, "N":5, "W": 5, 
                                "F":6, "O":6, "X": 6, 
                                "G":7, "P":7, "Y": 7, 
                                "H":8, "Q":8, "Z": 8, 
                                "I":9, "R":9}
        
    
        self.soul = 0
        self.personality = 0

        for sLetter in self.name.upper(): # Mikey

            #print(sLetter)

            #print(self.dictCharacters.get(sLetter, 0))

            if sLetter in "AEIOU":

                #print(sLetter)
                self.soul += self.dictCharacters.get(sLetter, 0)

            else:
                #print(sLetter)
                self.personality += self.dictCharacters.get(sLetter, 0)


        #print(self.soul)
        self.soul = self.reduceNumber(self.soul)
        #print(self.soul)

        #print(self.personality)
        self.personality = self.reduceNumber(self.personality)
        #print(self.personality)


        self.power = 0
        #8 (Soul) + 5 (Personality)
        self.power = self.reduceNumber(self.soul + self.personality)
        #print(self.power)



        """
        Soul Number: Is computed by taking all the vowels (A,E,I,O,U) in the inputted birth name adding them together.   
        The Soul Number is supposed to denote what a person feels on the inside. 
        For example: 
        I A A I O are the vowels in Brian Candido would be computed as: 9+1+1+9+6 = 26 
        26 would then be reduced again by 2+6 = 8 and 8 would be the Soul Numbe
        """


    def reduceNumber(self, iNumber):
        strNumber = str(iNumber)
        while len(strNumber) > 1:
            iNumber = int(strNumber[0]) + int(strNumber[1])
            strNumber = str(iNumber)
        #print(iNumber)
        return iNumber

    def getName(self):
        return self.name
    
    def getBirthdate(self): #03-10-1995
        return self.birthdate
    

    def getLifePath(self):
        return self.lifePath
    
    def getBirthday(self): # 6
        return self.birthday
    
    def getAttitude(self):
        return self.iAttitude
    
    def getSoul(self):
        return self.soul
    
    def getPersonality(self):
        return self.personality
    
    def getPower(self):
        return self.power

    def __str__(self):
        return f"""Name: {self.getName()}
        Birthdate: {self.getBirthdate()}
        Life Path: {self.getLifePath()}
        Birthday: {self.getBirthday()}
        Attitude: {self.getAttitude()}
        Soul: {self.getSoul()}
        Personality: {self.getPersonality()}
        Power: {self.getPower()}"""
