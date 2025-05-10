
import csv

with open("RealEstateData.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    lstData = [row for row in reader]

#With open so it doesn't need to be closed

lstCity = []
lstPropertyTypes = []
lstPrices = []


dictPropertyType, dictCity, dictZip = {}, {}, {}


for row in lstData:
    #print(row)

    sCity = row[1]
    sPropertyType = row[7]
    fPrice = float( row[8]  )

    sZip = row[2]
    
    if sCity not in lstCity:
        lstCity.append(sCity)

    if sPropertyType not in lstPropertyTypes:
        lstPropertyTypes.append(sPropertyType)


    if sPropertyType in dictPropertyType:
        dictPropertyType[sPropertyType] += fPrice
    else:
        dictPropertyType[sPropertyType] = fPrice

    if sCity in dictCity:
        dictCity[sCity] += fPrice
    else:
        dictCity[sCity] = fPrice
            

    if sZip in dictZip:
        dictZip[sZip] += fPrice
    else:
        dictZip[sZip] = fPrice



    lstPrices.append(fPrice)



print("Summary for Property Types:")
for propertyType, fTotal in dictPropertyType.items():
    print(f"{propertyType:20s}{fTotal:15,.2f}")

print("Summary for Cities Types:")
for sCity, fTotal in dictCity.items():
    print(f"{sCity:20s}{fTotal:15,.2f}")

print("Summary for Zips Types:")
for sZip, fTotal in dictZip.items(): # {"01118": 60000}
    print(f"{sZip:20s}{fTotal:15,.2f}")


def getMedian(lstList1):

    lstList1.sort()
    iListLength = len(lstList1)

    if iListLength % 2 == 0:
        print(f"The list length is even: {iListLength}")
        fMedianRight = lstList1[iListLength // 2]
        fMedianLeft = lstList1[(iListLength // 2) - 1]
        fMedian = (fMedianLeft + fMedianRight) / 2
        #print(f"The Medians are {fMedianLeft, fMedianRight}")
        #print(f"The Median is: {fMedian}")

    else: # if iListLength % 2 != 0:
        
        #print(f"The list length is odd: {iListLength}")
        fMedian = lstList1[iListLength // 2] # 1
        #print(f"The Median is: {fMedian}")

    return fMedian


print(f"{'The min is: ':20s}{min(lstPrices):15,.2f}")
print(f"{'The max is: ':20s}{max(lstPrices):15,.2f}")
print(f"{'The sum is: ':20s}{sum(lstPrices):15,.2f}")
print(f"{'The average is ':20s}{sum(lstPrices)/len(lstPrices):15,.2f}")
#print(f"{'The Median is ':20s}{fMedian:15,.2f}")
print(f"{'The Median is ':20s}{getMedian(lstPrices):15,.2f}")
