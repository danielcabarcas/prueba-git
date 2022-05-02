# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:21:27 2022

@author: cabarcas
"""

from math import exp

def bisection(f,a,b,tol= 1e-3):
    # Inicialización
    if f(a)*f(b) > 0:
        print(f'No roots or more than one root in [{a},{b}]')
        return    
    m = (a+b)/2 # Calcular punto medio
    # Ciclo principal
    while abs(f(m)) > tol:
        #Decide en que mitad seguir buscando raíz.
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
        # Recalcula punto medio.
        m = (a+b)/2
    return m

def test_bisection():
    # Tolerance for tests
    tol = 1e-10
    # Lists of tests
    f_vals = [lambda x: x**2-1, lambda x: x**3]
    a_vals = [0., -1.]
    b_vals = [3., 1.]
    root_vals = [1., 0]
    # Recorrer las listas para hacer cada uno de los tests
    for f, a, b, root in zip(f_vals, a_vals, b_vals, root_vals):
        assert abs(bisection(f, a, b)-root) < tol, \
            f'Failed for x = {x}, expected {exp}, but got {f(x)}'

#call the method for f(x)= x**2-4*x+exp(-x)
f = lambda x: x**2-4*x+exp(-x)
sol = bisection(f,-0.5,1,1e-6)
print(f'x = {sol:.2f} is an approximate root, f({sol:.2f}) = {f(sol):E}')

test_bisection()