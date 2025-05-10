import pickle

def validateInput(sPrompt):
   fNumber = 0
   while fNumber <= 0 :
      try:   
         fNumber = float(input(sPrompt)) 
      except ValueError:
         print("Input must a numeric value")
   return fNumber


def main():

    dictPlanetWeightFactors = { #2

            "Earth"   :1.0,
            "Mercury" :0.38,
            "Venus"   :0.91, 
            "Moon"    :0.165, 
            "Mars"    :0.38, 
            "Jupiter" :2.34, 
            "Saturn"  :0.93, 
            "Uranus"  :0.92, 
            "Neptune" :1.12, 
            "Pluto"   :0.066
        }


    dictPlanetHistory = {}
    # 1. Load stored dictionary key/values:
    eof = False
    try:

        with open("mwPlanetaryWeights.db", "rb") as file:

            #1.2 if execution reaches here load each dictory key/value in: 
            while not eof:
                try:
                    dictPlanetHistory = pickle.load(file)
                    if input("Would you like to see the history? y/n: ").lower() == "y": #4
                        dictPlanetHistory:dict
                        for name, dictWeights in dictPlanetHistory.items():
                            print(f"{name}, here are your weights on Solar System's planets")
                            #print(key, value)
                            dictWeights:dict
                            for planet, weight in dictWeights.items():print(f"Weight on {planet:10s} {weight:10,.2f}") #7
                    
                except EOFError: eof = True
            #input_file.close()

    except FileNotFoundError: pass
        #1.3 The file may not exist on first run.  If so just skip the loading of the dictionary:
            #pass


    while True: #5
        sName = input("Enter a name: ").title()
        if not sName: break
        if sName in dictPlanetHistory: 
            print(f"{sName} is already in the history file. Enter a unique name.")
            continue
        fWeight = validateInput("Enter Weight: ") #the bug was fixed by taking out the input passed into the prompt
        dictPersonWeights = {}
        print(f"{sName}, here are your weights on our Solar System's planets")
        for planet, factor in dictPlanetWeightFactors.items():
            fCalculatedWeight = fWeight * factor
            dictPersonWeights[planet] = fCalculatedWeight
            print(f"{planet:10s}{fCalculatedWeight:10,.2f}")
        dictPlanetHistory[sName] = dictPersonWeights
    with open("mwPlanetaryWeights.db", "wb") as file: pickle.dump(dictPlanetHistory, file) #6


main()
