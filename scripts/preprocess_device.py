import os
import sys
import numpy as np
import scipy.stats as stats

def flatten_data(data_):
    switch, dest, temp, max = False, [], [], 0
    for line in data_:
        if line[0] > 0:
            temp.append(line[0])
            switch = True
        elif switch:
            if len(temp) > 3:
                dest.append(np.array(temp))
                max = (len(temp)) if len(temp) > max else max
            temp, switch = [], False
    if len(temp) > 0:
        dest.append(np.array(temp))
        max = (len(temp)) if len(temp) > max else max
    # print(len(dest))
    return dest, max

def get_statictics(data_):
    return [[np_array.mean()] + [np.median(np_array)] + [np_array.std()] + [np_array.var()] + [stats.skew(np_array)] + [
        stats.kurtosis(np_array)] + [stats.hmean(np_array)]
            for np_array in data_]

def normalize(data_):
    for i in range(len(data_[0])):
        temp = data_[:, i]
        print(len(temp))
        variance = temp.var()
        if variance != 0:
            data_[:, i] = (temp - temp.mean()) / variance
    return data

def print_data(data_, appareil_, output_):
    for line in data_:
        output_.write("%f,%f,%f,%f,%f,%f,%f,%s\n" % ( line[0], line[1], line[2], line[3], line[4], line[5], line[6], appareil_))



# Le nom du dossier (tracebase) de l'apppareil
appareil = sys.argv[1]
# le seuil de valeures de puissance1 à partir duquel on garde les valeures
seuil = int(sys.argv[2])
# le dossier tracebase à utiliser
path = './tracebase/incomplete/' + appareil
# Le fichier de destination
output = open('./preprocessed/new/' + appareil + '_stats.csv', "w")

# Ecrire cette ligne  en début du fichier de sortie
output.write("moyenne,mediane,ecartType,variance,symetrie,kurtosis,harmonique,appareil\n")
# Parcourir tout les fichiers d'un dossier liés à un appareil précis
for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current):
        # Ici j'ouvre un fichier du dossier à lire
        data = open(current).readlines()
        # Ici je divise en deux blocs (en fonction de l'espace) chaque lines et je garde uniquement le second bloc
        # Exemple: "10/12/2011 01:00:01;120;118"   => ["10/12/2011", "01:00:01;120;118"] => ["01:00:01;120;118", ...]
        data = [line.split(" ")[1] for line in data]
        # Là je divise en fonction des points virgules et je converti les deux derniers blocs en entiers
        # Exemple: ["01:00:01;120;118", ...] => [["01:00:01", 120, 118], [..], ...]
        data = [[int(line.split(";")[1])] + [int(line.split(";")[2])] for line in data]
        # regroupement des donnees par signal recu)
        data, max = flatten_data(data)
        # extarction des statictiques
        data = np.array(get_statictics(data))
        # print(data[0])
        # Affichage
        print_data(data, appareil, output)
output.close()