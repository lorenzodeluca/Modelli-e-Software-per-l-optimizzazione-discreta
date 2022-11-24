#!/usr/bin/env python
# encoding: utf-8

from pyomo.environ import *
from pyomo.opt import SolverFactory


def obj_rule(model):
	return sum(model.profit[p] * model.x[p] for p in model.Porte)


def constr_rule(model, c):
	return sum(model.demand[p,c] * model.x[p] for p in model.products) <= model.stock[c]

// manca roba
def buildmodel():
	# Model
	model = AbstractModel()
	# sets
	model.Porte = Set()
	model.Fasi = Set()
	# params
	model.Ore = Param(model.Porte, model.Fasi)
	model.Ub = Param(model.Porte)
	model.Ricavo = Param(model.Porte)
	model.Operai = Param(model.Fasi)
	model.OreSettimana = Param()
	# variables
	model.x = Var(model.Porte, domain=NonNegativeIntegers, bounds=bounds_rule)
	# objective
	model.obj = Objective(rule=obj_rule, sense=maximize)
	# constraints
	model.fr = Constraint(model.components, rule=constr_rule)

	return model


if __name__ == '__main__':
	import sys
	model = buildmodel()
	opt = SolverFactory('cplex_persistent')
	instance = model.create_instance(sys.argv[1])
	opt.set_instance(instance)
	res = opt.solve(tee=True)
	for p in instance.x:
		print("x[{}] = {}".format(p, value(instance.x[p])))
