#!/usr/bin/env python
# encoding: utf-8

from pyomo.environ import *
from pyomo.opt import SolverFactory

n = 5
profits = [3, 2, 4, 3, 1]
weights = [2, 1, 3, 2, 1]
capacity = 4


def buildmodel(**kwargs):
	# Model
	model = ConcreteModel()
	# sets
	model.Items = RangeSet(0, n-1)
	# params
	model.Profits = Param(model.Items, initialize=lambda model, j: profits[j])
	model.Weights = Param(model.Items, initialize=lambda model, j: weights[j])
	model.Capacity = Param(mutable=True)
	model.Capacity.value = capacity
	# variables
	model.x = Var(model.Items, domain=Boolean)
	# objective
	model.obj = Objective(expr = sum(model.Profits[j] * model.x[j] for j in model.Items), sense=maximize)
	# constraints
	model.kc = Constraint(expr = sum(model.Weights[j] * model.x[j] for j in model.Items) <= model.Capacity)
	return model


if __name__ == '__main__':
	model = buildmodel()
	# model.pprint()
	opt = SolverFactory('cplex_persistent')
	for cap in range(min(weights), sum(weights)+1):
		model.Capacity.value = cap
		opt.set_instance(model)
		res = opt.solve()
		print("cap = {} profit = {}".format(cap, value(model.obj)))
