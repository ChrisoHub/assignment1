# -*- coding: utf-8 -*-
"""
Created on Mon Nov  10 10:07:23 2020

@author: Christoph
"""

from assignment1 import gcd
from assignment1 import add_frac

def test_gcd():
    assert gcd(4,2) == 2
 
def test_add_frac():
    assert add_frac(1,4,2,8) == print("Das Ergebnis lautet: ", 1, "/", 2)

