def main()->None:
    sName = input("Enter Name: ")
    #Prompt the user for their First and Last name and store the input into a variable called sName

    sInitials = ""
    sInitials += sName[0] + sName[sName.find(" ")+1] #extract initials from sName

    sPassword = ""
    bIsValid = False
    while not bIsValid: #loop that will keep asking for a password until we reach a valid password
        bLength = bPass = bInitials = bUpper = bLower = bDigit = bSpecial = bCount = False
        dictCharacters = {}
        sPassword = input("Enter password: ") #Prompt the user for their desired password

        bLength = True if len(sPassword) in range(8, 13) else print("Password must be between 8 and 12 characters")
        #Ensure password length is between 8-12 characters

        bPass = True if not sPassword.lower().startswith("pass") else print("Password can't start with Pass")
        #Check to make sure the sPassword does not start with Pass or pass

        for char in sPassword:
            if char.isupper():     bUpper = True
            elif char.islower():   bLower = True
            elif char.isdigit():   bDigit = True
            elif char in "!@#$%^": bSpecial = True

            if char in dictCharacters: continue

            iCount = sPassword.lower().count(char.lower())

            if iCount > 1: dictCharacters[char.lower()] = iCount
            

        if not bUpper: print("Password must contain at least 1 uppercase letter.")
        #at least 1 uppercase letter A through Z
        if not bLower: print("Password must contain at least 1 lowercase letter.")
        #at least 1 lowercase letter a through z
        if not bDigit: print("Password must contain at least 1 number.")
        #at least 1 number between 0 - 9
        if not bSpecial: print("Password must contain at least 1 of these special characters: ! @ # $ % ^ ")
        #at least one of the allowed special characters

        bInitials = True if not sInitials.lower() in sPassword.lower() else print("Password must not contain user initials")
        #make sure sPassword does not contain the value of sInitials

        if not dictCharacters: bCount = True

        else:
            dictCharacters = dict(sorted(dictCharacters.items()))
            print(f"These characters occur more then once:")
            for key, value in dictCharacters.items(): print(f"{key}: {value} times")
            #No duplicate characters

        if bLength and bPass and bInitials and bUpper and bLower and bDigit and bSpecial and bCount: bIsValid = True
    print("\nPassword is valid and OK to use")
    print(f"Name: {sName}\nPassword: {sPassword}\n")

main()
