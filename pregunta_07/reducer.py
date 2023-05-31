#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    data = []
    
    for line in sys.stdin:
        line = line.strip()
        columns = line.split("\t")
        data.append((columns[0], columns[2], int(columns[1])))

    sorted_data = sorted(data, key=lambda x: (x[0], x[2]))

    for item in sorted_data:
        sys.stdout.write("{}\t{}\t{}\n".format(item[0], item[1], item[2]))