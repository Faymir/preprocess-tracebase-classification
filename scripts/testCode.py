import os
import sys
import numpy as np
import scipy.stats as stats

appareil = 'Refrigerator'
data = open('./tracebase/incomplete/MicrowaveOven/dev_4BEA01_2011.12.11_cleaned_11.12.2011.csv').readlines()
# data = open('./tracebase/incomplete/Refrigerator/dev_D3230E_2011.12.03.csv').readlines()
# data = open('./tracebase/incomplete/Washingmachine/dev_B8198B_2011.12.11_cleaned_11.12.2011.csv').readlines()
data = [line.split(" ")[1] for line in data]
data = [[line.split(";")[0]] + [int(line.split(";")[1])] + [int(line.split(";")[2])]
        for line in data]
data = [
    [int(line[0].split(":")[0]) * 3600 + int(line[0].split(":")[1]) * 60 + int(line[0].split(":")[2])] + [line[1]] + [
        line[2]] for line in data]


def flatten_data(data):
    print(len(data))
    switch, dest, temp, max = False, [], [], 0
    for line in data:
        if line[1] > 0:
            # if not switch:
            #     temp.append(line[0])
            #     temp.append('#')
            temp.append(line[1])
            switch = True
        elif switch:
            # temp[1] = line[0]
            # temp.append(appareil)
            dest.append(temp)
            max = (len(temp)) if len(temp) > max else max
            temp, switch = [], False
    if len(temp) > 0:
        dest.append(np.array(temp))
        max = (len(temp)) if len(temp) > max else max
    print(len(dest))
    return dest, max


def get_statictics(data_):
    print(type(data[0]))
    return [[np_array.mean()] + [np.median(np_array)] + [np_array.std()] + [np_array.var()] + [stats.skew(np_array)] + [
        stats.kurtosis(np_array)] + [stats.hmean(np_array)]
            for np_array in data_]


dest, max = flatten_data(data)
dest = [np.array(line) for line in dest if len(line) > 4]
result = np.array(get_statictics(dest))
print(result)
for i in range(6):
    temp = result[:, i]
    if len(temp) > 1:
        result[:, i] = (temp - temp.mean()) / temp.var()

output = open("./output/res_stats1.csv", "w")
output.write("moyenne,mediane,ecartType,variance,symetrie,kurtosis,harmonique,appareil\n")
for line in result:
    output.write("%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%s\n" % (
        line[0], line[1], line[2], line[3], line[4], line[5], line[6], appareil))
output.close()
print(max)

# moyenne => numpy.mean
# mediane => numpy.median
# ecartType => numy.std()
# variance => numy.var()
# asymetrie => scipy.stats.skew
# coeff d'applatissement de pearson => scipy.statskurtosis
# moyenne harmonique => scipy.stats.hmean
# arr = np.array(result)
# print("moyenne %.2f" % arr.mean())
# print("mediane %.2f" % np.median(arr))
# print("ecartType %.2f" % arr.std())
# print("variance %.2f" % arr.var())
# print("asymetrie %.2f" % stats.skew(arr))
# print("coeff d'applatissement de pearson %.2f" % stats.kurtosis(arr))
# print("moyenne harmonique %.2f" % stats.hmean(arr))
