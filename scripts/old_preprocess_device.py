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
                dest.append(temp)
                max = (len(temp)) if len(temp) > max else max
            temp, switch = [], False
    if len(temp) > 0:
        temp[1] = data_[-1][0]
        temp.append(appareil)
        dest.append(temp)
        max = (len(temp)) if len(temp) > max else max
    # print(len(dest))
    return dest, max


def print_data(data, output):
    for line in data:
        output.write("%s,%s,%s\n" % (line[0], line[1], line[-1]))


# Le nom du dossier (tracebase) de l'apppareil
appareil = sys.argv[1]
# le seuil de valeures de puissance1 à partir duquel on garde les valeures
seuil = int(sys.argv[2])
# le dossier tracebase à utiliser
path = './tracebase/incomplete/' + appareil
# Le fichier de destination
output = open('./preprocessed/' + appareil + '.csv', "w")

# Ecrire cette ligne  en début du fichier de sortie
output.write("Debut,Fin,Appareil\n")
# Parcourir tout les fichiers d'un dossier liés à un appareil précis
for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current):
        # Ici j'ouvre un fichier du dossier à lire
        data = open(current).readlines()
        # Ici je divise en deux blocs (en fonction de l'espace) chaque lines et je garde uniquement le second bloc
        # Exemple: "10/12/2011 01:00:01;120;118"   => ["10/12/2011", "01:00:01;120;118"] => ["01:00:01;120;118", ...]
        # data = [(line.split("  ")[0] + "-" + line.split(" ")[1]) for line in data]
        # Là je divise en fonction des points virgules et je converti les deux derniers blocs en entiers
        # Exemple: ["01:00:01;120;118", ...] => [["01:00:01", 120, 118], [..], ...]
        data = [[line.split(";")[0]] + [int(line.split(";")[1])] + [int(line.split(";")[2])] for line in data if
                int(line.split(";")[1]) >= seuil]
        # Au niveau de la ligne ci dessous je converti l'heure en timestamp
        # [["01:00:01", 120, 118], [..], ...] => [[3600*1+60*0+1, 120, 118], [..], ...] => [[3601, 120, 118], [..], ...]
        # data = [[int(line[0].split(":")[0]) * 3600 + int(line[0].split(":")[1]) * 60 + int(line[0].split(":")[2])] + [
        #     line[1]] + [line[2]] for line in data]
        # Là j'ordonne les données en fonction de leurs puissances mais c'est facultatif
        # data = sorted(data, reverse=True)
        dest, max = flatten_data(data)
        # Ici je les écrits dans un nouveau fichier sous le format => timestamp,puissance1,puissance2,appareil
        print_data(dest, output)
output.close()
