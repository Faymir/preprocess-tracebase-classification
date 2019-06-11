import os

blockSize = 20000
path = './preprocessed'
output = open('./testData.csv', "w")
output.write("Timestamp,Puissance1s,Puissance2s,Appareil\n")
for file in os.listdir(path):
    current = os.path.join(path, file)
    print(current)
    if os.path.isfile(current):
        data = open(current).readlines()
    end = blockSize * 2
    start = blockSize
    i = 0
    for line in data:
        if i >= end:
            break
        if (current == "./preprocessed/Washingmachine.csv") and (line != "Timestamp,Puissance1s,Puissance2s,Appareil\n"):
            parts = line.split(",")
            output.write("%s,%s,%s,'%s'\n" % (parts[0], parts[1], parts[2], parts[3].strip()))
        elif (line != "Timestamp,Puissance1s,Puissance2s,Appareil\n") and i >= start:
            parts = line.split(",")
            output.write("%s,%s,%s,'%s'\n" % (parts[0], parts[1], parts[2], parts[3].strip()))
            # output.write(line)
        i += 1
output.close()
