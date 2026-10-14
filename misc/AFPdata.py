# -*- coding: utf-8 -*-

# sets
P=['grannules', 'powder']
R=['oat', 'maize', 'molasses']
N=['proteins', 'lipids', 'fiber']
Q=['grinding', 'blending', 'granulating', 'sieving']


#parameters
C={'oat':0.13, 
   'maize': 0.17,
   'molasses': 0.12}

S={('oat','grinding','grannules'):0.25,
   ('maize','grinding','grannules'):0.25,
   ('molasses','grinding','grannules'):0,
   ('oat','blending','grannules'):0.05,
   ('maize','blending','grannules'):0.05,
   ('molasses','blending','grannules'):0.05,
   ('oat','granulating','grannules'):0.42,
   ('maize','granulating','grannules'):0.42,
   ('molasses','granulating','grannules'):0.42,
   ('oat','sieving','grannules'):0,
   ('maize','sieving','grannules'):0,
   ('molasses','sieving','grannules'):0,
   ('oat','grinding','powder'):0.25,
   ('maize','grinding','powder'):0.25,
   ('molasses','grinding','powder'):0,
   ('oat','blending','powder'):0.05,
   ('maize','blending','powder'):0.05,
   ('molasses','blending','powder'):0.05,
   ('oat','granulating','powder'):0,
   ('maize','granulating','powder'):0,
   ('molasses','granulating','powder'):0,
   ('oat','sieving','powder'):0.17,
   ('maize','sieving','powder'):0.17,
   ('molasses','sieving','powder'):0.17}


a={('proteins','oat'):13.6,
   ('proteins','maize'):4.1,
    ('proteins','molasses'):5,
    ('lipids','oat'):7.1,
   ('lipids','maize'):2.4,
    ('lipids','molasses'):0.3,
   ('fiber','oat'):7,
   ('fiber','maize'):3.7,
    ('fiber','molasses'):25}

L={'proteins':9.5,
   'lipids':2}

U={'fiber':6}

d={'grannules':9000,
   'powder':12000}

b={'oat':11900,
   'maize':23500,
   'molasses':750}

import AFPmodel

AFPmodel.solve(P,R, N, Q, C, S, a, L, U, d, b)