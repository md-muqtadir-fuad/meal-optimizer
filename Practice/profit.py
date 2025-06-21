# -*- coding: utf-8 -*-

# sets
P=['cake', 'bread','cupcake','pastries','donuts','croissants']
R=['flour', 'sugar', 'eggs','syrup','oil']
Q=['preparing', 'mixing', 'baking', 'decorating']

#parameters
S={'cakes':5.00,
   'bread': 4.00,
    'cupcake': 2.00,
    'pastries': 2.50,
    'donuts': 2.00,
   'croissants': 3.00}

A={'flour':0.48,
   'sugar':1.1,
   'eggs':0.25,
   'syrup':1.5,
   'oil':1.2}

C={'preparing':0.5,
   'mixing':0.75,
   'baking':2.00,
   'decorating':1.00}

M={'flour':45,
   'sugar':25,
   'eggs':70,
   'syrup':10,
   'oil':1000}

N={'preparing':10,
   'mixing':17,
   'baking':25,
   'decorating':12}

L={'cakes':5.00,
   'bread': 5.00,
    'cupcake': 4.00,
    'pastries': 2.00,
    'donuts': 5.00,
   'croissants': 7.00}

U={'cakes':10,
   'bread': 45,
    'cupcake': 160,
    'pastries': 85,
    'donuts': 80,
   'croissants': 60}

F={'cakes':3.00,
   'bread': 1.00,
    'cupcake': 0.50,
    'pastries': 0.50,
    'donuts': 0.20,
   'croissants': 0.10}

D={'cakes':1.00,
   'bread': 0.50,
    'cupcake':0.20,
    'pastries': 0.250,
    'donuts': 0.20,
   'croissants': 0.30}

W=250
X=25
Z=450

import maxmodel

maxmodel.solve(P,R,Q,A,C,M,N,L,U,F,,W,D,X,Z)