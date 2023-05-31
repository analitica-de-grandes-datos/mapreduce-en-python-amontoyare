#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    data = []

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        line = line.strip()

        key, val = line.split("\t")
        val = int(val)
        #print(key,val)

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            data.append(val)
            # print(data)
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                data = set(sorted(data))
                sys.stdout.write("{}\t{}\n".format(curkey, ','.join(str(x) for x in data)))
                data = []

            curkey = key
            data.append(val)
    data = set(sorted(data))
    sys.stdout.write("{}\t{}\n".format(curkey, ','.join(str(x) for x in data)))