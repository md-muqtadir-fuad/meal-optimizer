#Create the variables
from gurobipy import GRB, Model
from gurobipy import LinExpr

m = Model()

# Create variables x1 to x34
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1")
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2")
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3")
x4 = m.addVar(vtype=GRB.CONTINUOUS, name="x4")
x5 = m.addVar(vtype=GRB.CONTINUOUS, name="x5")
x6 = m.addVar(vtype=GRB.CONTINUOUS, name="x6")
x7 = m.addVar(vtype=GRB.CONTINUOUS, name="x7")
x8 = m.addVar(vtype=GRB.CONTINUOUS, name="x8")
x9 = m.addVar(vtype=GRB.CONTINUOUS, name="x9")
x10 = m.addVar(vtype=GRB.CONTINUOUS, name="x10")
x11 = m.addVar(vtype=GRB.CONTINUOUS, name="x11")
x12 = m.addVar(vtype=GRB.CONTINUOUS, name="x12")
x13 = m.addVar(vtype=GRB.CONTINUOUS, name="x13")
x14 = m.addVar(vtype=GRB.CONTINUOUS, name="x14")
x15 = m.addVar(vtype=GRB.CONTINUOUS, name="x15")
x16 = m.addVar(vtype=GRB.CONTINUOUS, name="x16")
x17 = m.addVar(vtype=GRB.CONTINUOUS, name="x17")
x18 = m.addVar(vtype=GRB.CONTINUOUS, name="x18")
x19 = m.addVar(vtype=GRB.CONTINUOUS, name="x19")
x20 = m.addVar(vtype=GRB.CONTINUOUS, name="x20")
x21 = m.addVar(vtype=GRB.CONTINUOUS, name="x21")
x22 = m.addVar(vtype=GRB.CONTINUOUS, name="x22")
x23 = m.addVar(vtype=GRB.CONTINUOUS, name="x23")
x24 = m.addVar(vtype=GRB.CONTINUOUS, name="x24")
x25 = m.addVar(vtype=GRB.CONTINUOUS, name="x25")
x26 = m.addVar(vtype=GRB.CONTINUOUS, name="x26")
x27 = m.addVar(vtype=GRB.CONTINUOUS, name="x27")
x28 = m.addVar(vtype=GRB.CONTINUOUS, name="x28")
x29 = m.addVar(vtype=GRB.CONTINUOUS, name="x29")
x30 = m.addVar(vtype=GRB.CONTINUOUS, name="x30")
x31 = m.addVar(vtype=GRB.CONTINUOUS, name="x31")
x32 = m.addVar(vtype=GRB.CONTINUOUS, name="x32")
x33 = m.addVar(vtype=GRB.CONTINUOUS, name="x33")
x34 = m.addVar(vtype=GRB.CONTINUOUS, name="x34")
# Update the model to include variables and constraints
m.update()


# Create the price list
price_list = [180, 160, 250, 330, 450, 610, 310, 65, 25, 12, 80, 50, 30, 35, 110, 30, 50, 60, 30, 30, 160, 35, 440, 60, 35, 50, 80, 650, 1000, 450, 95, 120, 50, 600]

# Create the expression
expression = LinExpr()

# Add the terms to the expression
for i in range(len(price_list)):
    expression.add(price_list[i] * globals()[f'x{i+1}'])
#Objective Function
m.setObjective(expression, GRB.MINIMIZE)


# Create constraints for each variable using the corresponding lower and upper bounds
m.addConstr(x1 >= 600, "constraint_x1_lower_bound")
m.addConstr(x1 <= 2500, "constraint_x1_upper_bound")

m.addConstr(x2 >= 300, "constraint_x2_lower_bound")
m.addConstr(x2 <= 1200, "constraint_x2_upper_bound")

m.addConstr(x3 >= 300, "constraint_x3_lower_bound")
m.addConstr(x3 <= 1200, "constraint_x3_upper_bound")

m.addConstr(x4 >= 300, "constraint_x4_lower_bound")
m.addConstr(x4 <= 1200, "constraint_x4_upper_bound")

m.addConstr(x5 >= 100, "constraint_x5_lower_bound")
m.addConstr(x5 <= 1200, "constraint_x5_upper_bound")

m.addConstr(x6 >= 100, "constraint_x6_lower_bound")
m.addConstr(x6 <= 1200, "constraint_x6_upper_bound")

m.addConstr(x7 >= 100, "constraint_x7_lower_bound")
m.addConstr(x7 <= 1200, "constraint_x7_upper_bound")

m.addConstr(x8 >= 100, "constraint_x8_lower_bound")
m.addConstr(x8 <= 1200, "constraint_x8_upper_bound")

