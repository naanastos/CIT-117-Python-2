class Numerology:
    def __init__(self, sName, sDOB):
        self.__name = sName
        self.__birthdate = sDOB

        #lifepath
        self.__lifePath = 0
        for letter in self.__birthdate.replace("-", "").replace("/", ""):
            self.__lifePath += int(letter)
        self.__lifePath = self.reduceNumber(self.__lifePath)

        #birthday number
        iBirthdayDay = int(self.__birthdate[3:5])
        self.__birthday = self.reduceNumber(iBirthdayDay)

        #attitude
        self.__iAttitude = 0
        for strNumber in self.__birthdate.replace("-", "").replace("/", "")[:4]:
            self.__iAttitude += int(strNumber)
        self.__iAttitude = self.reduceNumber(self.__iAttitude)

        self.__dictCharacters = {
            "A": 1, "J": 1, "S": 1,
            "B": 2, "K": 2, "T": 2,
            "C": 3, "L": 3, "U": 3,
            "D": 4, "M": 4, "V": 4,
            "E": 5, "N": 5, "W": 5,
            "F": 6, "O": 6, "X": 6,
            "G": 7, "P": 7, "Y": 7,
            "H": 8, "Q": 8, "Z": 8,
            "I": 9, "R": 9
        }

        self.__soul = 0
        self.__personality = 0

        for sLetter in self.Name.upper():
            if sLetter in "AEIOU":
                self.__soul += self.__dictCharacters.get(sLetter, 0)
            else:
                self.__personality += self.__dictCharacters.get(sLetter, 0)

        self.__soul = self.reduceNumber(self.__soul)
        self.__personality = self.reduceNumber(self.__personality)
        self.__power = self.reduceNumber(self.__soul + self.__personality)

    def reduceNumber(self, iNumber):
        strNumber = str(iNumber)
        while len(strNumber) > 1:
            iNumber = sum(int(digit) for digit in strNumber)
            strNumber = str(iNumber)
        return iNumber

    @property
    def Name(self):
        return self.__name

    @property
    def Birthdate(self):
        return self.__birthdate

    @property
    def LifePath(self):
        return self.__lifePath

    @property
    def Birthday(self):
        return self.__birthday

    @property
    def Attitude(self):
        return self.__iAttitude

    @property
    def Soul(self):
        return self.__soul

    @property
    def Personality(self):
        return self.__personality

    @property
    def Power(self):
        return self.__power

    def __str__(self):
        return f"""Name: {self.Name}
Birthdate: {self.Birthdate}
Life Path: {self.LifePath}
Birthday: {self.Birthday}
Attitude: {self.Attitude}
Soul: {self.Soul}
Personality: {self.Personality}
Power: {self.Power}"""

class NumerologyExtended(Numerology):
    def __init__(self, sName, sDOB):
        super().__init__(sName, sDOB)

        self.__lifePathDescriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoys nature, water, and alternative life paths",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or learns through hardship"
        }

    @property
    def LifePathDescription(self):
        return self.__lifePathDescriptions.get(self.LifePath)

    def __str__(self):
        return f"{super().__str__()}\nLife Path Description: {self.LifePathDescription}"
