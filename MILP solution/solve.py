import highspy

model = highspy.Highs()
# Read a model from LP file model.lp
filename = 'base.lp'
status = model.readModel(filename)
print('Reading model file ', filename, ' returns a status of ', status)

model.run()

solution = model.getSolution()
basis = model.getBasis()
info = model.getInfo()
model_status = model.getModelStatus()
print('Model status = ', model.modelStatusToString(model_status))
print()
print('Optimal objective = ', info.objective_function_value)
print('Iteration count = ', info.simplex_iteration_count)
print('Primal solution status = ', model.solutionStatusToString(info.primal_solution_status))
print('Dual solution status = ', model.solutionStatusToString(info.dual_solution_status))
print('Basis validity = ', model.basisValidityToString(info.basis_validity))

model.writeSolution('./solver_result.sol', 1)
