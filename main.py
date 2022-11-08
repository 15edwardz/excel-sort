import csv
import sys

dupList = []
fullList = []

def readFile(sheet1, sheet2):
    try:
        with open(sheet1, "r", newline="") as f:
            reader = csv.reader(f)
            global sheet1Data
            sheet1Data = list(reader)
            print(sheet1Data)
    except:
        print("file not found")

    try:
        with open(sheet2, "r", newline="") as f:
            reader = csv.reader(f)
            global sheet2Data
            sheet2Data = list(reader)
            print(sheet2Data)
    except:
        print("file not found")


# def findMatching():
#     for element1 in sheet1Data[0]:
#         for element2 in sheet2Data[0]:
#             if element1 == element2:
#                dupList.append(element1)
#     print(dupList)

def findElements():
    for element1 in sheet1Data:
        for element2 in sheet2Data:
            if element1[0] == element2[0]:
                dupList.append(element2)
                sheet2Data.remove(element2)
    print(dupList)
    print(sheet2Data)
    for x in sheet1Data:
        fullList.append(x)
    for y in sheet2Data:
        fullList.append(y)
    print(fullList)



def executeProgram(sheet1, sheet2):
    readFile(sheet1, sheet2)
    findElements()
    with open('outputFull.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(fullList)
    with open('duplicates.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dupList)
# executeProgram("Sheet1.csv", "Sheet2.csv")
executeProgram(sys.argv[1], sys.argv[2])