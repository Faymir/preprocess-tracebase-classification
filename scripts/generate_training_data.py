import os
import sys

size_per_device = int(sys.argv[1])
path = './preprocessed/new'
output = open('./training/test_stats1.csv', "w")
output.write("moyenne,mediane,ecartType,variance,symetrie,kurtosis,harmonique,appareil\n")
for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current) and current!="./preprocessed/new/README.md":
        print(current)
        data = open(current).readlines()
        a = size_per_device
        for line in data:
            if a <= 0:
                break
            if line != "moyenne,mediane,ecartType,variance,symetrie,kurtosis,harmonique,appareil\n":
                output.write(line)
            else:
                a += 1
            a = a - 1
output.close()