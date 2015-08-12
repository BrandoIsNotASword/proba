# -*- coding: utf-8 -*-

import math
from data import Data

class DatosNoAgrupados(Data):
    def __init__(self, data):
        super(DatosNoAgrupados, self).__init__(data)

    def print_info(self):
        print "Media:", self.media()
        print "Mediana:", self.mediana()
        print "Moda:", self.moda()
        print "Varianza:", self.varianza()
        print "Desviación estándar:", self.desviacion_estandar()

    def media(self):
        return sum(self.data) / float(self.tam)

    def mediana(self):
        if (self.tam % 2) == 0:
            mid = self.tam / 2

            return (self.data[mid-1]+self.data[mid]) / 2.0
        else:
            return self.data[self.tam / 2]

    def moda(self):
        piv, moda = None, []

        for i in self.data:
            count = 0

            for j in self.data:
                if i == j: count += 1

            if piv < count: 
                piv = count
                del moda[:]
                moda.append(i)
            elif piv == count and i not in moda:
                piv = count
                moda.append(i)

        return moda[0] if len(moda) == 1 else moda

    def varianza(self):
        media = self.media()
        tam = self.tam
        var = 0

        for d in self.data:
            var += (d-media) ** 2

        return 1/float(tam) * var

    def desviacion_estandar(self):
        return math.sqrt(self.varianza())


if __name__ == '__main__':
    data = DatosNoAgrupados([170, 171, 166, 176, 176, 166, 160, 168, 163, 174, 166, 168, 178, 175, 176, 167, 172, 173, 173, 172, 168, 169, 166, 162, 181, 172, 169, 169, 165])

    data.print_info()