# -*- coding: utf-8 -*-

from gurobipy import *

def solve(P, R, Q, A, C, M, n, l, u, f, W, D, X, Z):

    # Create a Gurobi model
    m = Model("max")

    #Create the variables
    x={}
    for r in R:
        for p in P:
            x[r,p]=m.addVar(vtype=GRB.CONTINUOUS, name='x_%s,%s' % (r,p))

    b = {}
    for q in Q:
        for p in P:
            b[q, p] = m.addVar(vtype=GRB.CONTINUOUS, name='b_%s,%s' % (q, p))


    # Integrates the variables to model m
    m.update()

    # Set the objective
    m.setObjective(quicksum(S[p]*quicksum(x[r,p] for r in R)for p in P) - quicksum(A[r]*quicksum(x[r,p] for p in P)for r in R)-quicksum(C[q]*quicksum(b[q,p] for p in P)for q in Q), GRB.MAXIMIZE)

    #Add constraints


    for r in R:
        m.addConstr( quicksum(x[r,p]for p in P) <= m[r])
    for q in Q:
        m.addConstr( quicksum(b[q,p]for p in P) <= n[r])
    for p in P:
        m.addConstr(quicksum(x[r, p] for r in R) <= u[p])
    for p in P:
        m.addConstr(quicksum(x[r, p] for r in R) >= l[p])
    for p in P:
        m.addConstr(quicksum(f[p]*x[r,p] for r in R) <= W)
    for p in P:
        m.addConstr(quicksum(x[r, p] for r in R) <= Z)


    m.optimize()

    m.write("model.lp");

    print ("The total profit is: %g" % m.objval)

    for p in P:
        for r in R:
            print ("The company need %g amount of raw material %s to produce %s" % ( x[r,p].x, r, p))
