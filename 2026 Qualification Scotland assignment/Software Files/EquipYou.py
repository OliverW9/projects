def ReadData():                         #step 1 - Reading files into parrallel arrays
        tool =  []
        manufacturer = []
        dateRented = []
        returned = []
        fee = []
    
        f = open("tools.csv", "r")
    
        line = f.readline()
    
        while line:
            current = line.split(",")
            tool.append(current[0])
            manufacturer.append(current[1])
            dateRented.append(current[2])
            returned.append(current[3])
            fee.append(int(current[4]))
    
            line = f.readline()
    
        return tool, manufacturer, dateRented, returned, fee

def findNameAndNum(tool, manufacturer): #step 2 - Finding and displaying the name of each tool and the total number of tools by a chosen manufacturer

    total = 0

    chosenManufacturer = input("Enter a manufacturer: ")

    for i in range(len(tool)):
        if manufacturer[i] == chosenManufacturer:
            print(f"{tool[i]}")
            total += 1
    
    print(f"total: {total}")

def calcLateFee(dateRented, returned, fee): #step 3 - Calculate late fee for tools rented in 2025 and not retuned
    
    for i in range(len(fee)):
        if dateRented[i][6:10] == "2025" and returned[i] == "No":
            if int(dateRented[i][3:5]) <= 6:
                fee[i] = 10
            else:
                fee[i] = 5

    return fee

def WriteFile(tool, dateRented, fee): #step 4 - write the tool name, date rented, and fee of any tool with a late fee to an external file
        
    with open("lateTools.csv", "w") as f:

        for i in range(len(tool)):
            if int(fee[i]) != 0:
                f.write(tool[i])
                f.write(",")
                f.write(dateRented[i])
                f.write(",")
                f.write(str(fee[i]))
                f.write("\n")
    f.close()

tool, manufacturer, dateRented, returned, fee = ReadData()    
findNameAndNum(tool, manufacturer)
CalculatedFees = calcLateFee(dateRented, returned, fee)
WriteFile(tool, dateRented, fee)

# - 150698154 -