from Numerology import Numerology


"""
Test Name: John Smith  
Test DOB: 03/15/1962 
Life Path Number:  9 
Birth Day Number:  6 
Attitude Day Number:  9 
Soul Number:   6 
Personality Number:  2 
Power Name Number:  8
"""

def main():

    while True:
        sName = input("Enter Name: ") # mm-dd-yyyy

        if not sName: continue

        sDOB = input("Enter birthday (mm-dd-yyyy: ")

        if sDOB[2] == "-" or sDOB[2] == "/" and sDOB[5] == "-" or sDOB[5] == "/" and len(sDOB) == 10: 
            break

    #sName = "John Smith"
    #sDOB = "03/15/1962"

    myNumerologyObject = Numerology(sName, sDOB)
    print(myNumerologyObject)

main()
