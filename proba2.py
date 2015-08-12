# -*- coding: utf-8 -*-

import math
import collections
from data import Data

class DatosAgrupados(Data):
    def __init__(self, data):
        super(DatosAgrupados, self).__init__(data)

        self.rango = self.data[self.tam-1] - self.data[0]
        # self.k = round(1 + math.log(self.tam,  2))

        # # verificar si lo correcto es redondear
        # self.a = round(self.rango / float(self.k))

        self.k, self.a = 4, 4

        self.tabla = (
            ('min', []),
            ('max', []),
            ('ni', []),
            ('Ni', []),
            ('fi', []),
            ('Fi', []),
            ('mi', [])
        )

        self.tabla = collections.OrderedDict(self.tabla)

        self.min_max()
        self.ni()
        self.Ni()
        self.fi()
        self.Fi()
        self.mi()

        self.media()
        self.mediana()
        self.moda()

    def min_max(self):
        max_val = max(self.hist.keys())
        min_val = self.hist.keys()[0]

        while min_val < max_val:
            self.tabla['min'].append(min_val)
            self.tabla['max'].append(min_val + self.k-1)

            min_val += self.k

    def ni(self):
        for min_val, max_val in zip(self.tabla['min'], self.tabla['max']):
            self.tabla['ni'].append(self.__get_num_repeated(min_val, max_val))

    def Ni(self):
        count = 0

        for i in self.tabla['ni']:
            count += i
            self.tabla['Ni'].append(count)

    def fi(self):
        for i in self.tabla['ni']:
            self.tabla['fi'].append('%d/%d' % (i, self.tam))

    def Fi(self):
        for i in self.tabla['Ni']:
            self.tabla['Fi'].append('%d/%d' % (i, self.tam))

    def mi(self):
        for min_val, max_val in zip(self.tabla['min'], self.tabla['max']):
            total, tam = 0, 0

            for key, value in self.hist.iteritems():
                if key >= min_val and key <= max_val:
                    total += key * value 
                    tam += value

            self.tabla['mi'].append('%d/%d' % (total, tam))

    def print_tabla(self):
        for key in self.tabla.keys():
            print str(key).ljust(10, ' '),

        print

        for i in range(len(self.tabla['min'])):
            for value in self.tabla.values():
                print str(value[i]).ljust(10, ' '),

            print

    def print_info(self):
        print "Media:", self.media()
        print "Mediana:", self.mediana()
        print "Moda:", self.moda()
        print "Varianza:", self.varianza()
        print "Desviación estándar:", self.desviacion_estandar()

    def media(self):
        sumatory = 0

        for mi, ni in zip(self.tabla['mi'], self.tabla['ni']):
            sumatory += self.__resolve_fraction(mi) * ni

        return sumatory / float(self.tam)

    def mediana(self):
        max_val = self.__get_max()
        linf = self.tabla['min'][max_val]
        ni = self.tabla['ni'][max_val]
        Ni = self.tabla['Ni'][max_val-1]
        a = self.k - 1
        N = self.tam

        return linf + ((N/2.0-Ni)/float(ni)) * a

    def moda(self):
        max_val = self.__get_max()
        linf = self.tabla['min'][max_val]
        ni_a = self.tabla['ni'][max_val-1]
        ni = self.tabla['ni'][max_val]
        ni_d = self.tabla['ni'][max_val+1]
        a = self.k - 1

        return linf + (ni-ni_a)/((ni-ni_a)*(ni-ni_d)) * a

    def varianza(self):
        media = self.media()
        num = 0

        for val, frec in self.hist.iteritems():
            num += (val**2) * frec

        return (num/float(self.tam)) - (media**2)

    def desviacion_estandar(self):
        return math.sqrt(self.varianza())

    def __get_repeated_indexes(self, val):
        pass

    def __get_max(self):
        max_val = max(self.tabla['ni'])
        max_index = self.tabla['ni'].index(max_val)

        return max_index

    def __get_num_repeated(self, min_val, max_val):
        count = 0

        for key, value in self.hist.iteritems():
            if key >= min_val and key <= max_val:
                count += value

        return count

    def __resolve_fraction(self, str):
        str_splt = str.split('/')
        num, den = str_splt[0], str_splt[1]

        return float(num) / float(den)

if __name__ == '__main__':
    data = DatosAgrupados([170, 171, 166, 176, 176, 166, 160, 168, 163, 174, 166, 168, 178, 175, 176, 167, 172, 173, 173, 172, 168, 169, 166, 162, 181, 172, 169, 169, 165])

    # data.print_data()

    # data = DatosAgrupados([36, 30, 47, 60, 32, 35, 40, 50, 54, 35, 45, 52, 48, 58, 60, 38,32, 35, 56, 48, 30, 55, 49, 39, 58, 50, 65, 35, 56, 47, 37, 56,58, 50, 47, 58, 55, 39, 58, 45])

    data.print_tabla()
    data.print_info()