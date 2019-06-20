# Pour l'utiliser pour par exemple extraire les données du freezer  il faut taper cette commande dans un terminal:
# python extractFromFolder.py Printer 0
import os
import sys


def flatten_data(data_):
    switch, dest, temp, max = False, [], [], 0
    for line in data_:
        if line[1] > 0:
            if not switch:
                temp.append(line[0])
                temp.append('#')
            temp.append(line[1])
            switch = True
        elif switch:
            if len(temp) > 4:
                temp[1] = line[0]
                temp.append(appareil)
                dest.append(temp[0:2])
                max = (len(temp)) if len(temp) > max else max
            temp, switch = [], False
    if len(temp) > 0:
        temp[1] = data_[-1][0]
        temp.append(appareil)
        dest.append(temp[0:2])
        max = (len(temp)) if len(temp) > max else max
    # print(len(dest))
    return dest, max


def print_data(data):
    for line in data:
        print("%s => %s" % (line[0], line[1]))


# Le nom du dossier (tracebase) de l'apppareil
appareil = sys.argv[1]
# le seuil de valeures de puissance1 à partir duquel on garde les valeures
seuil = 0#int(sys.argv[2])
# le dossier tracebase à utiliser
path = './tracebase/incomplete/' + appareil
# Le fichier de destination
# output = open('./preprocessed/' + appareil + '.csv', "w")

# Ecrire cette ligne  en début du fichier de sortie
print(f"\n....{appareil}....\n")
print("Debut => Fin")
# Parcourir tout les fichiers d'un dossier liés à un appareil précis
for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current):
        # Ici j'ouvre un fichier du dossier à lire
        data = open(current).readlines()
        #  Exemple: "10/12/2011 01:00:01;120;118"  => [["10/12/2011 01:00:01", 120, 118], [..], ...]
        data = [[line.split(";")[0]] + [int(line.split(";")[1])] + [int(line.split(";")[2])] for line in data if
                int(line.split(";")[1]) >= seuil]
        dest, max = flatten_data(data)
        # Ici je les écrits dans un nouveau fichier sous le format => timestamp,puissance1,puissance2,appareil
        print_data(dest)

print(f"\n....{appareil}....\n")