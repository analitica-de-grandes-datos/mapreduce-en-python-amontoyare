#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
# Esta es la funcion que mapea la entrada a parejas (clave, valor)
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:

        columns = line.split(',')
        
        sys.stdout.write("{}\t{}\n".format(columns[3], columns[4]))