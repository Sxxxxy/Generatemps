import gurobipy as gp

model = gp.read(r"G:\MpsData\Hybridflowshop\0.mps")
model.optimize()
