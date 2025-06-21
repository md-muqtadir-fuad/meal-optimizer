# -*- coding: utf-8 -*-

from gurobipy import *

def solve(P,R, N, Q, C, S, a, L, U, d, b):

    # Create a Gurobi model
    m = Model("AFP")

    #Create the variables
    x={}
    for r in R:
        for p in P:
            x[r,p]=m.addVar(vtype=GRB.CONTINUOUS, name='x_%s,%s' % (r,p))


    # Integrates the variables to model m
    m.update()

    # Set the objective
    m.setObjective(quicksum(C[r]*quicksum(x[r,p] for p in P)for r in R) + 
                    quicksum(quicksum(quicksum(S[r,q,p]*x[r,p] for p in P)for r in R)for q in Q), GRB.MINIMIZE)

    #Add constraints


    for p in P:
        m.addConstr( quicksum(x[r,p]for r in R) >= d[p])
    for r in R:
        m.addConstr( quicksum(x[r,p]for p in P) <= b[r])

    for p in P:
        for i in N:
            if i== 'proteins' or i=='lipids':
                m.addConstr( quicksum(a[i,r]*x[r,p] for r in R )>= L[i]*quicksum(x[r,p]for r in R))

    for p in P:
        for i in N:
            if i== 'fiber':
                m.addConstr( quicksum(a[i,r]*x[r,p] for r in R )<= U[i]*quicksum(x[r,p]for r in R))


    m.optimize()

    m.write("model.lp");

    print ("The total cost is: %g" % m.objval)

    for p in P:
        for r in R:
            print ("The company need %g amount of raw material %s to produce %s" % ( x[r,p].x, r, p))
