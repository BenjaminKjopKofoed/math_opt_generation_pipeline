import pulp
import json

# Define the decision variables
soccer_balls = pulp.LpVariable('soccer_balls', 0, None, 'continuous')
basketballs = pulp.LpVariable('basketballs', 0, None, 'continuous')

# Formulate the objective function
problem = pulp*LpProblem("soccer_factory", pulp*LpMaximize)

# Add revenue and time constraints
problem += soccer_balls * 4 - basketballs * 5
problem += (soccer_balls * 5 + basketballs * 7) <= 700
problem += soccer_balls * 3 + basketballs * 4 <= 500

# Solve the problem
solution = problem.solve(pulp*LpMaximize())
 
output = {'The number of soccer balls': int(solution.getVarValue('soccer_balls')),
         'The number of basket balls': int(solution.getVarValue('basketballs')),
         'The total profit': solution.getVarValue(0)} 

# Format the output as a JSON string
print(json.dumps(output, indent=4))