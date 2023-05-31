#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:

        columns = line.strip().split('\t')

        aux = columns[1].split(",")

        for item in aux:
        
            sys.stdout.write("{}\t{}\n".format(item,columns[0]))