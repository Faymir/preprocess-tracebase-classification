import os
import sys
import numpy as np


# import scipy.stats as stats

def normalize(data_):
    for i in range(6):
        temp = data_[:, i]
        # print(len(temp))
        variance = temp.var()
        if variance != 0:
            data_[:, i] = (temp - temp.mean()) / variance
    return data_


size_per_device = int(sys.argv[1])
path = './preprocessed/new'
output = open('./training/training.csv', "w")
r = []
labels = []
output.write("moyenne,mediane,ecartType,variance,symetrie,kurtosis,harmonique,appareil\n")
for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current) and current != "./preprocessed/new/README.md":
        print(current)
        data = open(current).readlines()
        a = size_per_device
        for line in data:
            if a <= 0:
                break
            if line != "moyenne,mediane,ecartType,variance,symetrie,kurtosis,harmonique,appareil\n":
                # output.write(line)
                part = line.split(',')
                r.append([float(part[0]),
                          float(part[1]),
                          float(part[2]),
                          float(part[3]),
                          float(part[4]),
                          float(part[5]),
                          float(part[6])
                          ])
                labels.append(line.split(',')[-1])
            else:
                a += 1
            a = a - 1
r = np.array(r)
r = normalize(r)
for i in range(len(r)):
    # output.write(join([str(value) for value in r[i]], sep=','))
    # output.write("%s" % labels[i])
    output.write("%f,%f,%f,%f,%f,%f,%f,%s" % (r[i, 0], r[i, 1], r[i, 2], r[i, 3], r[i, 4], r[i, 5], r[i, 6], labels[i]))
output.close()
