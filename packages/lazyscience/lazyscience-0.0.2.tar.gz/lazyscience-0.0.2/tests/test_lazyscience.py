#%%
#import pytest
import lazyscience as lz
import numpy as np
import os

def test_save():
    a = 3
    b = np.array([3, 5])
    c = 7
    lz.save('a')
    lz.save(['b', 'c'], mode='a', filename='a.h5')
    out = lz.load('a.h5')
    assert(out['a'] == 3)
    assert((out['b'] == [3, 5]).all())
    assert(out['c'] == 7)
    
    # delete a.h5
    os.remove('a.h5')
    
    

def test_significance():
    pass