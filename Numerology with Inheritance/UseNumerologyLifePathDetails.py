from NumerologyLifePathDetails import NumerologyExtended

def main():

    while True:
        sName = input("Enter Name: ")

        if not sName: continue

        sDOB = input("Enter birthday (mm-dd-yyyy): ")

        if len(sDOB) == 10 and ((sDOB[2] in "-/") and (sDOB[5] in "-/")):
            break

    #sName = "John Smith"
    #sDOB = "03/15/1962"

    myNumerologyObject = NumerologyExtended(sName, sDOB)
    print(myNumerologyObject)

main()
