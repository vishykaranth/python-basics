import pandas as pd

import numpy as np

ser = {
    'index': [0, 1, 2, 3],
    'data': [145, 142, 38, 13],
    'name': 'songs'
}


def get(ser, idx):
    value_idx = ser['index'].index(idx)
    return ser['data'][value_idx]


print get(ser, 1)
print get(ser, 3)

songs = {
    'index': ['Paul', 'John', 'George', 'Ringo'],
    'data': [145, 142, 38, 13],
    'name': 'counts'
}

print get(songs, 'John')

songs2 = pd.Series([145, 142, 38, 13],
                   name='counts');

print songs2

songs3 = pd.Series([145, 142, 38, 13],
                   name='counts',
                   index=['Paul', 'John', 'George', 'Ringo'])

print songs3

print songs3.index


class Foo:
    pass


ringo = pd.Series(
    ['Richard', 'Starkey', 13, Foo()],
    name='ringo')

print ringo

nan_ser = pd.Series([2, None],
                    index=['Ono', 'Clapton'])

print nan_ser

print nan_ser.count()

numpy_ser = np.array([145, 142, 38, 13])
print songs3[1]

print numpy_ser[1]

print songs3.mean()

print numpy_ser.mean()

mask = songs3 > songs3.median() # boolean array