m.addConstr(x9 >= 100, "constraint_x9_lower_bound")
m.addConstr(x9 <= 1200, "constraint_x9_upper_bound")

m.addConstr(x10 >= 200, "constraint_x10_lower_bound")
m.addConstr(x10 <= 900, "constraint_x10_upper_bound")

m.addConstr(x11 >= 450, "constraint_x11_lower_bound")
m.addConstr(x11 <= 900, "constraint_x11_upper_bound")

m.addConstr(x12 >= 300, "constraint_x12_lower_bound")
m.addConstr(x12 <= 900, "constraint_x12_upper_bound")

m.addConstr(x13 >= 300, "constraint_x13_lower_bound")
m.addConstr(x13 <= 900, "constraint_x13_upper_bound")

m.addConstr(x14 >= 900, "constraint_x14_lower_bound")
m.addConstr(x14 <= 1600, "constraint_x14_upper_bound")

m.addConstr(x15 >= 100, "constraint_x15_lower_bound")
m.addConstr(x15 <= 900, "constraint_x15_upper_bound")

m.addConstr(x16 >= 100, "constraint_x16_lower_bound")
m.addConstr(x16 <= 900, "constraint_x16_upper_bound")

m.addConstr(x17 >= 900, "constraint_x17_lower_bound")
m.addConstr(x17 <= 1600, "constraint_x17_upper_bound")

m.addConstr(x18 >= 900, "constraint_x18_lower_bound")
m.addConstr(x18 <= 1600, "constraint_x18_upper_bound")

m.addConstr(x19 >= 900, "constraint_x19_lower_bound")
m.addConstr(x19 <= 1600, "constraint_x19_upper_bound")

m.addConstr(x20 >= 900, "constraint_x20_lower_bound")
m.addConstr(x20 <= 1600, "constraint_x20_upper_bound")

m.addConstr(x21 >= 240, "constraint_x21")
m.addConstr(x22 >= 300, "constraint_x22")
m.addConstr(x23 >= 50, "constraint_x23")
m.addConstr(x24 >= 300, "constraint_x24")
m.addConstr(x25 >= 45, "constraint_x25")
m.addConstr(x26 >= 60, "constraint_x26")
m.addConstr(x27 >= 450, "constraint_x27")
m.addConstr(x28 >= 150, "constraint_x28")
m.addConstr(x29 >= 25, "constraint_x29")
m.addConstr(x30 >= 25, "constraint_x30")
m.addConstr(x31 >= 1000, "constraint_x31")
m.addConstr(x32 >= 400, "constraint_x32")
m.addConstr(x33 == 2600, "constraint_x33")
m.addConstr(x34 ==4, "constraint_x34")

#nutrition constraints
m.addConstr((31*x1 + 13*x2 + 26*x3 + 22*x4 + 22.6*x5 + 18*x6 + 24*x7 + 8.7*x8 + 0.8*x9 + 0.7*x10 + 0.5*x11 + 2.5*x12 + 2.8*x13 + 3*x14 + 2.8*x15 + 0.9*x16 + 3.15*x17 + 2.4*x18 + 1.3*x19 + 1.8*x20 + 0*x21 +26*x28 + 25*x29 + 23*x30 + 9*x31 + 1.1*x32 + 2.7*x33)*10 >= 507000, "constraint_x35")
m.addConstr((0*x1 + 0.7*x2 + 0*x3 + 0*x4 + 14*x5 + 0*x6 + 0*x7 + 23*x8 + 8.7*x9 + 3.4*x10 + 11*x11 + 21*x12 + 5.4*x13 + 3.8*x14 + 8.3*x15 + 5.4*x16 + 2.33*x17 + 7.2*x18 + 5.5*x19 + 4.1*x20 + 0*x21 + 0*x28 + 0*x29 + 1.5*x30 + 20*x31 + 9.3*x32 + 28*x33)*10 >= 1521000, "constraint_x36")
m.addConstr((3.6*x1 + 9.5*x2 + 2.7*x3 + 12*x4 + 12.5*x5 + 7.2*x6 + 8.1*x7 + 0.5*x8 + 0.2*x9 + 0.2*x10 + 0.3*x11 + 0.1*x12 + 0.2*x13 + 0.3*x14 + 0.4*x15 + 0*x16 + 0.4*x17 + 0.4*x18 + 0.1*x19 + 0.5*x20 + 100*x21 + 17*x28 + 21*x29 + 1.7*x30 + 0.4*x31 + 0.3*x32 + 0.3*x33)*10 >= 304200, "constraint_x37")


# Add constraint:

m.optimize()

m.write("model.lp")

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
print('Objective Function Value: %g' % m.objVal)
