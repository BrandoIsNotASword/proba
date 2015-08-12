# -*- coding: utf-8 -*-

import collections

class Data(object):
  def __init__(self, data):
    self.data = data
    self.tam = len(self.data)

    self.normalize_data()
    self.histogram()

  def print_data(self):
    print self.data

  def normalize_data(self):
      self.data = sorted([float(d) for d in self.data])

  def histogram(self):
    self.hist = collections.OrderedDict()

    for i in self.data:
      if i not in self.hist.keys():
        self.hist[i] = 1
      else:
        self.hist[i] += 1