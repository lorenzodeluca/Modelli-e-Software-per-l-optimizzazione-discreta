#!/usr/bin/env python
# encoding: utf-8

from pyomo.environ import *
from pyomo.opt import SolverFactory


def obj_rule(model):
	return sum(model.Consumo[c] * model.x[c,t] for c in model.COlture)


def bounds_rule(model, j):
	return model.Lb[j]

def ore_rule(model, j):
        return sum( model.Tempo[j]*model.x[j] for j in model.Formaggi) <= model.DispOre

def latte_rule(model, j):
        return sum( model.Lb[j]*model.x[j] for j in model.Formaggi) <= model.DispLatte

def buildmodel():
	# Model
	model = AbstractModel()
	# sets
	model.Tenute = Set()
	model.Colture = Set()
	# params
	model.Dim = Param(model.Tenute)
	model.CapAcqua = Param(model.Tenute)
	model.Profitto = Param(model.Colture)
	model.Consumo = Param(model.Colture)
	model.riposoCampi = Param()
	# variables
	model.x = Var(model.Tenute, model.Colture, domain=NonNegativeIntegers, bounds=bounds_rule)
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
