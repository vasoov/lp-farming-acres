#Farming linear programming problem
from pulp import *

# The challenge is to maximise the profit by producing an optimum quantity of cotton and potatoes
# X - "Cotton", profit margin of $207 per acre unit
# Y - "Potatoes", profit margin of $200 per acre unit
#
model = LpProblem("Profit Maximising", LpMaximize)

# We cannot have negative amounts, so category for each item type is an integer.
#X >= 0, Y >= 0 : Input (Changing) cells
X = LpVariable('X', lowBound=0, cat='Integer')
Y = LpVariable('Y', lowBound=0, cat='Integer')

#Our objective is to maximise the profit
model += 207 * X + 200 * Y, "Total Profit"

#Setup the constraints (parts available in stock)
planted_acres = X + Y
cotton_acres = X
water_needed = 30 * X + 15 * Y

#Add constraints to the model
model += planted_acres <=150
model += cotton_acres <= 60
model += water_needed <= 3000

#Print the problem
print (model)

#Solve the problem
model.solve()
print ("Status : ", LpStatus[model.status])

#Print our changing cells
print ("Acres of cotton   = ", X.varValue)
print ("Acres of potatoes    = ", Y.varValue)

#Print our objective function value - Result (Target) cell
print ("Total Profit             = ", value(model.objective))