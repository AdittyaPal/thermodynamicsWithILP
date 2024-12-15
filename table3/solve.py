import highspy

model = highspy.Highs()
# Read a model from LP file model.lp
#filename = '32Vertices.lp'
#filename = '43Vertices.lp'
#filename = '50Vertices.lp'
filename = '58Vertices.lp'
#filename = '67Vertices.lp'
#filename = '77Vertices.lp'
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

#model.writeSolution('./32Vertices.sol', 1)
#model.writeSolution('./43Vertices.sol', 1)
#model.writeSolution('./50Vertices.sol', 1)
model.writeSolution('./58Vertices.sol', 1)
#model.writeSolution('./67Vertices.sol', 1)
#model.writeSolution('./77Vertices.sol', 1)
