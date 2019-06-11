import os

classes = open('./testData.csv').readlines()
classes = [line.strip().split(",")[3] for line in classes][1:]
# classes = classes[1:]
predicted = open('./result.csv').readlines()
predicted = [line.strip() for line in predicted]
differences = set(classes).symmetric_difference(set(predicted))
cmp = 0
for a, b in zip(classes, predicted):
    if a != b:
        cmp += 1

# print(len(classes))
# print(len(predicted))

print("%.2f%%" % (cmp/len(classes) * 100.0))