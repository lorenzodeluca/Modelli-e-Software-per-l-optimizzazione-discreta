#!/usr/bin/env python
# encoding: utf-8

from pyomo.environ import *
from pyomo.opt import SolverFactory


def obj_rule(model):
	return sum((model.Ricavo[j] - (model.CostoLatte*model.Latte[j]))*x[j] for j in model.Formaggi)


def bounds_rule(model, j):
	return null,model.Lb[j]

def ore_rule(model, j):
        return sum( model.Tempo[j]*model.x[j] for j in model.Formaggi) <= model.DispOre

def latte_rule(model, j):
        return sum( model.Lb[j]*model.x[j] for j in model.Formaggi) <= model.DispLatte

def buildmodel():
	# Model
	model = AbstractModel()
	# sets
	model.Formaggi = Set()
	# params
	model.Lb = Param(model.Formaggi)
	model.Ricavo = Param(model.Formaggi)
	model.Tempo = Param(model.Formaggi)
	model.Latte = Param(model.Formaggi)
	model.DispOre = Param()
	model.DispLatte = Param()
	model.CostoLatte = Param()
	# variables
	model.x = Var(model.Formaggi, domain=NonNegativeIntegers, bounds=bounds_rule)
	# objective
	model.obj = Objective(rule=obj_rule, sense=maximize)
	# constraints
	model.oc = Constraint(rule=ore_rule)
	model.lc = Constraint(rule=latte_rule)
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
